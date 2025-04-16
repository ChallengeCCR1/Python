from dados import avisos
from status_linhas import buscar_status_linhas_4_8_9

def centro_controle_operacional():
    while True:
        try:

            linhas = buscar_status_linhas_4_8_9()

            print("\n===== Centro de Controle Operacional =====")
            print("1. Linha 4 Amarela. ")
            print("2. Linha 8 Diamante. ")
            print("3. Linha 9 Esmeralda. ")
            print("4. Retornar ao menu principal. ")
            opcao = input("Escolha uma opção: ")

            if opcao in ["1", "2", "3"]:
                index = int(opcao) - 1
                if "erro" in linhas[index]:
                    print(linhas[index]["erro"])
                else:
                    print(f"\n🛤️ {linhas[index]['nome']}")
                    print(f"📍 Situação: {linhas[index]['situacao']}")
            elif opcao == "4":
                break
            else:
                print("Opção inválida. Por favor, tente novamente.")

            input("\nPressione 'Enter' para continuar...")
        except Exception as e:
            print(f"Erro no Centro de Controle: {e}")
