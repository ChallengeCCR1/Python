from operacoes_json import avisos

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