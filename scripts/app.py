from flask import Flask, jsonify, request
import os
from previsao_pico import obter_fluxo, gerar_grafico
from apis import buscar_status_linhas_4_8_9

app = Flask(__name__)

## mapa
@app.route('/api/mapa/linha9', methods=['GET'])
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
@app.route("/api/pico", methods=["GET"])
def api_previsao_pico():
    estacao = request.args.get("estacao")
    horario = request.args.get("horario")  # opcional

    if not estacao:
        return jsonify({"erro": "Informe o nome da estação via parâmetro 'estacao'."}), 400

    resultado, status = obter_fluxo(estacao, horario)
    return jsonify(resultado), status

@app.route("/api/pico/grafico", methods=["GET"])
def api_grafico_pico():
    estacao = request.args.get("estacao")

    if not estacao:
        return jsonify({"erro": "Informe o nome da estação via parâmetro 'estacao'."}), 400

    imagem_base64, status = gerar_grafico(estacao)
    if status != 200:
        return jsonify({"erro": "Erro ao gerar gráfico."}), status

    return jsonify({"estacao": estacao, "grafico_base64": imagem_base64})      

## status das linhas 4, 8 e 9
@app.route("/api/status_linhas_ccr", methods=["GET"])
def status_linhas():
    try:
        status = buscar_status_linhas_4_8_9()
        return jsonify(status)
    except Exception as e:
        return jsonify({"erro": str(e)}), 500  

@app.route('/')
def home():
    return jsonify({
        "mensagem": "API de Previsão de Pico e Mapa da Linha 9 Esmeralda. Use as rotas /mapa/linha9 e /pico?estacao=NomeDaEstacao"
    })
    
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
