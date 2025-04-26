from dados import viagens, usuarios

import json

def salvar_viagens_json():
    global viagens
    try:
        with open('viagens.json', mode='w', encoding='utf-8') as arq:
            json.dump(viagens, arq, ensure_ascii=False, indent=4)
    except Exception as e:
        print(f"Ocorreu um erro ao salvar o arquivo: {e}")

def carregar_viagens_json():
    try:
        with open('viagens.json', mode='r', encoding='utf-8') as arq:
            dados_carregados = json.load(arq)
            viagens.clear()  # limpa a lista atual
            viagens.extend(dados_carregados)  # mantém a mesma referência
    except FileNotFoundError:
        viagens.clear()
    except Exception as e:
        print(f"Erro ao carregar viagem em JSON: {e}")
        viagens.clear()

def carregar_usuarios_json():
    try:
        with open('usuarios.json', mode='r', encoding='utf-8') as arq:
            dados = json.load(arq)
            usuarios.clear()
            usuarios.update(dados)
    except FileNotFoundError:
        usuarios.clear()
    except Exception as e:
        print(f"Erro ao carregar usuários em JSON: {e}")
        usuarios.clear()

def salvar_usuarios_json():
    try:
        with open('usuarios.json', mode='w', encoding='utf-8') as arq:
            json.dump(usuarios, arq, ensure_ascii=False, indent=4)
    except Exception as e:
        print(f"Ocorreu um erro ao salvar o arquivo: {e}")