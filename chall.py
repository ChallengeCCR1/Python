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

## funcionalidade 1
def funcionalidade_1():
    
    print("Você escolheu a funcionalidade 1")

    while True : 
        print("\n-------Linhas de metrô CCR-------")
        print("\n1. Linha 4 Amarela")
        print("\n2. Linha 8 Diamante")
        print("\n3. Linha 9 Esmeralda")
        print("\n4. Voltar")

        opcao2 = input("Escolha sua opção: ")

        if opcao2 ==  '1' :
            print("Linha 4 Amarela.")
        elif opcao2 == '2' :
            print("Linha 8 Diamante.") 
        elif opcao2 == '3' :
            print("Linha 9 Esmeralda.")
        elif opcao2 == '4' :
            voltar ()
            break
        else :
            print("Opção inválida. Por favor escolha uma opção disponível.")

        input("\nPressione enter para voltar ao menu principal.")

## funcionalidade 2
def  funcionalidade_2():
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


## funcionalidade 3
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

def sair() :
    print("Você escolheu sair.")
    
#chamando a função menu para executar o menu principal
if __name__ == "__main__":
    menu()
    