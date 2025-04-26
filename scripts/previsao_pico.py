import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
import io
import base64

ccr_estacoes = {
    "Linha 4 Amarela": ["Butantã", "Pinheiros", "Faria Lima", "Paulista", "Consolação", "República", "Luz"],
    "Linha 8 Diamante": ["Osasco", "Presidente Altino", "Ceasa", "Villa Lobos", "Pinheiros", "Cidade Jardim", "Vila Olímpia"],
    "Linha 9 Esmeralda": ["Osasco", "Presidente Altino", "Ceasa", "Villa Lobos", "Pinheiros", "Cidade Jardim",
                          "Vila Olímpia", "Berrini", "Morumbi", "Granja Julieta", "João Dias", "Santo Amaro",
                          "Socorro", "Jurubatuba", "Autódromo", "Interlagos", "Grajaú"]
}

df = pd.read_csv("dados/fluxo_passageiros.csv")
df["Horario"] = pd.to_datetime(df["Horario"], format='%H:%M').dt.time

def estacao_valida(nome_estacao):
    return any(nome_estacao in estacoes for estacoes in ccr_estacoes.values())

def obter_fluxo(estacao, horario=None):
    if not estacao_valida(estacao):
        return {"erro": "Estação não pertence à CCR."}, 400

    df_estacao = df[df["Estacao"] == estacao].copy()
    if df_estacao.empty:
        return {"erro": "Não há dados disponíveis para essa estação."}, 404

    if horario:
        try:
            horario = datetime.strptime(horario, "%H:%M").time()
        except ValueError:
            return {"erro": "Formato de horário inválido. Use HH:MM."}, 400

        if horario not in df_estacao["Horario"].values:
            return {"erro": f"Não há dados para o horário {horario.strftime('%H:%M')}."}, 404

    else:
        horario_atual = datetime.now().time()
        horario = min(df_estacao["Horario"], key=lambda x: abs(datetime.combine(datetime.today(), x) - datetime.combine(datetime.today(), horario_atual)))

    fluxo = df_estacao[df_estacao["Horario"] == horario]["Passageiros"].values[0]
    return {
        "estacao": estacao,
        "horario": horario.strftime("%H:%M"),
        "passageiros": int(fluxo)
    }, 200

def gerar_grafico(estacao):
    if not estacao_valida(estacao):
        return None, 400

    df_estacao = df[df["Estacao"] == estacao].copy()
    if df_estacao.empty:
        return None, 404

    df_estacao["Horario_dt"] = pd.to_datetime(df_estacao["Horario"].astype(str), format='%H:%M:%S')
    df_estacao = df_estacao.sort_values(by="Horario_dt")

    plt.figure(figsize=(10, 5))
    plt.plot(df_estacao["Horario_dt"], df_estacao["Passageiros"], marker='o', linestyle='-', color='blue')
    plt.title(f"Fluxo de Passageiros - Estação {estacao}")
    plt.xlabel("Horário")
    plt.ylabel("Número de Passageiros")
    plt.xticks(rotation=45)
    plt.grid(True)

    pico = df_estacao.loc[df_estacao["Passageiros"].idxmax()]
    plt.axvline(pico["Horario_dt"], color='red', linestyle='--', label='Horário de Pico')
    plt.legend()
    plt.tight_layout()

    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    plt.close()
    buffer.seek(0)
    imagem_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
    return imagem_base64, 200

def previsao_pico_menu():
    print("\n--- Previsão de Pico ---")
    print("1. Obter pico atual de uma estação")
    print("2. Obter pico de uma estação em um horário específico")
    print("3. Obter gráfico do fluxo de uma estação")
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        estacao = input("Digite o nome da estação: ")
        resultado, status = obter_fluxo(estacao)
        print(resultado)

    elif opcao == '2':
        estacao = input("Digite o nome da estação: ")
        horario = input("Digite o horário no formato HH:MM: ")
        resultado, status = obter_fluxo(estacao, horario)
        print(resultado)

    elif opcao == '3':
        estacao = input("Digite o nome da estação: ")
        gerar_grafico(estacao)
        # if status == 200:
        #     print(f"Gráfico gerado em base64! (tamanho {len(imagem_base64)} caracteres)")
        # else:
        #     print("Erro ao gerar gráfico.")
    else:
        print("Opção inválida!")