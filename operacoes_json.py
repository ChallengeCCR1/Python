import json

usuarios = {}
avisos = [
    "Linha 4 Amarela com grande fluxo de passageiros neste momento.", #0
    "Linha 8 Diamante com atrasos de 10 minutos.", #1
    "Linha 9 Esmeralda operando normalmente."#2
]

viagens = []

def salvar_viagens_json():
    try:
        with open('viagens.json', mode='w', encoding='utf-8') as arq:
            json.dump(viagens, arq, ensure_ascii=False, indent=4)
    except Exception as e:
        print(f"Ocorreu um erro ao salvar o arquivo: {e}")

def carregar_viagens_json():
    global viagens
    try:
        with open('viagens.json', mode='r', encoding='utf-8') as arq:
            viagens = json.load(arq)
    except FileNotFoundError:
        viagens = []
    except Exception as e:
        print(f"Erro ao carregar viagem em JSON: {e}")
        viagens = []

## def salvar_usuarios_json
def salvar_usuarios_json():
    """Salva os usuários no arquivo JSON."""
    try:
        with open('usuarios.json', mode='w', encoding='utf-8') as arq:
            json.dump(usuarios, arq, ensure_ascii=False, indent=4)
    except Exception as e:
        print(f"Ocorreu um erro ao salvar o arquivo: {e}")