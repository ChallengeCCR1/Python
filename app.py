import time
import os
import json
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime
import oracledb
from conecction_oracle import obter_conexao
import getpass
import sqlite3

'''
1. Consumo de uma API externa pública;
2. Integraçração com banco de dados (inserir ok, atualizar (pendente), deletar (pendente), select (ok));
3. Realizar duas consultas no banco de dados (select, where) e ter a opção de exportar essas consultas
para arquivos.json;

---------

Restante é documentação.

'''

def exibir_nome_do_programa():
    print("""𝗙𝘂𝘁𝘂𝗿𝗲 𝗦𝘁𝗮𝘁𝗶𝗼𝗻🚄""")

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
    """Salva os usuários no arquivo JSON."""
    try:
        with open('usuarios.json', mode='w', encoding='utf-8') as arq:
            json.dump(usuarios, arq, ensure_ascii=False, indent=4)
    except Exception as e:
        print(f"Ocorreu um erro ao salvar o arquivo: {e}")

def carregar_usuarios():
    """Carrega os usuários do arquivo JSON."""
    global usuarios
    try:
        with open('usuarios.json', mode='r', encoding='utf-8') as arq:
            usuarios = json.load(arq)
    except FileNotFoundError:
        usuarios = {}
    except Exception as e:
        print(f"Ocorreu um erro ao carregar o arquivo: {e}")
        usuarios = {}

def cadastrar_usuario():
    """Cadastra um novo usuário."""
    try: 
        print("\n===== Cadastro =====")
        usuario = input("Digite um nome de usuário: ").strip().upper()
        if usuario in usuarios:
            print("Usuário já cadastrado. Tente fazer login.")
            input("Pressione 'Enter' para continuar...")
            return False
        email = input("Digite seu e-mail: ").strip().lower()
        senha = getpass.getpass("Digite uma senha: ")
        inserir_usuario(usuario, email, senha)

        usuarios[usuario] = {"email": email, "senha": senha}
        salvar_usuarios_json()
        print("Cadastro realizado com sucesso! Você agora pode fazer login.")
        input("Pressione 'Enter' para continuar...")
    except Exception as e:
        print(f"Ocorreu um erro durante o cadastro: {e}")

def fazer_login():
    """Realiza o login de um usuário utilizando e-mail e senha."""
    try:
        print("\n===== Login =====")
        email_input = input("E-mail: ").strip()
        senha_input = getpass.getpass("Senha: ")
        
        for usuario, dados in usuarios.items():
            if dados["email"] == email_input:
                if dados["senha"] == senha_input:
                    print(f"Login realizado com sucesso! Bem-vindo(a), {usuario.upper()}!")
                    input("Pressione 'Enter' para continuar...\n")
                    return usuario
                else:
                    print("Senha incorreta!")
                    input("Pressione 'Enter' para tentar novamente...\n")
                    return None
        print("E-mail não encontrado!")
        input("Pressione 'Enter' para tentar novamente...\n")
    except Exception as e:
        print(f"Ocorreu um erro ao fazer login: {e}")
    
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

# estações linha 9 esmeralda
estacoes_esmeralda = [
    "Osasco", "Presidente Altino", "Ceasa", "Vila Lobos", "Pinheiros",
    "Cidade Jardim", "Vila Olimpia", "Berrini", "Morumbi", "Granja Julieta",
    "João Dias", "Santo Amaro", "Socorro", "Jurubatuba", "Autódromo",
    "Interlagos", "Grajaú"
]

dados_estacao = {
    "08:00": 1200,
    "09:00": 700,
    "10:00": 500,
    "11:00": 400,
    "12:00": 670,
    "13:00": 789,
    "14:00": 600,
    "15:00": 400,
    "16:00": 560,
    "17:00": 700,
    "18:00": 980,
    "19:00": 1240,
    "20:00": 1300,
    "21:00": 1000,
    "22:00": 987,
    "23:00": 654
}

def obter_estacao_valida(mensagem):
    """Solicita ao usuário uma estação e verifica se ela existe no banco."""
    while True:
        estacao = input(mensagem).strip()
        if estacao in estacoes_esmeralda:
            return estacao
        print("❌ Estação inválida. Tente novamente!")

def calcular_tempo_total(origem, destino):
    """Calcula o tempo total da viagem entre duas estações."""
    if origem not in estacoes_esmeralda or destino not in estacoes_esmeralda:
        return None
    
    idx_origem = estacoes_esmeralda.index(origem)
    idx_destino = estacoes_esmeralda.index(destino)

    if idx_origem > idx_destino:
        idx_origem, idx_destino = idx_destino, idx_origem
    
    return sum(
        tempos_viagem.get((estacoes_esmeralda[i], estacoes_esmeralda[i + 1]), 0)
        for i in range(idx_origem, idx_destino)
    )
    
def encontrar_horario_proximo(hora_partida):
    """Encontra o horário mais próximo da hora_partida dentro dos horários disponíveis no dicionário."""
    horarios_disponiveis = list(dados_estacao.keys())
    horarios_disponiveis.sort() 
    for horario in reversed(horarios_disponiveis):
        if hora_partida >= horario:
            return horario
    return horarios_disponiveis[0]

def obter_estacao_valida(mensagem, cursor):
    """Solicita ao usuário uma estação e verifica se ela existe no banco de dados."""
    while True:
        estacao = input(mensagem).strip()
        cursor.execute("SELECT COUNT(*) FROM ESTACAO WHERE NOME = :1", [estacao])
        if cursor.fetchone()[0] > 0:
            return estacao
        print("❌ Estação inválida. Tente novamente!")

def obter_id_estacao(nome_estacao, cursor):
    """Busca o ID da estação no banco de dados pelo nome."""
    cursor.execute("SELECT ID_ESTACAO FROM ESTACAO WHERE NOME = :1", [nome_estacao])
    row = cursor.fetchone()
    return row[0] if row else None

def iniciar_viagem(usuario):
    """Inicia a simulação de uma viagem e registra no banco de dados."""
    conexao = obter_conexao()
    if conexao is None:
        print("Falha ao obter conexão com banco de dados.")
        return

    try:
        cursor = conexao.cursor()
        
        print("\n===== Iniciar Viagem =====")
        origem = obter_estacao_valida("Digite a estação de origem: ", cursor)
        destino = obter_estacao_valida("Digite a estação de destino: ", cursor)

        tempo_estimado = calcular_tempo_total(origem, destino)
        if tempo_estimado is None:
            print("❌ Erro ao calcular o tempo de viagem.")
            return

        print(f"⏳ Tempo estimado de viagem de {origem} para {destino}: {tempo_estimado} minutos.")

        confirmacao = input("Deseja iniciar a viagem? (s/n): \n").strip().lower()
        if confirmacao != 's':
            print("Viagem cancelada.\n")
            return

        hora_partida = datetime.now()
        print(f"🚆 Viagem iniciada às {hora_partida.strftime('%H:%M:%S')}.\n")
        print("Aperte Enter para encerrar a viagem...")
        input()

        hora_chegada_real = datetime.now();
        tempo_real_decorrido = (hora_chegada_real - hora_partida).total_seconds() / 60
        data_viagem = hora_partida.strftime("%d/%m/%Y")

        print(f"Finalizando a sua viagem, {usuario}...\n")
        time.sleep(3)

        # Simula a chegada com base no tempo estimado
        print(f"🏁 Viagem concluída às {hora_chegada_real.strftime('%H:%M:%S')}.")
        print(f"🕒 Tempo real decorrido: {tempo_real_decorrido:.2f} minutos, na data de {data_viagem}.")

        # Registro da viagem
        viagem = {
            "usuario": usuario,
            "origem": origem,
            "destino": destino,
            "partida": hora_partida.strftime('%H:%M:%S'),
            "chegada": hora_chegada_real.strftime('%H:%M:%S'),
            "tempo_estimado": tempo_estimado,
            "tempo_real": tempo_real_decorrido,
            "data": data_viagem 
        }

        viagens.append(viagem)
        salvar_viagens_json()

        # Buscar IDs das estações
        id_origem = obter_id_estacao(origem, cursor)
        id_destino = obter_id_estacao(destino, cursor)

        if id_origem is None or id_destino is None:
            print("❌ Erro: Estação de origem ou destino não encontrada no banco de dados.")
            return

        # Insere a viagem no banco
        sql = """
            INSERT INTO VIAGEM (ID_VIAGEM, HPARTIDA, HCHEGADA, ESTACAO_ORIGEM, ESTACAO_DESTINO)
            VALUES (gerador_id_chall.NEXTVAL, :1, :2, :3, :4)
        """
        cursor.execute(sql, [hora_partida, hora_chegada_real, id_origem, id_destino])
        conexao.commit()
        print("✅ Viagem registrada com sucesso!\n")

    except oracledb.DatabaseError as e:
        print(f"❌ Erro ao registrar viagem: {e}")
    finally:
        if conexao:
            conexao.close()

# Relatório de viagens
def exibir_relatorio(usuario):
    try:
        print(f"\n===== Relatório de Viagens de {usuario} =====")
        
        # Verifica se a lista de viagens foi corretamente registrada
        if not viagens:
            print("Nenhuma viagem registrada até o momento.")
            input("\nPressione Enter para voltar ao menu...")
            #voltar_sair()  # Voltar ao menu
            return

        viagens_usuario = [v for v in viagens if v["usuario"] == usuario]
        
        if not viagens_usuario:
            print("Nenhuma viagem registrada para este usuário.")
            input("\nPressione Enter para voltar ao menu...") 
        else:
            for i, v in enumerate(viagens_usuario, 1):
                print(f"\n🚆 Viagem {i}")
                print(f"   📍 Origem: {v['origem']}")
                print(f"   🎯 Destino: {v['destino']}")
                print(f"   ⏳ Partida: {v['partida']} | 🏁 Chegada: {v['chegada']}")
                print(f"   🕒 Tempo de viagem: {v.get('tempo_real', 'Desconhecido')} minutos.")
                print(f"   📅 Data: {v.get('data', 'Desconhecida')}")

        input("\nPressione Enter para voltar ao menu...")

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

        # Carregar os dados do CSV
        df = pd.read_csv("fluxo_passageiros.csv")

        while True:
            escolha_estacao = input("Informe a estação que deseja saber o pico de passageiros: ").strip()

            estacao_encontrada = any(escolha_estacao in estacoes for estacoes in ccr_estacoes.values())

            if not estacao_encontrada:
                print(f"A estação {escolha_estacao} não pertence a uma linha da CCR. Tente novamente.")
                continue

            df_estacao = df[df["Estacao"] == escolha_estacao].copy()

            if df_estacao.empty:
                print(f"Não há dados disponíveis para a estação {escolha_estacao}.")
                continue

            df_estacao["Horario"] = pd.to_datetime(df_estacao["Horario"], format='%H:%M').dt.time

            print("\nOpções:")
            print("1. Ver o pico no horário atual")
            print("2. Escolher um horário específico")
            print("3. Ver gráfico de fluxo de passageiros")
            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                horario_atual = datetime.now().time()
                horario_mais_proximo = min(df_estacao["Horario"], key=lambda x: abs(datetime.combine(datetime.today(), x) - datetime.combine(datetime.today(), horario_atual)))
                fluxo_passageiros = df_estacao[df_estacao["Horario"] == horario_mais_proximo]["Passageiros"].values[0]

                print(f"No horário mais próximo ({horario_mais_proximo.strftime('%H:%M')}), a estação {escolha_estacao} tem {fluxo_passageiros} passageiros.")

            elif opcao == "2":
                horario_escolhido = input("Digite o horário no formato HH:MM: ").strip()

                try:
                    horario_escolhido = datetime.strptime(horario_escolhido, "%H:%M").time()
                except ValueError:
                    print("Formato de horário inválido. Tente novamente.")
                    continue

                if horario_escolhido not in df_estacao["Horario"].values:
                    print(f"Não há registros para o horário {horario_escolhido.strftime('%H:%M')}.")
                else:
                    fluxo_passageiros = df_estacao[df_estacao["Horario"] == horario_escolhido]["Passageiros"].values[0]
                    print(f"No horário {horario_escolhido.strftime('%H:%M')}, a estação {escolha_estacao} tem {fluxo_passageiros} passageiros.")

            elif opcao == "3":
                # Converter para datetime completo e ordenar
                df_estacao["Horario_dt"] = pd.to_datetime(df_estacao["Horario"].astype(str), format='%H:%M:%S')
                df_estacao = df_estacao.sort_values(by="Horario_dt")

                # Plotar gráfico
                plt.figure(figsize=(10, 5))
                plt.plot(df_estacao["Horario_dt"], df_estacao["Passageiros"], marker='o', linestyle='-', color='blue')
                plt.title(f"Fluxo de Passageiros - Estação {escolha_estacao}")
                plt.xlabel("Horário")
                plt.ylabel("Número de Passageiros")
                plt.xticks(rotation=45)
                plt.grid(True)

                # Destacar o pico
                pico = df_estacao.loc[df_estacao["Passageiros"].idxmax()]
                plt.axvline(pico["Horario_dt"], color='red', linestyle='--', label='Horário de Pico')
                plt.legend()

                plt.tight_layout()
                plt.show()

            else:
                print("Opção inválida. Retornando ao menu.")
                continue

            input("\nPressione 'Enter' para voltar ao menu...")
            break

    except Exception as e:
        print(f"Ocorreu um erro ao prever o pico: {e}")


def mapa_linha():
    try:
        print("\n===== Mapa =====")
        print("1. Linha 9 Esmeralda")
        print("2. Linha 4 Amarela (em breve)")
        print("3. Linha 8 Diamante (em breve)")
        print("4. Retornar ao menu principal")

        opcao = input("\nEscolha uma linha para ver o mapa: ")

        print("\n --------------------- ")

        if opcao == "1":
            exibir_mapa_linha9()
        elif opcao == "4":
            return
        else:
            print("\nEssa linha ainda não está disponível!")

            input("\nPressione 'Enter' para voltar ao menu das linhas.")
            mapa_linha()

    except Exception as e:
        print(f"Erro ao exibir as informações da linha: {e}")

def exibir_mapa_linha9():
    print("\n===== 🟩 Mapa da Linha 9 Esmeralda =====\n")

    # Lista de estações da Linha 9
    estacoes_linha9 = [
        "Osasco", "Presidente Altino", "Ceasa", "Villa Lobos", "Pinheiros", "Cidade Jardim",
        "Vila Olímpia", "Berrini", "Morumbi", "Granja Julieta", "João Dias", "Santo Amaro",
        "Socorro", "Jurubatuba", "Autódromo", "Interlagos", "Grajaú"
    ]

    # Destaques especiais
    destaques = {
        "Pinheiros": "⭐ Pinheiros",
        "Santo Amaro": "🚆 Santo Amaro"
    }

    # Dividindo a linha em blocos para melhor visualização
    blocos = [estacoes_linha9[i:i+5] for i in range(0, len(estacoes_linha9), 5)]

    for bloco in blocos:
        linha_formatada = "───".join([f"● {destaques.get(est, est)}" for est in bloco])
        print(linha_formatada)

    input("\n\nPressione 'Enter' para voltar ao menu das linhas.")
    mapa_linha()

def centro_controle_operacional():
    while True:
        try:
            print("\n===== Centro de Controle Operacional =====")
            print("1. Linha 4 Amarela. ")
            print("2. Linha 8 Diamante. ")
            print("3. Linha 9 Esmeralda. ")
            print("4. Retornar ao menu principal. ")
            opcao_linha = input("Escolha uma opção: ")

            if opcao_linha == "1":
                print(avisos[0])
            elif opcao_linha == "2":
                print(avisos[1])
            elif opcao_linha == "3":
                print(avisos[2])
            elif opcao_linha == "4":
                break
            else:
                print("Opção inválida. Por favor, escolha uma opção válida.")
                continue

            input("Pressione 'Enter' para retornar ao menu de opções...")
            
        except Exception as e:
            print(f"Erro ao exibir o painel de avisos: {e}")

def exportar_estacoes_para_json():
    nome_linha = input("Digite o nome da linha (ex: Linha 9): ")

    conexao = obter_conexao()
    if conexao is None:
        print("Falha ao obter conexão com banco de dados.")
        return

    try:
        with conexao.cursor() as cursor:
            
            cursor.execute("SELECT id_linhametro FROM LinhaMetro WHERE LOWER(nome) = :1", [nome_linha.lower()])
            resultado = cursor.fetchone()
            
            if resultado is None:
                print("Linha não encontrada.")
                return
            
            id_linha = resultado[0]

            
            cursor.execute("""
                SELECT nome, localizacao FROM Estacao
                WHERE id_linhametro = :1
                """, [id_linha])

            estacoes = cursor.fetchall()
            if not estacoes:
                print("Nenhuma estação encontrada para essa linha.")
                return

            estacoes_json = [{"nome": nome, "localizacao": local} for nome, local in estacoes]
            nome_arquivo = nome_linha.replace(" ", "_").lower() + "_estacoes.json"

            with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
                json.dump(estacoes_json, arquivo, indent=4, ensure_ascii=False)

            print(f"Estações da {nome_linha} exportadas com sucesso para {nome_arquivo}!")

    except Exception as e:
        print(f"Erro durante exportação: {e}")
    finally:
        conexao.close()


# menu de cadastro/login
def menu_inicial():
    usuario = None
    while usuario is None:
        try:
            print(f"\nSeja bem-vindo ao Sistema da Future Station!")
            print("1. Cadastro")
            print("2. Login")
            print("3. Sair")

            opcao = input("Escolha uma opção: ").strip()
        
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

    return usuario

## menu após login
def menu_principal(usuario):
    while True:
        try:
            exibir_nome_do_programa()
            
            print(f"\nBem vindo, {usuario}!")
            print("1. Mapa")
            print("2. Iniciar viagem")
            print("3. Relatório de viagens")
            print("4. Status Operacional")
            print("5. Previsão de pico")
            print("6. Exportar estações para JSON")
            print("7. logout")

            opcao = input("Escolha uma opção: ")

            if opcao == '1':
                mapa_linha()
            elif opcao == '2':
                iniciar_viagem(usuario)
            elif opcao == '3':
                exibir_relatorio(usuario)
            elif opcao == '4':
                centro_controle_operacional()
            elif opcao == '5':
                previsao_pico()
            elif opcao == '6':
                exportar_estacoes_para_json()
            elif opcao == '7':
                print(f"Poxa, {usuario}! Parece que escolheu sair...")
                return
            else:
                print("Opção inválida!")

        except Exception as e:
            print(f"Ocorreu um erro iniesperado: {e}")


## conexao com banco de dados oracle
def inserir_usuario(usuario, email, senha):
    conexao = obter_conexao()
    if conexao is None:
        print("Falha ao obter conexão com banco de dados.")
        return
    
    try:
        with conexao.cursor() as cursor:
            email = email.lower()  # Normaliza o e-mail para evitar duplicatas com maiúsculas/minúsculas
            
            # Verifica se o e-mail já existe
            cursor.execute("SELECT COUNT(*) FROM Usuario_Challenge WHERE LOWER(email) = :1", [email])
            resultado = cursor.fetchone()
            
            if resultado[0] > 0:
                print("Erro: o e-mail fornecido já está cadastrado.")
                return
            
            # Insere o usuário no banco
            sql = """
                INSERT INTO Usuario_Challenge (id_usuario, nome, email, senha)
                VALUES (gerador_id_chall.NEXTVAL, :1, :2, :3)
            """
            cursor.execute(sql, [usuario, email, senha])
            conexao.commit()

    except oracledb.IntegrityError as e:
        print(f"Erro de integridade: {e}")
    except oracledb.DatabaseError as e:
        print(f"Erro ao inserir usuário: {e}")
    finally:
        if conexao:
            conexao.close()


if __name__ == "__main__":
    carregar_viagens_json()
    carregar_usuarios()
    while True:
        usuario_logado = menu_inicial()
        menu_principal(usuario_logado)