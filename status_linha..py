import requests 

def buscar_status_linhas_4_8_9():
    try:
        url = 'https://www.diretodostrens.com.br/api/status'
        resp = requests.get(url)

        if resp.status_code == 200:
            todas_linhas = resp.json()
            linhas_desejadas = []

            for linha in todas_linhas:
                codigo = linha['codigo']
                if codigo in ['linha-4-amarela', 'linha-8-diamante', 'linha-9-esmeralda']:
                    linhas_desejadas.append({
                        "codigo": codigo,
                        "nome": linha['nome'],
                        "situacao": linha['situacao']
                    })
                
            return linhas_desejadas
        
        else:
            return [{"erro": f"Erro {resp.status_code} ao acessar a API."}]
    except Exception as e:
        return [{"erro": f"Erro ao buscar dados: {str(e)}"}]