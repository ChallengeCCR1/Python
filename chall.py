# Função para coletar os dados dos horários e número de pessoas
def coletar_dados():
    horarios = []
    pessoas_entraram = []
    
    # Pedir ao usuário para inserir os dados
    while True:
        horario = input("Digite o horário (formato HH:MM) ou 'sair' para terminar: ")
        if horario.lower() == 'sair':
            break
        try:
            pessoas = int(input(f"Quantas pessoas entraram às {horario}? "))
            horarios.append(horario)
            pessoas_entraram.append(pessoas)
        except ValueError:
            print("Por favor, insira um número válido de pessoas.")
    
    return horarios, pessoas_entraram

# Função para encontrar o horário de pico
def encontrar_pico(horarios, pessoas_entraram):
    maior_numero = max(pessoas_entraram)
    indice_do_pico = pessoas_entraram.index(maior_numero)
    horario_de_pico = horarios[indice_do_pico]
    
    return horario_de_pico, maior_numero

# Função para calcular a média de pessoas por horário
def calcular_media(pessoas_entraram):
    total_pessoas = sum(pessoas_entraram)
    media_pessoas = total_pessoas / len(pessoas_entraram)
    
    return media_pessoas

# Função para exibir os dados de maneira organizada
def exibir_resultados(horarios, pessoas_entraram, horario_de_pico, maior_numero, media_pessoas):
    print("\n=== Resultados ===")
    for i in range(len(horarios)):
        print(f"Às {horarios[i]}, {pessoas_entraram[i]} pessoas entraram.")
    
    print(f"\nO horário de pico foi {horario_de_pico}, com {maior_numero} pessoas.")
    print(f"A média de pessoas por horário foi {media_pessoas:.2f}.")

# Função para analisar o horário de pico
def funcionalidade_1():
    print("Você escolheu a análise de horários de pico!")
    horarios, pessoas_entraram = coletar_dados()
    if horarios:
        horario_de_pico, maior_numero = encontrar_pico(horarios, pessoas_entraram)
        media_pessoas = calcular_media(pessoas_entraram)
        exibir_resultados(horarios, pessoas_entraram, horario_de_pico, maior_numero, media_pessoas)
    else:
        print("Nenhum dado foi inserido.")

def voltar() :
        input("Pressione enter para voltar ao menu.")

# Função para exibir horários de funcionamento das linhas
def funcionalidade_2():
    print("Você escolheu a funcionalidade 2")

    while True : 
        print("\n-------Horário de funcionamento-------")
        print("\n1. Linha 4 Amarela")
        print("\n2. Linha 8 Diamante")
        print("\n3. Linha 9 Esmeralda")
        print("\n4. Voltar")

        opcao2 = input("Escolha sua opção: ")

        if opcao2 ==  '1' :
            print("Linha 4 Amarela funciona das 04h40 AM até as 00h.")
        elif opcao2 == '2' :
            print("Linha 8 diamante funciona das 04h00 AM até as 00h.") 
        elif opcao2 == '3' :
            print("Linha 9 Esmeralda funciona 04h00 AM até as 00h.")
        elif opcao2 == '4' :
            voltar ()
            break
        else :
            print("Opção inválida. Por favor escolha uma opção disponível.")

        input("Pressione enter para voltar ao menu principal.")

def voltar() :
        input("Pressione enter para voltar ao menu.")

# Função para exibir status das linhas
def funcionalidade_3():
    print("\nVocê escolheu a funcionalidade 3")

    while True : 
        print("\n-------Funcionamento-------")
        print("\n1. Linha 4 Amarela")
        print("\n2. Linha 8 Diamante")
        print("\n3. Linha 9 Esmeralda")
        print("\n4. Voltar")

        opcao2 = input("Escolha sua opção: ")

        if opcao2 ==  '1' :
            print("Linha 4 Amarela funcionando normalmente.")
        elif opcao2 == '2' :
            print("Linha 8 Diamante funcionando normalmente.") 
        elif opcao2 == '3' :
            print("Linha 9 Esmeralda funcionando normalmente.")
        elif opcao2 == '4' :
            voltar ()
            break
        else :
            print("Opção inválida. Por favor escolha uma opção disponível.")

        input("Pressione enter para voltar ao menu principal.")

def voltar() :
        input("Pressione enter para voltar ao menu.")

# Menu principal
def menu():
    while True:
        print("\n-------MENU PRINCIPAL-------")
        print("1. Analisar horários de pico")
        print("2. Ver horários de funcionamento das linhas")
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

    def sair() :
        print("Você escolheu sair.")