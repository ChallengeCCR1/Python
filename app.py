from flask import Flask, jsonify, request
from datetime import datetime
import pandas as pd

app = Flask(__name__)

## mapa
@app.route('/mapa/linha9', methods=['GET'])
def mapa_linha9():
    estacoes = [
        "Osasco", "Presidente Altino", "Ceasa", "Villa Lobos", "Pinheiros", "Cidade Jardim",
        "Vila Olímpia", "Berrini", "Morumbi", "Granja Julieta", "João Dias", "Santo Amaro",
        "Socorro", "Jurubatuba", "Autódromo", "Interlagos", "Grajaú"
    ]

    destaques = {
        "Pinheiros": "⭐ Pinheiros",
        "Santo Amaro": "🚆 Santo Amaro"
    }

    estacoes_formatadas = [destaques.get(est, est) for est in estacoes]

    return jsonify({
        "linha": "Linha 9 Esmeralda",
        "estacoes": estacoes_formatadas
    })

## previsao de pico
@app.route('/pico', methods=['GET'])
def previsao_pico():
    estacao = request.args.get('estacao')
    if not estacao:
        return jsonify({
            "erro": "Parâmetro 'estacao' é obrigatório.",
        }), 400
    
    try:
        df = pd.read_csv("fluxo_passageiros.csv")
        df_estacao = df[df["Estacao"] == estacao]

        if df_estacao.empty:
            return jsonify({"erro": f"Estação '{estacao}' não encontrada ou sem dados."}), 404

        df_estacao["Horario"] = pd.to_datetime(df_estacao["Horario"], format='%H:%M').dt.time
        horario_atual = datetime.now().time()
        horario_mais_proximo = min(
            df_estacao["Horario"],
            key=lambda x: abs(datetime.combine(datetime.today(), x) - datetime.combine(datetime.today(), horario_atual))
        )

        fluxo = df_estacao[df_estacao["Horario"] == horario_mais_proximo]["Passageiros"].values[0]
        return jsonify({
            "estacao": estacao,
            "horario_mais_proximo": horario_mais_proximo.strftime("%H:%M"),
            "fluxo_passageiros": int(fluxo)
        })

    except Exception as e:
        return jsonify({"erro": str(e)}), 500
    
@app.route('/')
def home():
    return jsonify({
        "mensagem": "API de Previsão de Pico e Mapa da Linha 9 Esmeralda. Use as rotas /mapa/linha9 e /pico?estacao=NomeDaEstacao"
    })
    
if __name__ == "__main__":
    app.run(debug=True)
