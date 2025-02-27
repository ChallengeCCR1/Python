import time
import random
import os

'''
1. melhorar menu -> se eu cadastrei um usuario, não tem porque aparecer para cadastrar de novo,
2. painel de avisos -> alguma forma de automatizar isso
'''

# def limpar tela
def limpar_tela():
    os.system('cls')

# Banco de dados simulado
usuarios = {}
viagens = []
avisos = [
    "Linha 4 Amarela com grande fluxo de passageiros neste momento.", #0
    "Linha 8 Diamante com atrasos de 10 minutos.", #1
    "Linha 9 Esmeralda operando normalmente."#2
]

# Login/Cadastro
def cadastrar_usuario():
    try: 
        print("\n===== Cadastro =====")
        usuario = input("Digite um nome de usuário: ")
        if usuario in usuarios:
            print("Usuário já cadastrado!")
            return None
        senha = input("Digite uma senha: ")
        usuarios[usuario] = senha
        print("Cadastro realizado com sucesso!")
    except Exception as e:
        print(f"Ocorreu um erro durante o cadastro: {e}")

    limpar_tela()

# função de voltar ou sair
def voltar_sair():
    try: 
        while True:
            escolha = input("\nDigite 'V' para voltar ou 'S' para sair: ").strip().lower()
            if escolha == 'v':
                return
            elif escolha == 's':
                print("Saindo do sistema...")
                exit()
            else:
                print("Opção inválida. Tente novamente.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

def fazer_login():
    try: 
        print("\n===== Login =====")
        usuario = input("Usuário: ")
        senha = input("Senha: ")
        if usuarios.get(usuario) == senha:
            print("Login realizado com sucesso!")
            return usuario
        print("Usuário ou senha incorretos!")
    except Exception as e:
        print(f"Ocorreu um erro ao fazer login: {e}")

        limpar_tela()
    return None
    
# Iniciar viagem
def iniciar_viagem(usuario):
    try:
        print("\n===== Iniciar Viagem =====")
        origem = input("Digite a estação de origem: ")
        destino = input("Digite a estação de destino: ")
        hora_partida = time.strftime("%H:%M")
        print(f"Viagem de {usuario} iniciada às {hora_partida}, para finalizar a viagem, pressione Enter.")

        input("Pressione Enter para encerrar a viagem.") # -> isso faz com que o sistema espere
                                                         # a decisão do usuario, ficando mais realista

        print("Finalizando a viagem...")
        time.sleep(3)  # simula o tempo de processamento

        hora_chegada = time.strftime("%H:%M")
        print(f"Viagem de {usuario} concluída às {hora_chegada}")

        viagens.append({
            "usuario": usuario, 
            "origem": origem, 
            "destino": destino, 
            "partida": hora_partida, 
            "chegada": hora_chegada
        })

        voltar_sair()
        limpar_tela()

    except Exception as e:
        print(f"Ocorreu um erro ao iniciar a viagem. {e}")

# Relatório de viagens
def exibir_relatorio(usuario):
    try:
        print(f"\n===== Relatório de Viagens de {usuario} =====")
        viagens_usuario = [v for v in viagens if v["usuario"] == usuario]
        if not viagens_usuario:
            print("Nenhuma viagem registrada.")
            return
        for i, v in enumerate(viagens_usuario, 1):
            print(f"Viagem {i}: {v['origem']} -> {v['destino']} | Partida: {v['partida']} | Chegada: {v['chegada']}")

        voltar_sair()
        limpar_tela()
    except Exception as e:
        print(f"Ocorreu um erro ao exibir o relatório: {e}")

# Previsão de pico
def previsao_pico():
    ## seria bacana o usuario definir qual a estação que ele quer saber o pico
    try:
        print("\n===== Previsão de Pico =====")
        escolha_estacao = input("Informe a estação que deseja saber o pico de passageiros: ")
        horarios = [f"{h:02}:00" for h in range(6, 23)]
        fluxo = [random.randint(10, 300) for _ in horarios]
        pico = max(fluxo)
        horario_pico = horarios[fluxo.index(pico)]
        print(f"Horário de maior fluxo: {horario_pico} na estação {escolha_estacao} com {pico} passageiros.")

        voltar_sair()
        limpar_tela()
    except Exception as e:
        print(f"Ocorreu um erro ao prever o pico: {e}")

def centro_controle_operacional():
    try:
        print("\n===== Centro de Controle Operacional =====")
        print("1. Linha 4 Amarela. ")
        print("2. Linha 8 Diamante. ")
        print("3. Linha 9 Esmeralda. ")
        opcao_linha = input("Escolha uma opção: ")

        if opcao_linha == "1":
            print(avisos[0])
        elif opcao_linha == "2":
            print(avisos[1])
        elif opcao_linha == "3":
            print(avisos[2])
        else:
            print("Opção inválida")

        voltar_sair()
        limpar_tela()
    except Exception as e:
        print(f"Erro ao exibir o painel de avisos: {e}")

# Menu principal
def menu():
    usuario = None
    while True:
        try:
            print(f"\nSeja bem vindo ao Sistema da Future Station, {usuario}!")

            if not usuarios:
                print("1. Cadastrar Usuário")
            if usuario is None:
                print("2. Fazer Login")
            print("3. Iniciar Viagem")
            print("4. Relatório de Viagens")
            print("5. Previsão de Pico")
            print("6. Centro de Controle Operacional")
            print("7. Sair")
            opcao = input("Escolha uma opção: ")
            
            if opcao == '1' and not usuarios:
                cadastrar_usuario()
            elif opcao == '2' and usuario is None:
                usuario = fazer_login()
            elif opcao == '3':
                if usuario:
                    iniciar_viagem(usuario)
                else:
                    print("Você precisa estar logado!")
            elif opcao == '4':
                if usuario:
                    exibir_relatorio(usuario)
                else:
                    print("Você precisa estar logado!")
            elif opcao == '5':
                previsao_pico()
            elif opcao == '6':
                centro_controle_operacional()
            elif opcao == '7':
                print("Saindo...")
                break
            else:
                print("Opção inválida!")
        except Exception as e:
            print(f"Ocorreu um erro inesperado no menu: {e}")

if __name__ == "__main__":
    menu()