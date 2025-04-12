from menu import menu_inicial, menu_principal
from operacoes_json import carregar_viagens_json
from usuario import carregar_usuarios


'''
1. Consumo de uma API externa pública;
2. Integraçração com banco de dados (inserir ok, atualizar (pendente), deletar (pendente), select (ok));
3. Fazer virar uma API com flask para usar no Java e assim usar no front-end;

---------

Restante é documentação.

'''

if __name__ == "__main__":
    viagens = []  # lista global
    carregar_viagens_json()
    carregar_usuarios()
    while True:
        usuario_logado = menu_inicial()
        menu_principal(usuario_logado)