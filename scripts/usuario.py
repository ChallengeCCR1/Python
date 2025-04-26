import getpass
import json
from conecction_oracle import inserir_usuario
from operacoes_json import salvar_usuarios_json
from dados import usuarios

def carregar_usuarios_json():
    try:
        with open('dados/usuarios.json', mode='r', encoding='utf-8') as arq:
            dados = json.load(arq)
            usuarios.clear()
            usuarios.update(dados)
    except FileNotFoundError:
        usuarios.clear()
    except Exception as e:
        print(f"Erro ao carregar usuários em JSON: {e}")
        usuarios.clear()

def cadastrar_usuario():
    """Cadastra um novo usuário."""
    try: 
        print("\n===== Cadastro =====")
        usuario = input("Digite um nome de usuário: ").strip().upper()
        
        # Verifica se o usuário já está cadastrado
        if usuario in usuarios:
            print("Usuário já cadastrado. Tente fazer login.")
            input("Pressione 'Enter' para continuar...")
            return False
        
        email = input("Digite seu e-mail: ").strip().lower()
        senha = getpass.getpass("Digite uma senha: ")
        
        # Chama a função para adicionar o usuário no dicionário
        usuarios[usuario] = {"email": email, "senha": senha}
        
        # Salva as alterações no arquivo
        salvar_usuarios_json()
        
        print("Cadastro realizado com sucesso! Você agora pode fazer login.")
        input("Pressione 'Enter' para continuar...")
    except Exception as e:
        print(f"Ocorreu um erro durante o cadastro: {e}")


def fazer_login():
    """Realiza o login de um usuário utilizando e-mail e senha."""
    try:
        # Carregar os usuários antes de tentar o login
        carregar_usuarios_json()

        print("\n===== Login =====")
        email_input = input("E-mail: ").strip().lower()  # Garantir que o e-mail esteja no formato correto
        senha_input = getpass.getpass("Senha: ")

        # Verificar se o usuário existe
        for usuario, dados in usuarios.items():
            if dados["email"] == email_input:
                if dados["senha"] == senha_input:
                    print(f"Login realizado com sucesso! Bem-vindo(a), {usuario.upper()}!")
                    input("Pressione 'Enter' para continuar...\n")
                    return usuario
                else:
                    print("Senha incorreta!")
                    input("Pressione 'Enter' para tentar novamente...\n")
                    return None
        
        # Se o e-mail não foi encontrado
        print("E-mail não encontrado!")
        input("Pressione 'Enter' para tentar novamente...\n")
    except Exception as e:
        print(f"Ocorreu um erro ao fazer login: {e}")

    return None