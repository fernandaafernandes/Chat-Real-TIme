from flask import Blueprint, request, jsonify
from storage import mensagens, usuarios
from datetime import datetime

routes = Blueprint("routes", __name__)

@routes.route("/entrar", methods=["POST"])
def entrar():
    data = request.json
    usuario = data.get("username")

    if usuario not in usuarios:
        usuarios.append(usuario)

    return jsonify({"status": "ok", "usuarios": usuarios})


@routes.route('/enviar', methods=['POST'])
def enviar_mensagem():
    dados = request.get_json()
    usuario = dados.get('username')
    mensagem = dados.get('message')
    
  
    print(f"[{usuario}] disse: {mensagem}")
    
    
    return jsonify({"status": "sucesso"}), 200


@routes.route("/mensagens", methods=["GET"])
def listar_mensagens():
    return jsonify(mensagens)


@routes.route("/usuarios", methods=["GET"])
def listar_usuarios():
    return jsonify(usuarios)


@routes.route("/sair", methods=["POST"])
def sair():
    data = request.json
    usuario = data.get("username")

    if usuario in usuarios:
        usuarios.remove(usuario)

    return jsonify({"status": "saiu"})


@routes.route("/ping", methods=["GET"])
def ping():
    return jsonify({"status": "servidor ativo"})