import os

def exibir_nome_do_programa():
    print("""𝗙𝘂𝘁𝘂𝗿𝗲 𝗦𝘁𝗮𝘁𝗶𝗼𝗻🚄""")

# def limpar tela
def limpar_tela():
    os.system('clear' if os.name == 'posix' else 'cls')


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