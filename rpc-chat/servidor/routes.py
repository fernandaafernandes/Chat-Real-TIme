from flask import Blueprint, request, jsonify
import json
import os
from datetime import datetime

routes = Blueprint("routes", __name__)

#  armazenar mensagens e usuários (simulando um banco de dados simples)
DATA_FILE = "database.json"

def carregar_dados():
    
    if not os.path.exists(DATA_FILE):
        return {"mensagens": [], "usuarios": []}
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except:
        return {"mensagens": [], "usuarios": []}

def salvar_dados(dados):
    
    with open(DATA_FILE, "w") as f:
        json.dump(dados, f, indent=4)

@routes.route("/entrar", methods=["POST"])
def entrar():
    data = request.json
    usuario = data.get("username")
    
    dados = carregar_dados()
    if usuario not in dados["usuarios"]:
        dados["usuarios"].append(usuario)
        salvar_dados(dados)

    return jsonify({"status": "ok", "usuarios": dados["usuarios"]})

@routes.route('/enviar', methods=['POST'])
def enviar_mensagem():
    dados_requisicao = request.get_json()
    usuario = dados_requisicao.get('username')
    mensagem = dados_requisicao.get('message')
    hora = datetime.now().strftime("%H:%M:%S")
    
    dados = carregar_dados()
    nova_mensagem = {
        "usuario": usuario,
        "texto": mensagem,
        "hora": hora
    }
    dados["mensagens"].append(nova_mensagem)
    salvar_dados(dados)
    
    print(f"[{hora}] [{usuario}] disse: {mensagem}")
    return jsonify({"status": "sucesso"}), 200

@routes.route("/mensagens", methods=["GET"])
def listar_mensagens():
    dados = carregar_dados()
    return jsonify(dados["mensagens"])

@routes.route("/usuarios", methods=["GET"])
def listar_usuarios():
    dados = carregar_dados()
    return jsonify(dados["usuarios"])

@routes.route("/sair", methods=["POST"])
def sair():
    data = request.json
    usuario = data.get("username")

    dados = carregar_dados()
    if usuario in dados["usuarios"]:
        dados["usuarios"].remove(usuario)
        salvar_dados(dados)

    return jsonify({"status": "saiu"})

@routes.route("/ping", methods=["GET"])
def ping():
    #  verificar qual servidor está ativo
    return jsonify({"status": "servidor ativo"}), 200