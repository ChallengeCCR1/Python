import random
import os

# Função para coletar os dados dos horários e número de pessoas
def coletar_dados():
    """
    Coleta horários e números de pessoas que entraram nesses horários.
    Permite entrada manual ou aleatória.
    """
    horarios = []
    pessoas_entraram = []
    
    print("\nVocê quer inserir os dados manualmente ou gerar automaticamente?")
    print("1. Inserir manualmente")
    print("2. Gerar automaticamente")
    
    opcao = input("Escolha sua opção (1-2): ")
    if opcao == '2':
        horarios, pessoas_entraram = gerar_dados_aleatorios()
        print("\nDados gerados automaticamente com sucesso!")
    else:
        while True:
            horario = input("Digite o horário (formato HH:MM) ou 'sair' para terminar: ")
            if horario.lower() == 'sair':
                break
            if not validar_horario(horario):
                print("Formato de horário inválido. Por favor, use HH:MM.")
                continue
            try:
                pessoas = int(input(f"Quantas pessoas entraram às {horario}? "))
                horarios.append(horario)
                pessoas_entraram.append(pessoas)
            except ValueError:
                print("Por favor, insira um número válido de pessoas.")
    
    return horarios, pessoas_entraram

# Função para validar o formato do horário
def validar_horario(horario):
    """
    Valida se o horário está no formato HH:MM e é válido.
    """
    if len(horario) != 5 or horario[2] != ':':
        return False
    partes = horario.split(':')
    try:
        horas = int(partes[0])
        minutos = int(partes[1])
        return 0 <= horas < 24 and 0 <= minutos < 60
    except ValueError:
        return False

# Função para encontrar o horário de pico
def encontrar_pico(horarios, pessoas_entraram):
    """
    Encontra o horário com o maior número de pessoas.
    """
    maior_numero = max(pessoas_entraram)
    indice_do_pico = pessoas_entraram.index(maior_numero)
    horario_de_pico = horarios[indice_do_pico]
    return horario_de_pico, maior_numero

# Função para calcular a média de pessoas por horário
def calcular_media(pessoas_entraram):
    """
    Calcula a média de pessoas por horário.
    """
    total_pessoas = sum(pessoas_entraram)
    return total_pessoas / len(pessoas_entraram) if pessoas_entraram else 0

# Função para exibir os dados de maneira organizada
def exibir_resultados(horarios, pessoas_entraram, horario_de_pico, maior_numero, media_pessoas):
    """
    Exibe os resultados calculados de maneira organizada.
    """
    print("\n=== Resultados ===")
    print("\nHorários e pessoas:")
    for i in range(len(horarios)):
        print(f" - Às {horarios[i]}, {pessoas_entraram[i]} pessoas.")
    
    print(f"\nO horário de pico foi {horario_de_pico}, com {maior_numero} pessoas.")
    print(f"A média de pessoas por horário foi {media_pessoas:.2f}.")

# Função para gerar dados aleatórios (opcional)
def gerar_dados_aleatorios():
    """
    Gera horários e números de pessoas aleatórios para teste.
    """
    horarios = [f"{h:02}:{m:02}" for h in range(6, 23) for m in [0, 30]]
    pessoas_entraram = [random.randint(0, 100) for _ in horarios]
    return horarios, pessoas_entraram

# Função para analisar o horário de pico
def funcionalidade_1():
    """
    Funcionalidade para analisar horários de pico.
    """
    print("\nVocê escolheu a análise de horários de pico!")
    horarios, pessoas_entraram = coletar_dados()
    
    if not horarios:
        print("Nenhum dado foi inserido!")
        return

    horario_de_pico, maior_numero = encontrar_pico(horarios, pessoas_entraram)
    media_pessoas = calcular_media(pessoas_entraram)
    exibir_resultados(horarios, pessoas_entraram, horario_de_pico, maior_numero, media_pessoas)

def voltar():
    """
    Função para pausar e voltar ao menu.
    """
    input("\nPressione enter para voltar ao menu.")

def funcionalidade_2():
    """
    Funcionalidade para comparar horários de funcionamento de linhas.
    """
    print("\n\nEscolha duas linhas para comparar:")
    linhas = {
        '1': ("Linha 4 Amarela", "04h40 até 00h"),
        '2': ("Linha 8 Diamante", "04h00 até 00h"),
        '3': ("Linha 9 Esmeralda", "04h00 até 00h"),
    }
    
    for chave, valor in linhas.items():
        print(f"{chave}. {valor[0]}")
    
    escolha1 = input("Escolha a primeira linha: ")
    escolha2 = input("Escolha a segunda linha: ")

    if escolha1 == escolha2 or escolha1 not in linhas or escolha2 not in linhas:
        print("Escolha inválida. Certifique-se de escolher duas linhas diferentes.")
        return
    
    print("\nComparativo de Linhas:")
    print("| Linha               | Horário de Funcionamento     |")
    print("|---------------------|------------------------------|")
    
    for escolha in [escolha1, escolha2]:
        linha_info = linhas[escolha]
        print(f"| {linha_info[0]} | {linha_info[1]}")
    
    voltar()

# Função para exibir status das linhas
def funcionalidade_3():
    """
    Funcionalidade para mostrar o status de funcionamento das linhas.
    """
    print("\nVocê escolheu ver o status de funcionamento das linhas.")
    
    while True: 
        print("\n------- Status de Funcionamento -------")
        print("1. Linha 4 Amarela")
        print("2. Linha 8 Diamante")
        print("3. Linha 9 Esmeralda")
        print("4. Voltar")

        opcao = input("Escolha sua opção (1-4): ")

        if opcao == '1':
            print("Linha 4 Amarela está funcionando normalmente.")
        elif opcao == '2':
            print("Linha 8 Diamante está com atrasos de 5 minutos.")
        elif opcao == '3':
            print("Linha 9 Esmeralda está com interrupção no trilho.")
        elif opcao == '4':
            voltar()
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção disponível.")
        
        voltar()

# Menu principal
def menu():
    """
    Menu principal do programa.
    """
    while True:
        print("\n-------MENU PRINCIPAL-------")
        print("1. Analisar horários de pico")
        print("2. Comparar duas linhas")
        print("3. Ver status de funcionamento das linhas")
        print("4. Sair")
        
        opcao = input("Escolha sua opção: ")
        
        if opcao == '1':
            funcionalidade_1()
        elif opcao == '2':
            funcionalidade_2()
        elif opcao == '3':
            funcionalidade_3()
        elif opcao == '4':
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida! Tente novamente.")

# Executar o programa
if __name__ == "__main__":
    menu()
    os.system('clear')