import time
import random
import os

# def limpar tela
def limpar_tela():
    os.system('cls')

# Banco de dados simulado
usuarios = {}
viagens = []
avisos = [
    "Linha 8 Diamante com atrasos de 10 minutos.",
    "Linha 9 Esmeralda operando normalmente.",
    "Linha 4 Amarela com grande fluxo de passageiros neste momento."
]

# Login/Cadastro
def cadastrar_usuario():
    print("\n===== Cadastro =====")
    usuario = input("Digite um nome de usuário: ")
    if usuario in usuarios:
        print("Usuário já cadastrado!")
        return None
    senha = input("Digite uma senha: ")
    usuarios[usuario] = senha
    print("Cadastro realizado com sucesso!")

# função de voltar ou sair
def voltar_sair():
    while True:
        escolha = input("\nDigite 'V' para voltar ou 'S' para sair.").strip().lower()
        if escolha == 'v':
            return
        elif escolha == 's':
            print("Saindo do sistema...")
            exit()
        else:
            print("Opção inválida. Tente novamente.")

def fazer_login():
    print("\n===== Login =====")
    usuario = input("Usuário: ")
    senha = input("Senha: ")
    if usuarios.get(usuario) == senha:
        print("Login realizado com sucesso!")
        return usuario
    print("Usuário ou senha incorretos!")
    return None

# Iniciar viagem
def iniciar_viagem(usuario):
    print("\n===== Iniciar Viagem =====")
    origem = input("Digite a estação de origem: ")
    destino = input("Digite a estação de destino: ")
    hora_partida = time.strftime("%H:%M")
    print("Viagem iniciada às", hora_partida)
    time.sleep(2)  # Simula o tempo de viagem
    hora_chegada = time.strftime("%H:%M")
    print("Viagem concluída às", hora_chegada)
    viagens.append({"usuario": usuario, "origem": origem, "destino": destino, "partida": hora_partida, "chegada": hora_chegada})

    voltar_sair()
    limpar_tela()

# Relatório de viagens
def exibir_relatorio(usuario):
    print("\n===== Relatório de Viagens =====")
    viagens_usuario = [v for v in viagens if v["usuario"] == usuario]
    if not viagens_usuario:
        print("Nenhuma viagem registrada.")
        return
    for i, v in enumerate(viagens_usuario, 1):
        print(f"Viagem {i}: {v['origem']} -> {v['destino']} | Partida: {v['partida']} | Chegada: {v['chegada']}")

    voltar_sair()
    limpar_tela()

# Previsão de pico
def previsao_pico():
    print("\n===== Previsão de Pico =====")
    horarios = [f"{h:02}:00" for h in range(6, 23)]
    fluxo = [random.randint(10, 300) for _ in horarios]
    pico = max(fluxo)
    horario_pico = horarios[fluxo.index(pico)]
    print(f"Horário de maior fluxo: {horario_pico} com {pico} passageiros.")

    voltar_sair()
    limpar_tela()

# Painel de avisos
def painel_de_avisos():
    print("\n===== Painel de Avisos =====")
    for aviso in avisos:
        print("-", aviso)

    voltar_sair()
    limpar_tela()

# Menu principal
def menu():
    usuario = None
    while True:
        print("\n===== Bem vindo ao sistema da Future Station =====")
        print("1. Cadastrar Usuário")
        print("2. Fazer Login")
        print("3. Iniciar Viagem")
        print("4. Relatório de Viagens")
        print("5. Previsão de Pico")
        print("6. Painel de Avisos")
        print("7. Sair")
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            cadastrar_usuario()
        elif opcao == '2':
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
            painel_de_avisos()
        elif opcao == '7':
            print("Saindo...")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    menu()