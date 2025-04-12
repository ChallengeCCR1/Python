# Previsão de pico
from datetime import datetime
from matplotlib import pyplot as plt
import pandas as pd


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
            escolha_estacao = input("Informe a estação que deseja saber o pico de passageiros: ").strip()

            estacao_encontrada = any(escolha_estacao in estacoes for estacoes in ccr_estacoes.values())

            if not estacao_encontrada:
                print(f"A estação {escolha_estacao} não pertence a uma linha da CCR. Tente novamente.")
                continue

            df_estacao = df[df["Estacao"] == escolha_estacao].copy()

            if df_estacao.empty:
                print(f"Não há dados disponíveis para a estação {escolha_estacao}.")
                continue

            df_estacao["Horario"] = pd.to_datetime(df_estacao["Horario"], format='%H:%M').dt.time

            print("\nOpções:")
            print("1. Ver o pico no horário atual")
            print("2. Escolher um horário específico")
            print("3. Ver gráfico de fluxo de passageiros")
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

            elif opcao == "3":
                # Converter para datetime completo e ordenar
                df_estacao["Horario_dt"] = pd.to_datetime(df_estacao["Horario"].astype(str), format='%H:%M:%S')
                df_estacao = df_estacao.sort_values(by="Horario_dt")

                # Plotar gráfico
                plt.figure(figsize=(10, 5))
                plt.plot(df_estacao["Horario_dt"], df_estacao["Passageiros"], marker='o', linestyle='-', color='blue')
                plt.title(f"Fluxo de Passageiros - Estação {escolha_estacao}")
                plt.xlabel("Horário")
                plt.ylabel("Número de Passageiros")
                plt.xticks(rotation=45)
                plt.grid(True)

                # Destacar o pico
                pico = df_estacao.loc[df_estacao["Passageiros"].idxmax()]
                plt.axvline(pico["Horario_dt"], color='red', linestyle='--', label='Horário de Pico')
                plt.legend()

                plt.tight_layout()
                plt.show()

            else:
                print("Opção inválida. Retornando ao menu.")
                continue

            input("\nPressione 'Enter' para voltar ao menu...")
            break

    except Exception as e:
        print(f"Ocorreu um erro ao prever o pico: {e}")