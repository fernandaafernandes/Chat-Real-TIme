from flask import Blueprint, request, jsonify
import json
import os
from datetime import datetime, timedelta

routes = Blueprint("routes", __name__)


DATA_FILE = "/home/fernanda/projeto_faculdade/database.json"

def carregar_dados():
    if not os.path.exists(DATA_FILE):
        return {"mensagens": [], "usuarios": []}
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            dados = json.load(f)
        
            print(f"[BACKUP] Lendo arquivo. Mensagens encontradas: {len(dados['mensagens'])}")
            return dados
    except:
        return {"mensagens": [], "usuarios": []}

def salvar_dados(dados):
    try:
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(dados, f, indent=4, ensure_ascii=False)
            f.flush() # Força a escrita no disco 
            os.fsync(f.fileno()) 
    except IOError as e:
        print(f"Erro de permissão ou escrita: {e}")

def sincronizar_log_historico():
    """Lê o arquivo de backup e imprime as mensagens antigas no terminal do servidor atual."""
    dados = carregar_dados()
    mensagens = dados.get("mensagens", [])
    
    if mensagens:
        print("\n" + "="*50)
        print(f" RECUPERANDO MENSAGENS DO BACKUP ({len(mensagens)} mensagens)")
        print("="*50)
        for m in mensagens:
            print(f"[{m['hora']}] {m['usuario']}: {m['texto']}")
        print("="*50 + "\n")
    else:
        print("\n Nenhum histórico de mensagens encontrado no backup.\n")

@routes.route("/entrar", methods=["POST"])
def entrar():
    data = request.get_json()
    if not data or "username" not in data:
        return jsonify({"status": "erro", "message": "Username faltando"}), 400
    
    usuario = data.get("username")
    dados = carregar_dados()
    
    sincronizar_log_historico()
    
    print(f"--> Usuário tentando entrar: {usuario}")

    if usuario not in dados["usuarios"]:
        dados["usuarios"].append(usuario)
        salvar_dados(dados)
        print(f"✅ {usuario} fez login com sucesso.")
    else:
        print(f"ℹ️ {usuario} já estava na lista.")

    return jsonify({"status": "ok", "usuarios": dados["usuarios"]})

@routes.route('/enviar', methods=['POST'])
def enviar_mensagem():
    dados_requisicao = request.get_json()
    usuario = dados_requisicao.get('username')
    mensagem = dados_requisicao.get('message')
    hr_brasilia = datetime.utcnow() - timedelta(hours=3)
    hora = hr_brasilia.strftime("%H:%M:%S")
    
    if not usuario or not mensagem:
        return jsonify({"status": "erro"}), 400

    dados = carregar_dados()
    nova_mensagem = {
        "usuario": usuario,
        "texto": mensagem,
        "hora": hora
    }
    dados["mensagens"].append(nova_mensagem)
    
    
    if usuario not in dados["usuarios"]:
        dados["usuarios"].append(usuario)
        
    salvar_dados(dados)
    
    print(f"[{hora}] [{usuario}] disse: {mensagem}")
    return jsonify({"status": "sucesso"}), 200

@routes.route("/mensagens", methods=["GET"])
def listar_mensagens():
    dados = carregar_dados() 
    print(f"DEBUG: Enviando {len(dados['mensagens'])} mensagens do backup.")
    return jsonify(dados["mensagens"])

@routes.route("/limpar", methods=["DELETE", "POST"])
def limpar_banco():
    """Apaga todas as mensagens e usuários."""
    dados_vazios = {"mensagens": [], "usuarios": []}
    salvar_dados(dados_vazios)
    print("\nDATABASE FOI RESETADO COM SUCESSO!\n")
    return jsonify({"status": "banco limpo"}), 200

@routes.route("/usuarios", methods=["GET"])
def listar_usuarios():
    dados = carregar_dados()
    print(f"Lista de usuários atual: {dados['usuarios']}")
    return jsonify(dados["usuarios"])

@routes.route("/sair", methods=["POST"])
def sair():
    data = request.get_json()
    usuario = data.get("username")

    dados = carregar_dados()
    if usuario in dados["usuarios"]:
        dados["usuarios"].remove(usuario)
        salvar_dados(dados)

    return jsonify({"status": "saiu"})

@routes.route("/ping", methods=["GET"])
def ping():
    return jsonify({"status": "servidor ativo", "timestamp": datetime.now().isoformat()}), 200
