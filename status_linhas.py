import requests 

def buscar_status_linhas_4_8_9():
    try:
        url = 'https://www.diretodostrens.com.br/api/status'
        resposta = requests.get(url)

        if resposta.status_code != 200:
            raise Exception(f"Erro {resposta.status_code} ao acessar a API.")

        info = resposta.json()

        nomes_linhas = {
            "4": "Linha 4 Amarela",
            "8": "Linha 8 Diamante",
            "9": "Linha 9 Esmeralda"
        }

        resultados = []
        for linha in info:
            codigo = str(linha.get('codigo'))  # FORÇANDO PARA STRING
            if codigo in nomes_linhas:
                resultados.append({
                    "nome": nomes_linhas[codigo],
                    "status": linha.get("situacao", "Desconhecido")
                })

        if not resultados:
            raise Exception("Nenhuma das linhas desejadas foi encontrada.")

        return resultados

    except Exception as e:
        print(f"Erro ao buscar status das linhas: {e}")
        return []