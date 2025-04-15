from newsapi import NewsApiClient

newsapi = NewsApiClient(api_key='9307d8328c034c668a9f217b60cbe80b')

def obter_noticias_metro():
    try:
        artigos = newsapi.get_everything(
            q='metrô São Paulo',
            language='pt',
            sort_by='publishedAt',
            page_size=5
        )

        return artigos['articles']
    except Exception as e:
        print(f'Erro ao obter notícias: {e}')
        return []