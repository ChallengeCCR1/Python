import getpass
import json
from conecction_oracle import inserir_usuario
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
    """Cadastra um novo usuário no banco de dados."""
    try: 
        print("\n===== Cadastro =====")
        usuario = input("Digite um nome de usuário: ").strip().upper()
        email = input("Digite seu e-mail: ").strip().lower()
        senha = getpass.getpass("Digite uma senha: ")
        
        # Chama a função que insere no banco
        inserir_usuario(usuario, email, senha)
        
        input("Pressione 'Enter' para continuar...")

    except Exception as e:
        print(f"Ocorreu um erro durante o cadastro: {e}")

import oracledb
import getpass
from conecction_oracle import obter_conexao 

import getpass

def fazer_login():
    """Realiza o login de um usuário utilizando o banco de dados."""
    try:
        print("\n===== Login =====")
        email_input = input("E-mail: ").strip().lower()
        senha_input = getpass.getpass("Senha: ")

        conexao = obter_conexao()
        if conexao is None:
            print("Erro ao conectar ao banco de dados.")
            return None

        try:
            with conexao.cursor() as cursor:
                cursor.execute("""
                    SELECT nome, senha FROM Usuario_Challenge WHERE LOWER(email) = :1
                """, [email_input])
                resultado = cursor.fetchone()

                if resultado:
                    nome_banco, senha_banco = resultado
                    if senha_input == senha_banco:
                        print(f"Login realizado com sucesso! Bem-vindo(a), {nome_banco.upper()}!")
                        input("Pressione 'Enter' para continuar...\n")
                        return nome_banco
                    else:
                        print("Senha incorreta!")
                        input("Pressione 'Enter' para tentar novamente...\n")
                        return None
                else:
                    print("E-mail não encontrado!")
                    input("Pressione 'Enter' para tentar novamente...\n")
                    return None
        finally:
            conexao.close()

    except Exception as e:
        print(f"Ocorreu um erro ao fazer login: {e}")
        return None