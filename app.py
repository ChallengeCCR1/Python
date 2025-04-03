import time
import os
import json
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime

'''
O que devedemos focar para a próxima sprint é:
1. Integração com banco de dados;
2. Deixar o sistema extremamente parecido com o banco de dados;
3. Integrar com o front;
4. consumir uma API externa -> se formos usar uma API para dados da CPTM, devemos mudar
a estrutura do sistema, ja que informações sobre linhas que não pertencem a CCR serão desconsideradas.
8. na previsao de pico exibir o pico no terminal somente do horario que o usuario esta, e dar a opção tbm
do usuario escolher um horario para saber o pico numa determinada estação
9. colocar data na viagem
10. deixar o mapa mais bonito (talvez)
11. AO iniciar viagem, só aparecer informações de pico em estações que são da CCR (puxar da base de dados talvez, n sei)
12. colocar .lower(), .strip() em validacoes, cadastro e login por ex
'''

# def limpar tela
def limpar_tela():
    os.system('clear' if os.name == 'posix' else 'cls')

# Banco de dados simulado
usuarios = {}
viagens = []
avisos = [
    "Linha 4 Amarela com grande fluxo de passageiros neste momento.", #0
    "Linha 8 Diamante com atrasos de 10 minutos.", #1
    "Linha 9 Esmeralda operando normalmente."#2
]

## def de salvar arquivos no json
def salvar_viagens_json():
    try:
        with open('viagens.json', mode='w', encoding='utf-8') as arq:
            json.dump(viagens, arq, ensure_ascii=False, indent=4)
    except Exception as e:
        print(f"Ocorreu um erro ao salvar o arquivo: {e}")

## def para carregar as viagens do json
def carregar_viagens_json():
    global viagens
    try:
        with open('viagens.json', mode='r', encoding='utf-8') as arq:
            viagens = json.load(arq)
    except FileNotFoundError:
        viagens = []
    except Exception as e:
        print(f"Erro ao carregar viagem em JSON: {e}")
        viagens = []

## def salvar_usuarios_json
def salvar_usuarios_json():
    """Salva os usuários no arquivo JSON."""
    try:
        with open('usuarios.json', mode='w', encoding='utf-8') as arq:
            json.dump(usuarios, arq, ensure_ascii=False, indent=4)
    except Exception as e:
        print(f"Ocorreu um erro ao salvar o arquivo: {e}")

def carregar_usuarios():
    """Carrega os usuários do arquivo JSON."""
    global usuarios
    try:
        with open('usuarios.json', mode='r', encoding='utf-8') as arq:
            usuarios = json.load(arq)
    except FileNotFoundError:
        usuarios = {}
    except Exception as e:
        print(f"Ocorreu um erro ao carregar o arquivo: {e}")
        usuarios = {}

def cadastrar_usuario():
    """Cadastra um novo usuário."""
    try: 
        print("\n===== Cadastro =====")
        usuario = input("Digite um nome de usuário: ").strip()
        if usuario in usuarios:
            print("Usuário já cadastrado. Tente fazer login.")
            return False
        email = input("Digite seu e-mail: ").strip()
        senha = input("Digite uma senha: ").strip()

        usuarios[usuario] = {"email": email, "senha": senha}
        salvar_usuarios_json()
        print("Cadastro realizado com sucesso! Você agora pode fazer login.")
        input("Pressione 'Enter' para continuar...")
        return True
    except Exception as e:
        print(f"Ocorreu um erro durante o cadastro: {e}")

def fazer_login():
    """Realiza o login de um usuário utilizando e-mail e senha."""
    try:
        print("\n===== Login =====")
        email_input = input("E-mail: ").strip()
        senha_input = input("Senha: ").strip()
        
        for usuario, dados in usuarios.items():
            if dados["email"] == email_input:
                if dados["senha"] == senha_input:
                    print("Login realizado com sucesso! Aproveite a nossa plataforma!")
                    input("Pressione 'Enter' para continuar...")
                    return usuario
                else:
                    print("Senha incorreta!")
                    input("Pressione 'Enter' para tentar novamente...")
                    return None
        print("E-mail não encontrado!")
        input("Pressione 'Enter' para tentar novamente...")
    except Exception as e:
        print(f"Ocorreu um erro ao fazer login: {e}")
    return None

# função de voltar ou sair
def voltar_sair():
    try: 
        while True:
            escolha = input("\nDigite 'V' para voltar ou 'S' para sair: ").strip().lower()
            if escolha == 'v':
                return
            elif escolha == 's':
                print("Saindo do sistema...")
                exit()
            else:
                print("Opção inválida. Tente novamente.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

# tempo de viagem entre estações linha 9 esmeralda
tempos_viagem = {
    ("Osasco", "Presidente Altino") : 5,
    ("Presidente Altino", "Ceasa") : 5,
    ("Ceasa", "Vila Lobos") : 5,
    ("Vila Lobos", "Pinheiros") : 5,
    ("Pinheiros", "Cidade Jardim") : 5,
    ("Cidade Jardim", "Vila Olimpia") : 5,
    ("Vila Olimpia", "Berrini") : 5,
    ("Berrini", "Morumbi") : 5,
    ("Morumbi", "Granja Julieta") : 5,
    ("Granja Julieta", "João Dias") : 5,
    ("João Dias", "Santo Amaro") : 5,
    ("Santo Amaro", "Socorro") : 5,
    ("Socorro", "Jurubatuba") : 5,
    ("Jurubatuba", "Autódromo") : 5,
    ("Autódromo", "Interlargos") : 5,
    ("Interlargos", "Grajaú") : 5,
}

# estações linha 9 esmeralda
estacoes = [
    "Osasco", "Presidente Altino", "Ceasa", "Vila Lobos", "Pinheiros",
    "Cidade Jardim", "Vila Olimpia", "Berrini", "Morumbi", "Granja Julieta",
    "João Dias", "Santo Amaro", "Socorro", "Jurubatuba", "Autódromo",
    "Interlagos", "Grajaú"
]

def calcular_tempo_total(origem, destino):
    if origem not in estacoes or destino not in estacoes:
        return None, "Estação inválida. Tente novamente!"
    
    idx_origem = estacoes.index(origem)
    idx_destino = estacoes.index(destino)

    if idx_origem > idx_destino:
        idx_origem, idx_destino = idx_destino, idx_origem
    
    tempo_total = 0
    for i in range(idx_origem, idx_destino):
        tempo_total += tempos_viagem.get((estacoes[i], estacoes[i + 1]), 0)

    return tempo_total, None

dados_estacao = {
    "08:00": 1200,
    "09:00": 700,
    "10:00": 500,
    "11:00": 400,
    "12:00": 670,
    "13:00": 789,
    "14:00": 600,
    "15:00": 400,
    "16:00": 560,
    "17:00": 700,
    "18:00": 980,
    "19:00": 1240,
    "20:00": 1300,
    "21:00": 1000,
    "22:00": 987,
    "23:00": 654
}
    
def encontrar_horario_proximo(hora_partida):
    """Encontra o horário mais próximo da hora_partida dentro dos horários disponíveis no dicionário."""
    horarios_disponiveis = list(dados_estacao.keys())
    horarios_disponiveis.sort() 
    for horario in reversed(horarios_disponiveis):
        if hora_partida >= horario:
            return horario
    return horarios_disponiveis[0]

def iniciar_viagem(usuario):
    """Inicia a simulação de uma viagem."""
    try:
        print("\n===== Iniciar Viagem =====")
        origem = input("Digite a estação de origem: ").strip()
        destino = input("Digite a estação de destino: ").strip()

        tempo_estimado, erro = calcular_tempo_total(origem, destino)
        if erro:
            print(erro)
            return

        print(f"Tempo estimado de viagem de {origem} para {destino}: {tempo_estimado} minutos.")

        confirmacao = input("Deseja iniciar a viagem? (s/n): ").strip().lower()
        if confirmacao != 's':
            print("Viagem cancelada.")
            return

        hora_partida = datetime.now()
        print(f"Viagem iniciada às {hora_partida.strftime('%H:%M:%S')}.")
        print("Aperte Enter para encerrar a viagem...")

        # Aguarda o usuário pressionar Enter para encerrar a viagem
        input()

        print(f"Finalinado a sua viagem, {usuario}...")
        time.sleep(3)

        hora_chegada = datetime.now()
        tempo_real = (hora_chegada - hora_partida).total_seconds() / 60
        print(f"Viagem concluída às {hora_chegada.strftime('%H:%M:%S')}.")
        print(f"Tempo real decorrido: {tempo_real:.2f} minutos.")

        # Registro da viagem
        viagem = {
            "usuario": usuario,
            "origem": origem,
            "destino": destino,
            "partida": hora_partida.strftime('%H:%M:%S'),
            "chegada": hora_chegada.strftime('%H:%M:%S'),
            "tempo_estimado": tempo_estimado,
            "tempo_real": tempo_real
        }
        viagens.append(viagem)
        salvar_viagens_json()

    except Exception as e:
        print(f"Erro ao iniciar a viagem: {e}")

    input("Pressione Enter para voltar...")

# Relatório de viagens
def exibir_relatorio(usuario):
    try:
        print(f"\n===== Relatório de Viagens de {usuario} =====")
        
        # Verifica se a lista de viagens foi corretamente registrada
        if not viagens:
            print("Nenhuma viagem registrada até o momento.")
            input("\nPressione Enter para voltar ao menu...")  # Pausa para o usuário ler
            voltar_sair()  # Voltar ao menu
            return

        viagens_usuario = [v for v in viagens if v["usuario"] == usuario]
        
        if not viagens_usuario:
            print("Nenhuma viagem registrada para este usuário.")
            input("\nPressione Enter para voltar ao menu...")  # Pausa para o usuário ler
        else:
            for i, v in enumerate(viagens_usuario, 1):
                print(f"\n🚆 Viagem {i}")
                print(f"   📍 Origem: {v['origem']}")
                print(f"   🎯 Destino: {v['destino']}")
                print(f"   ⏳ Partida: {v['partida']} | 🏁 Chegada: {v['chegada']}")

        input("\nPressione Enter para voltar ao menu...")
        limpar_tela()

    except Exception as e:
        print(f"❌ Erro ao exibir o relatório: {e}")

# Previsão de pico
def previsao_pico():
    try:
        print("\n===== Previsão de Pico =====")

        # Dicionário de estações da CCR
        ccr_estacoes = {
            "Linha 4 Amarela": ["Butantã", "Pinheiros", "Faria Lima", "Paulista", "Consolação", "República", "Luz"],
            "Linha 8 Diamante": ["Osasco", "Presidente Altino", "Ceasa", "Villa Lobos", "Pinheiros", "Cidade Jardim", "Vila Olímpia"],
            "Linha 9 Esmeralda": ["Osasco", "Presidente Altino", "Ceasa", "Villa Lobos", "Pinheiros", "Cidade Jardim",
                                  "Vila Olímpia", "Berrini", "Morumbi", "Granja Julieta", "João Dias", "Santo Amaro",
                                  "Socorro", "Jurubatuba", "Autódromo", "Interlagos", "Grajaú"]
        }

        # Carregar os dados do CSV
        df = pd.read_csv("fluxo_passageiros.csv")

        while True:
            # Recebe a estação
            escolha_estacao = input("Informe a estação que deseja saber o pico de passageiros: ").strip()

            # Verifica se a estação pertence a alguma linha da CCR
            estacao_encontrada = any(escolha_estacao in estacoes for estacoes in ccr_estacoes.values())

            if not estacao_encontrada:
                print(f"A estação {escolha_estacao} não pertence a uma linha da CCR. Tente novamente.")
                continue  # Retorna ao início do loop para tentar novamente

            # Filtrar os dados da estação escolhida
            df_estacao = df[df["Estacao"] == escolha_estacao].copy()

            if df_estacao.empty:
                print(f"Não há dados disponíveis para a estação {escolha_estacao}.")
                continue

            # Converter a coluna "Horario" para objetos datetime.time
            df_estacao["Horario"] = pd.to_datetime(df_estacao["Horario"], format='%H:%M').dt.time

            print("\nOpções:")
            print("1. Ver o pico no horário atual")
            print("2. Escolher um horário específico")
            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                horario_atual = datetime.now().time()
                horario_mais_proximo = min(df_estacao["Horario"], key=lambda x: abs(datetime.combine(datetime.today(), x) - datetime.combine(datetime.today(), horario_atual)))
                fluxo_passageiros = df_estacao[df_estacao["Horario"] == horario_mais_proximo]["Passageiros"].values[0]

                print(f"No horário mais próximo ({horario_mais_proximo.strftime('%H:%M')}), a estação {escolha_estacao} tem {fluxo_passageiros} passageiros.")

            elif opcao == "2":
                horario_escolhido = input("Digite o horário no formato HH:MM: ").strip()

                try:
                    horario_escolhido = datetime.strptime(horario_escolhido, "%H:%M").time()
                except ValueError:
                    print("Formato de horário inválido. Tente novamente.")
                    continue

                if horario_escolhido not in df_estacao["Horario"].values:
                    print(f"Não há registros para o horário {horario_escolhido.strftime('%H:%M')}.")
                else:
                    fluxo_passageiros = df_estacao[df_estacao["Horario"] == horario_escolhido]["Passageiros"].values[0]
                    print(f"No horário {horario_escolhido.strftime('%H:%M')}, a estação {escolha_estacao} tem {fluxo_passageiros} passageiros.")

            else:
                print("Opção inválida. Retornando ao menu.")
                continue

            input("\nPressione 'Enter' para voltar ao menu...")
            break

    except Exception as e:
        print(f"Ocorreu um erro ao prever o pico: {e}")


def mapa_linha():
    try:
        print("\n===== Mapa =====")
        print("1. Linha 9 Esmeralda")
        print("2. Linha 4 Amarela (em breve)")
        print("3. Linha 8 Diamante (em breve)")

        opcao = input("Escolha uma linha para ver o mapa: ")

        if opcao == "1":
            exibir_mapa_linha9()
        else:
            print("Essa linha ainda não está disponível!")

            voltar_sair()
    except Exception as e:
        print(f"Erro ao exibir as informações da linha: {e}")

def exibir_mapa_linha9():
    print("\n===== Mapa da Linha 9 Esmeralda =====")

    
    estacoes_matriz = [
        ["Osasco", "Presidente Altino", "Ceasa"], 
        ["Villa Lobos", "Pinheiros", "Cidade Jardim"], 
        ["Vila Olímpia", "Berrini", "Morumbi"], 
        ["Granja Julieta", "João Dias", "Santo Amaro"], 
        ["Socorro", "Jurubatuba", "Autódromo", "Interlagos", "Grajaú"] 
    ]

    # Imprimindo a matriz de estações de forma legível
    for trecho in estacoes_matriz:
        print(" -> ".join(trecho))

    voltar_sair()

def centro_controle_operacional():
    while True:
        try:
            print("\n===== Centro de Controle Operacional =====")
            print("1. Linha 4 Amarela. ")
            print("2. Linha 8 Diamante. ")
            print("3. Linha 9 Esmeralda. ")
            print("4. Retornar ao menu principal. ")
            opcao_linha = input("Escolha uma opção: ")

            if opcao_linha == "1":
                print(avisos[0])
            elif opcao_linha == "2":
                print(avisos[1])
            elif opcao_linha == "3":
                print(avisos[2])
            elif opcao_linha == "4":
                break
            else:
                print("Opção inválida. Por favor, escolha uma opção válida.")
                continue

            input("Pressione 'Enter' para retornar ao menu de opções...")
            
        except Exception as e:
            print(f"Erro ao exibir o painel de avisos: {e}")
        limpar_tela()

# menu de cadastro/login
def menu_inicial():
    usuario = None
    while usuario is None:
        try:
            print(f"\nSeja bem-vindo ao Sistema da Future Station!")
            print("1. Cadastrar Usuário")
            print("2. Fazer Login")
            print("3. Sair")

            opcao = input("Escolha uma opção: ")
        
            if opcao == '1':
                cadastrar_usuario()
            elif opcao == '2':
                usuario = fazer_login()
            elif opcao == '3':
                print("Saindo...")
                exit()
            else:
                print("Opção inválida!")
            
        except Exception as e:
            print(f"Ocorreu um erro inesperado no menu: {e}")

    limpar_tela()

    return usuario

## menu após login
def menu_principal(usuario):
    while True:
        try:
            print(f"Bem vindo, {usuario}!")
            print("1. Mapa")
            print("2. Iniciar viagem")
            print("3. Relatório de viagens")
            print("4. Painel de avisos")
            print("5. Previsão de pico")
            print("6. logout")

            opcao = input("Escolha uma opção: ")

            if opcao == '1':
                mapa_linha()
            elif opcao == '2':
                iniciar_viagem(usuario)
            elif opcao == '3':
                exibir_relatorio(usuario)
            elif opcao == '4':
                centro_controle_operacional()
            elif opcao == '5':
                previsao_pico()
            elif opcao == '6':
                print(f"Poxa, {usuario}! Parece que escolheu sair...")
                return
            else:
                print("Opção inválida!")

        except Exception as e:
            print(f"Ocorreu um erro iniesperado: {e}")

        limpar_tela()

if __name__ == "__main__":
    carregar_viagens_json()
    carregar_usuarios()
    while True:
        usuario_logado = menu_inicial()
        menu_principal(usuario_logado)