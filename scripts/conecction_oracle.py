import oracledb
import json

def obter_conexao():
    try:
        con = oracledb.connect(
            user="rm561178",
            password="200905",
            dsn="oracle.fiap.com.br/orcl"
        )

        return con
    except oracledb.DatabaseError as e:
        erro, = e.args
        print(f"Erro ao conectar com o banco de dados: {erro.code} - {erro.message}")
        return None

## exportação de consulta para json
def exportar_estacoes_para_json():
    nome_linha = input("Digite o nome da linha (ex: Linha 9): ")

    conexao = obter_conexao()
    if conexao is None:
        print("Falha ao obter conexão com banco de dados.")
        return

    try:
        with conexao.cursor() as cursor:
            
            cursor.execute("SELECT id_linhametro FROM LinhaMetro WHERE LOWER(nome) = :1", [nome_linha.lower()])
            resultado = cursor.fetchone()
            
            if resultado is None:
                print("Linha não encontrada.")
                return
            
            id_linha = resultado[0]

            
            cursor.execute("""
                SELECT nome, localizacao FROM Estacao
                WHERE id_linhametro = :1
                """, [id_linha])

            estacoes = cursor.fetchall()
            if not estacoes:
                print("Nenhuma estação encontrada para essa linha.")
                return

            estacoes_json = [{"nome": nome, "localizacao": local} for nome, local in estacoes]
            nome_arquivo = nome_linha.replace(" ", "_").lower() + "_estacoes.json"

            with open(f'dados/{nome_arquivo}', "w", encoding="utf-8") as arquivo:
                json.dump(estacoes_json, arquivo, indent=4, ensure_ascii=False)

            print(f"Estações da {nome_linha} exportadas com sucesso para {nome_arquivo}!\n")

    except Exception as e:
        print(f"Erro durante exportação: {e}")
    finally:
        conexao.close()

## insert de usuários no banco
def inserir_usuario(usuario, email, senha):
    conexao = obter_conexao()
    if conexao is None:
        print("Falha ao obter conexão com banco de dados.")
        return
    
    try:
        with conexao.cursor() as cursor:
            email = email.lower()  
            
            # Verifica se o e-mail já existe
            cursor.execute("SELECT COUNT(*) FROM Usuario_Challenge WHERE LOWER(email) = :1", [email])
            resultado = cursor.fetchone()
            
            if resultado[0] > 0:
                print("Erro: o e-mail fornecido já está cadastrado.")
                return
            
            # Insere o usuário no banco
            sql = """
                INSERT INTO Usuario_Challenge (id_usuario, nome, email, senha)
                VALUES (gerador_id_chall.NEXTVAL, :1, :2, :3)
            """
            cursor.execute(sql, [usuario, email, senha])
            conexao.commit()

    except oracledb.IntegrityError as e:
        print(f"Erro de integridade: {e}")
    except oracledb.DatabaseError as e:
        print(f"Erro ao inserir usuário: {e}")
    finally:
        if conexao:
            conexao.close()

def excluir_usuario(usuario, email):
    conexao = obter_conexao()
    if conexao is None:
        print("Falha ao obter conexão com banco de dados.")
        return
    
    try:
        with conexao.cursor() as cursor:
            email = email.lower()

            cursor.execute("SELECT COUNT(*) FROM Usuario_Challenge WHERE LOWER(email) = :1 AND nome = :2", [email, usuario])
            resultado = cursor.fetchone()

            if resultado[0] == 0:
                print("Usuário não encontrado. Nenhum registro foi excluído.")
                return
            
            cursor.execute("DELETE FROM Usuario_Challenge WHERE LOWER(email) = :1 AND nome = :2", [email, usuario])
            conexao.commit()
            print("Usuário excluído com sucesso.")
    except oracledb.DatabaseError as e:
        print(f"Erro ao excluir usuário: {e}")
    finally:
        if conexao:
            conexao.close()
