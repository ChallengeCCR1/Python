import time
import random
import os
import json
import matplotlib.pyplot as plt

'''
O que devedemos focar para a próxima sprint é:
1. Integração com banco de dados;
2. Deixar o sistema extremamente parecido com o banco de dados;
3. Integrar com o front
'''

# def limpar tela
def limpar_tela():
    os.system('clear' if os.name == 'posix' else 'cls')

# Banco de dados simulado
usuarios = {}
viagens = []
avisos = [
    "Linha 4 Amarela com grande fluxo de passageiros neste momento.", #0
    "Linha 8 Diamante com atrasos de 10 minutos.", #1
    "Linha 9 Esmeralda operando normalmente."#2
]

## def de salvar arquivos no json
def salvar_viagens_json():
    try:
        with open('viagens.json', mode='w', encoding='utf-8') as arq:
            json.dump(viagens, arq, ensure_ascii=False, indent=4)
    except Exception as e:
        print(f"Ocorreu um erro ao salvar o arquivo: {e}")

## def para carregar as viagens do json
def carregar_viagens_json():
    global viagens
    try:
        with open('viagens.json', mode='r', encoding='utf-8') as arq:
            viagens = json.load(arq)
    except FileNotFoundError:
        viagens = []
    except Exception as e:
        print(f"Erro ao carregar viagem em JSON: {e}")
        viagens = []

## def salvar_usuarios_json
def salvar_usuarios_json():
    try:
        with open('usuarios.json', mode='w', encoding='utf-8') as arq:
            json.dump(usuarios, arq, ensure_ascii=False, indent=4)
    except Exception as e:
        print(f"Ocorreu um erro ao salvar o arquivo: {e}")

## def para carregar os usuarios
def carregar_usuarios():
    global usuarios
    try:
        with open('usuarios.json', mode='r', encoding='utf-8') as arq:
            usuarios = json.load(arq)
    except FileNotFoundError:
        usuarios = {}
    except Exception as e:
        print(f"Ocorreu um erro ao carregar o arquivo:{e}")
        usuarios = {}

# Login/Cadastro
def cadastrar_usuario():
    try: 
        print("\n===== Cadastro =====")
        usuario = input("Digite um nome de usuário: ")
        if usuario in usuarios:
            print("Usuário já cadastrado. Tente fazer login.")
            return False
        senha = input("Digite uma senha: ")

        usuarios[usuario] = senha
        salvar_usuarios_json()
        print("Cadastro realizado com sucesso! Você agora pode fazer login.")
        input("Pressione 'Enter' para continuar...")
        limpar_tela()
        return True
    except Exception as e:
        print(f"Ocorreu um erro durante o cadastro: {e}")

        limpar_tela()

## função de fazer login na plataforma
def fazer_login():
    try: 
        print("\n===== Login =====")
        usuario = input("Usuário: ")
        senha = input("Senha: ")
        if usuarios.get(usuario) == senha:
            print("Login realizado com sucesso! Aproveite a nossa plataforma!")
            input("Pressione 'Enter' para continuar...")
            limpar_tela()
            return usuario
        print("Usuário ou senha incorretos!")
        input("Pressione 'Enter' para tentar novamente..." )
    except Exception as e:
        print(f"Ocorreu um erro ao fazer login: {e}")
        limpar_tela()
    return None

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

# tempo de viagem entre estações linha 9 esmeralda
tempos_viagem = {
    ("Osasco", "Presidente Altino") : 5,
    ("Presidente Altino", "Ceasa") : 5,
    ("Ceasa", "Vila Lobos") : 5,
    ("Vila Lobos", "Pinheiros") : 5,
    ("Pinheiros", "Cidade Jardim") : 5,
    ("Cidade Jardim", "Vila Olimpia") : 5,
    ("Vila Olimpia", "Berrini") : 5,
    ("Berrini", "Morumbi") : 5,
    ("Morumbi", "Granja Julieta") : 5,
    ("Granja Julieta", "João Dias") : 5,
    ("João Dias", "Santo Amaro") : 5,
    ("Santo Amaro", "Socorro") : 5,
    ("Socorro", "Jurubatuba") : 5,
    ("Jurubatuba", "Autódromo") : 5,
    ("Autódromo", "Interlargos") : 5,
    ("Interlargos", "Grajaú") : 5,
}

dados_estacao = {
    "08:00": 150,
    "09:00": 300,
    "10:00": 500,
    "11:00": 400,
    "12:00": 100,
    "13:00": 200,
    "17:00": 500,
    "18:00": 900
}
    
def encontrar_horario_proximo(hora_partida):
    """Encontra o horário mais próximo da hora_partida dentro dos horários disponíveis no dicionário."""
    horarios_disponiveis = list(dados_estacao.keys())
    horarios_disponiveis.sort()  # Garantir que os horários estão em ordem
    for horario in reversed(horarios_disponiveis):
        if hora_partida >= horario:
            return horario
    return horarios_disponiveis[0]

def iniciar_viagem(usuario):
    try:
        print("\n===== Iniciar Viagem =====")
        origem = input("Digite a estação de origem: ")
        destino = input("Digite a estação de destino: ")

        # Obter o horário atual e encontrar o horário mais próximo disponível
        hora_partida = time.strftime("%H:%M")
        horario_proximo = encontrar_horario_proximo(hora_partida)

        print(f"Viagem de {usuario} iniciada às {hora_partida} (Referência: {horario_proximo})")

        # Verificar se há dados de fluxo de pessoas no horário mais próximo
        if horario_proximo in dados_estacao:
            pessoas = dados_estacao[horario_proximo]

            # Gerar o gráfico
            horarios = list(dados_estacao.keys())
            quantidade_pessoas = list(dados_estacao.values())

            plt.bar(horarios, quantidade_pessoas, color='blue')
            plt.xlabel('Horários')
            plt.ylabel('Quantidade de Pessoas')
            plt.title(f'Fluxo de Pessoas na Estação {origem} - Horário: {horario_proximo}')
            plt.show()

            # Alerta gráfico
            if pessoas > 400:
                print(f"⚠️ Alerta! A estação {origem} está muito cheia nesse horário.")
            elif pessoas > 200:
                print(f"⚠️ Atenção! A estação {origem} está cheia nesse horário.")
            else:
                print(f"✅ A estação {origem} não está muito cheia nesse horário.")
        else:
            print(f"ℹ️ Não temos dados para a estação {origem} nesse horário.")

        input("Pressione Enter para encerrar a viagem.")
        print("Finalizando a viagem...")
        time.sleep(3)  

        hora_chegada = time.strftime("%H:%M")
        print(f"Viagem de {usuario} concluída às {hora_chegada}, de {origem} para {destino}")

        # Adicionando a viagem antes de salvar
        viagem = {
            "usuario": usuario,
            "origem": origem,
            "destino": destino,
            "partida": hora_partida,
            "chegada": hora_chegada
        }
        viagens.append(viagem)
        salvar_viagens_json()

    except Exception as e:
        print(f"Erro ao iniciar a viagem: {e}")

    limpar_tela()

# Relatório de viagens
def exibir_relatorio(usuario):
    try:
        print(f"\n===== Relatório de Viagens de {usuario} =====")
        
        # Verifica se a lista de viagens foi corretamente registrada
        if not viagens:
            print("Nenhuma viagem registrada até o momento.")
            input("\nPressione Enter para voltar ao menu...")  # Pausa para o usuário ler
            voltar_sair()  # Voltar ao menu
            return

        viagens_usuario = [v for v in viagens if v["usuario"] == usuario]
        
        if not viagens_usuario:
            print("Nenhuma viagem registrada para este usuário.")
            input("\nPressione Enter para voltar ao menu...")  # Pausa para o usuário ler
        else:
            for i, v in enumerate(viagens_usuario, 1):
                print(f"\n🚆 Viagem {i}")
                print(f"   📍 Origem: {v['origem']}")
                print(f"   🎯 Destino: {v['destino']}")
                print(f"   ⏳ Partida: {v['partida']} | 🏁 Chegada: {v['chegada']}")

        input("\nPressione Enter para voltar ao menu...")  # Adiciona pausa antes de sair
        limpar_tela()  # Garante que o usuário possa escolher voltar ou sair antes de limpar a tela

    except Exception as e:
        print(f"❌ Erro ao exibir o relatório: {e}")

# Previsão de pico
def previsao_pico():
    try:
        print("\n===== Previsão de Pico =====")
        
        # Dicionário de estações da CCR
        ccr_estacoes = {
            "Linha 4 Amarela": ["Butantã", "Pinheiros", "Faria Lima", "Paulista", "Consolação", "República", "Luz"],
            "Linha 8 Diamante": ["Osasco", "Presidente Altino", "Ceasa", "Villa Lobos", "Pinheiros", "Cidade Jardim", "Vila Olímpia"],
            "Linha 9 Esmeralda": ["Osasco", "Presidente Altino", "Ceasa", "Villa Lobos", "Pinheiros", "Cidade Jardim", 
                                  "Vila Olímpia", "Berrini", "Morumbi", "Granja Julieta", "João Dias", "Santo Amaro", 
                                  "Socorro", "Jurubatuba", "Autódromo", "Interlagos", "Grajaú"]
        }

        while True:
            # Recebe a estação
            escolha_estacao = input("Informe a estação que deseja saber o pico de passageiros: ")

            # Verifica se a estação pertence a alguma linha da CCR
            estacao_encontrada = False
            for linha, estacoes in ccr_estacoes.items():
                if escolha_estacao in estacoes:
                    estacao_encontrada = True
                    break

            if not estacao_encontrada:
                print(f"A estação {escolha_estacao} não pertence a uma linha da CCR. Tente novamente.")
                continue  # Retorna ao início da loop para tentar novamente

            # Simulação de horários e fluxo
            horarios = [f"{h:02}:00" for h in range(4, 23)]  # das 04:00 às 23:00
            fluxo = [random.randint(300, 900) for i in horarios]  # número aleatório de passageiros
            
            pico = max(fluxo)
            horario_pico = horarios[fluxo.index(pico)]

            # Exibe o horário de pico e o fluxo
            print(f"Horário de maior fluxo: {horario_pico} na estação {escolha_estacao} com {pico} passageiros.")
            print("\nFluxo de passageiros por horário:")
            for h, f in zip(horarios, fluxo):
                print(f"{h}: {f} passageiros")

            voltar_sair()
            limpar_tela()
            break  # Sai do loop após mostrar a previsão de pico
    
    except Exception as e:
        print(f"Ocorreu um erro ao prever o pico: {e}")


def mapa_linha():
    try:
        print("\n===== Informações das Linhas =====")
        print("1. Linha 9 Esmeralda")
        print("2. Linha 4 Amarela (em breve)")
        print("3. Linha 8 Diamante (em breve)")

        opcao = input("Escolha uma linha para ver detalhes: ")

        if opcao == "1":
            exibir_mapa_linha9()
        else:
            print("Essa linha ainda não está disponível!")

            voltar_sair()
    except Exception as e:
        print(f"Erro ao exibir as informações da linha: {e}")

def exibir_mapa_linha9():
    print("\n===== Mapa da Linha 9 Esmeralda =====")

    # Definindo as estações em uma matriz
    estacoes_matriz = [
        ["Osasco", "Presidente Altino", "Ceasa"],  # Primeira parte da linha
        ["Villa Lobos", "Pinheiros", "Cidade Jardim"],  # Segunda parte da linha
        ["Vila Olímpia", "Berrini", "Morumbi"],  # Terceira parte da linha
        ["Granja Julieta", "João Dias", "Santo Amaro"],  # Quarta parte da linha
        ["Socorro", "Jurubatuba", "Autódromo", "Interlagos", "Grajaú"]  # Última parte da linha
    ]

    # Imprimindo a matriz de estações de forma legível
    for trecho in estacoes_matriz:
        print(" -> ".join(trecho))

    voltar_sair()

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

# menu de cadastro/login
def menu_inicial():
    usuario = None
    while usuario is None:
        try:
            print(f"\nSeja bem-vindo ao Sistema da Future Station!")
            print("1. Cadastrar Usuário")
            print("2. Fazer Login")
            print("3. Sair")

            opcao = input("Escolha uma opção: ")
        
            if opcao == '1':
                cadastrar_usuario()
            elif opcao == '2':
                usuario = fazer_login()
            elif opcao == '3':
                print("Saindo...")
                exit()
            else:
                print("Opção inválida!")
            
        except Exception as e:
            print(f"Ocorreu um erro inesperado no menu: {e}")

        limpar_tela()

    return usuario

## menu após login
def menu_principal(usuario):
    while True:
        try:
            print(f"Bem vindo, {usuario}!")
            print("1. Informações da linha")
            print("2. Iniciar viagem")
            print("3. Previsão de pico")
            print("4. Painel de avisos")
            print("5. Relatório de viagens")
            print("6. logout")

            opcao = input("Escolha uma opção: ")

            if opcao == '1':
                mapa_linha()
            elif opcao == '2':
                iniciar_viagem(usuario)
            elif opcao == '3':
                previsao_pico()
            elif opcao == '4':
                centro_controle_operacional()
            elif opcao == '5':
                exibir_relatorio(usuario)
            elif opcao == '6':
                print(f"Poxa, {usuario}! Parece que escolheu sair...")
                return
            else:
                print("Opção inválida!")

        except Exception as e:
            print(f"Ocorreu um erro iniesperado: {e}")

        limpar_tela()

if __name__ == "__main__":
    carregar_viagens_json()
    carregar_usuarios()
    while True:
        usuario_logado = menu_inicial()
        menu_principal(usuario_logado)