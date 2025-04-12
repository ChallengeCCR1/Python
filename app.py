from menu import menu_inicial, menu_principal
from operacoes_json import carregar_viagens_json
from usuario import carregar_usuarios


'''
1. Consumo de uma API externa pública;
2. Integraçração com banco de dados (inserir ok, atualizar (pendente), deletar (pendente), select (ok));
3. Realizar duas consultas no banco de dados (select, where) e ter a opção de exportar essas consultas
para arquivos.json;

---------

Restante é documentação.

'''

if __name__ == "__main__":
    carregar_viagens_json()
    carregar_usuarios()
    while True:
        usuario_logado = menu_inicial()
        menu_principal(usuario_logado)