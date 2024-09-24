def menu() :
    while True :
        print("\n-------MENU PRINCIPAL-------")
        print("\nFuncionalidade 1")
        print("\nFuncionalidade 2")
        print("\nFuncionalidade 3")

        opcao = input("Escolha a sua opção: ")

        if opcao == '1' :
            funcionalidade_1()
        elif opcao == '2' :
            funcionalidade_2()
        elif opcao == '3' :
            funcionalidade_3()
        elif opcao == '4' :
            print("Saindo...")
            break
        else :
            print("Opção inválida! Tente novamente!")  

def funcionalidade_1():
    print("\Você escolheu a funcionalidade 1")
    #Lógica da funcionalidade 1
    input("\nPressione enter para voltar ao menu principal.")

def  funcionalidade_2():
    print("Você escolheu a funcionalidade 2")
    #Lógica da funcionalidade 2
    input("\nPressione enter para voltar ao menu principal.")

def funcionalidade_3():
    print("\nVocê escolheu a funcionalidade 3")
    #Lógica da funcionalidade 3
    input("Pressione enter para voltar ao menu principal.")

#chamando a função menu para executar o menu principal
menu()
    