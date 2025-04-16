from dados import avisos
from status_linhas import buscar_status_linhas_4_8_9

def centro_controle_operacional():
    while True:
        try:
            print("\n===== Centro de Controle Operacional =====")
            print("1. Linha 4 Amarela")
            print("2. Linha 8 Diamante")
            print("3. Linha 9 Esmeralda")
            print("4. Retornar ao menu principal")
            opcao_linha = input("Escolha uma opção: ")

            status_linhas = buscar_status_linhas_4_8_9()
            codigos = {"1": "Linha 4 Amarela", "2": "Linha 8 Diamante", "3": "Linha 9 Esmeralda"}

            if opcao_linha in codigos:
                nome_escolhido = codigos[opcao_linha]
                linha_info = next((linha for linha in status_linhas if linha["nome"] == nome_escolhido), None)

                if linha_info:
                    print(f"\n📢 {linha_info['nome']} - {linha_info['status']}")
                else:
                    print(f"\n⚠️ Status da {nome_escolhido} não encontrado.")
            elif opcao_linha == "4":
                break
            else:
                print("Opção inválida.")

            input("\nPressione 'Enter' para continuar...")

        except Exception as e:
            print(f"Erro no Centro de Controle: {e}")