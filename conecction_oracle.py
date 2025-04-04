import oracledb

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

    