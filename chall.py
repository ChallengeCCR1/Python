def menu() :
    while True :
        print("\n-------MENU PRINCIPAL-------")
        print("\n1. Funcionalidade 1")
        print("\n2. Funcionalidade 2")
        print("\n3. Funcionalidade 3")
        print("\n4. Sair")

        opcao = input("Escolha a sua opção: ")

        if opcao == '1' :
            funcionalidade_1()
        elif opcao == '2' :
            funcionalidade_2()
        elif opcao == '3' :
            funcionalidade_3()
        elif opcao == '4' :
            sair()
            break
        else :
            print("Opção inválida! Tente novamente!")  

def funcionalidade_1():
    print("Você escolheu a funcionalidade 1")
    #Lógica da funcionalidade 1

    input("\nPressione enter para voltar ao menu principal.")

def  funcionalidade_2():
    print("Você escolheu a funcionalidade 2")
    #Lógica da funcionalidade 2
    input("\nPressione enter para voltar ao menu principal.")

def funcionalidade_3():

    print("\nVocê escolheu a funcionalidade 3")

    while True : 
        print("\n-------Linhas de metrô-------")
        print("\n1. Linha 4 amarela")
        print("\n2. Linha 8 Diamente")
        print("\n3. Linha 9 Esmeralda")
        print("\n4. Voltar")

        opcao2 = input("Escolha sua opção: ")

        if opcao2 ==  '1' :
            print("Linha 4 amarela funcionando normalmente.")
        elif opcao2 == '2' :
            print("Linha 8 diamente funcionando normalmente.") 
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

def sair() :
    print("Você escolheu sair.")
    
#chamando a função menu para executar o menu principal
menu()
    