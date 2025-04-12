import time
import oracledb

from conecction_oracle import obter_conexao
from operacoes_json import carregar_viagens_json, salvar_viagens_json
from datetime import datetime
from dados import viagens

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
    carregar_viagens_json() 
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

        global viagens
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