# menu de cadastro/login
import getpass
from cco import centro_controle_operacional
from conecction_oracle import atualizar_usuario, excluir_usuario, exportar_estacoes_para_json
from funcoes import exibir_nome_do_programa
from mapa import mapa_linha
from operacoes_json import carregar_viagens_json
from previsao_pico import previsao_pico_menu
from relatorio import exibir_relatorio
from usuario import cadastrar_usuario, fazer_login
from viagem import iniciar_viagem


def menu_inicial():
    usuario = None
    while usuario is None:
        try:
            print(f"\nSeja bem-vindo ao Sistema da Future Station!")
            print("1. Cadastro")
            print("2. Login")
            print("3. Sair")

            opcao = input("Escolha uma opção: ").strip()
        
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

    return usuario

## menu após login
def menu_principal(usuario):
    while True:
        try:
            carregar_viagens_json()
            exibir_nome_do_programa()
            
            print(f"\nBem vindo, {usuario}!")
            print("1. Mapa")
            print("2. Iniciar viagem")
            print("3. Relatório de viagens")
            print("4. Status Operacional")
            print("5. Previsão de pico")
            print("6. Exportar estações para JSON")
            print("7. Excluir usuário")
            print("8. Atualizar usuário")
            print("9. logout")

            opcao = input("Escolha uma opção: ").strip()

            if opcao == '1':
                mapa_linha()
            elif opcao == '2':
                iniciar_viagem(usuario)
            elif opcao == '3':
                exibir_relatorio(usuario)
            elif opcao == '4':
                centro_controle_operacional()
            elif opcao == '5':
                previsao_pico_menu()
            elif opcao == '6':
                exportar_estacoes_para_json()
            elif opcao == '7':
                print("\n==== Remover usuário ====")
                nome = input("Nome do usário a excluir: ")
                email = input("E-mail do usuário: ")
                excluir_usuario(nome, email)
            elif opcao == '8':
                print("\n==== Atualizar usuário ====")
                nome_atual = input("Nome atual: ")
                email_atual = input("E-mail atual: ")
                novo_nome = input("Novo nome: ")
                novo_email = input("Novo e-mail: ")
                nova_senha = getpass.getpass("Nova senha: ")
                atualizar_usuario(nome_atual, email_atual, novo_nome, novo_email, nova_senha)    
            elif opcao == '9':
                print(f"Poxa, {usuario}! Parece que escolheu sair...")
                return
            else:
                print("Opção inválida!")

        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")