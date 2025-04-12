def mapa_linha():
    try:
        print("\n===== Mapa =====")
        print("1. Linha 9 Esmeralda")
        print("2. Linha 4 Amarela (em breve)")
        print("3. Linha 8 Diamante (em breve)")
        print("4. Retornar ao menu principal")

        opcao = input("\nEscolha uma linha para ver o mapa: ")

        print("\n --------------------- ")

        if opcao == "1":
            exibir_mapa_linha9()
        elif opcao == "4":
            return
        else:
            print("\nEssa linha ainda não está disponível!")

            input("\nPressione 'Enter' para voltar ao menu das linhas.")
            mapa_linha()

    except Exception as e:
        print(f"Erro ao exibir as informações da linha: {e}")

def exibir_mapa_linha9():
    print("\n===== 🟩 Mapa da Linha 9 Esmeralda =====\n")

    # Lista de estações da Linha 9
    estacoes_linha9 = [
        "Osasco", "Presidente Altino", "Ceasa", "Villa Lobos", "Pinheiros", "Cidade Jardim",
        "Vila Olímpia", "Berrini", "Morumbi", "Granja Julieta", "João Dias", "Santo Amaro",
        "Socorro", "Jurubatuba", "Autódromo", "Interlagos", "Grajaú"
    ]

    # Destaques especiais
    destaques = {
        "Pinheiros": "⭐ Pinheiros",
        "Santo Amaro": "🚆 Santo Amaro"
    }

    # Dividindo a linha em blocos para melhor visualização
    blocos = [estacoes_linha9[i:i+5] for i in range(0, len(estacoes_linha9), 5)]

    for bloco in blocos:
        linha_formatada = "───".join([f"● {destaques.get(est, est)}" for est in bloco])
        print(linha_formatada)

    input("\n\nPressione 'Enter' para voltar ao menu das linhas.")
    mapa_linha()