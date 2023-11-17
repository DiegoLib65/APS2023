# API - Lugar para disponibilizar recursos e/ou funcionalidades. 
# 1. Objetivo - Criar um api qu disponibiliza a consulta, criação, edição e exclusão de filmes.
# 2. URL base - localhost
# 3. Endpoints - 
    # - localhost/filmes (GET)
    # - localhost/filmes (POST)
    # - localhost/filmes/id (GET)
    # - localhost/filme/id (PUT)
    # - localhost/filme/id (DELETE)
# 4. Quais recusrsos - filmes

from flask import Flask, jsonify,request
from db import filmes
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


#Consultar(todos)
@app.route('/filmes',methods=['GET'])
def obter_filmes():
    return jsonify(filmes)

#Consultar(id, nome ou Diretor)

@app.route('/filmes/<id>',methods=['GET'])
def obter_filme_id(id):
    filmes_status = []
    for filme in filmes:
        if filme.get('id') == id or filme.get('Diretor') == id or filme.get('titulo') == id or filme.get('estado') == id: 
                filmes_status.append(filme)
    return jsonify(filmes_status)

#Editar um filme por ID
@app.route('/filmes/<id>',methods=['PUT'])
def editar_filme_id(id):
    filme_alterado = request.get_json()
    for indice,filme in enumerate(filmes):
        if filme.get('id') == id:
            filmes[indice].update(filme_alterado)
            return jsonify(filmes[indice])

#Criar novo filme
@app.route('/filmes', methods=['POST'])
def incluir_novo_filme():
    novo_filme = request.get_json()
    filmes.append(novo_filme)

    return jsonify(filmes)

#Excluir filme
@app.route('/filmes/<id>', methods=['DELETE'])
def excluir_filme(id):
    for indice, filme in enumerate(filmes):
        if filme.get('id') == id:
            del filmes[indice]
    
    
    return jsonify(filmes)


app.run(port=5000,host='0.0.0.0',debug=True)