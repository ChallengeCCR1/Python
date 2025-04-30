from menu import menu_inicial, menu_principal
from operacoes_json import carregar_viagens_json
from usuario import carregar_usuarios_json


'''
- Integraçração com banco de dados (inserir ok, atualizar (pendente), deletar (pendente), select (ok/50%));
   - Fazer select (exportar json) e opção de atualizar/deletar usuário -> banco de dados e python

- Documentação com códigos do banco de dados que devem ser usados para a aplicação rodar
---------

Restante é documentação.
'''

if __name__ == "__main__":
    viagens = []  # lista global
    carregar_viagens_json()
    carregar_usuarios_json()
    while True:
        usuario_logado = menu_inicial()
        menu_principal(usuario_logado)