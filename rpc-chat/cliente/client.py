import requests


SERVIDORES = ["http://10.0.0.1:5000", "http://10.0.0.10:5000"]
URL_ATUAL = None

def buscar_servidor_ativo():
    """Tenta encontrar um servidor online na lista."""
    for url in SERVIDORES:
        try:
            
            requests.get(f"{url}/usuarios", timeout=1)
            return url
        except:
            continue
    return None

usuario = input("Digite seu nome: ")


URL_ATUAL = buscar_servidor_ativo()

if not URL_ATUAL:
    print("Erro: Nenhum servidor (1 ou 2) está online. Verifique a rede.")
    exit()

try:
    requests.post(f"{URL_ATUAL}/entrar", json={"username": usuario})
    print(f"Conectado ao servidor: {URL_ATUAL}")
except Exception as e:
    print(f"Erro ao entrar: {e}")
    exit()

while True:
    print(f"\n--- Servidor Atual: {URL_ATUAL} ---")
    print("1 - Enviar mensagem")
    print("2 - Ver mensagens")
    print("3 - Ver usuários")
    print("4 - Sair")

    opcao = input("Escolha: ")

    try:
        if opcao == "1":
            msg = input("Mensagem: ")
            requests.post(f"{URL_ATUAL}/enviar", json={
                "username": usuario,
                "message": msg
            }, timeout=2)

        elif opcao == "2":
            res = requests.get(f"{URL_ATUAL}/mensagens", timeout=2)
            for m in res.json():
                print(f"{m['hora']} - {m['usuario']}: {m['texto']}")

        elif opcao == "3":
            res = requests.get(f"{URL_ATUAL}/usuarios", timeout=2)
            print("Usuários:", res.json())

        elif opcao == "4":
            requests.post(f"{URL_ATUAL}/sair", json={"username": usuario}, timeout=2)
            print("Saindo do chat...")
            break
        
    except (requests.exceptions.ConnectionError, requests.exceptions.Timeout):
        print("\n[!] CONEXÃO PERDIDA com o servidor atual. Buscando backup...")
        
        # procura o outro servidor
        nova_url = buscar_servidor_ativo()
        
        if nova_url and nova_url != URL_ATUAL:
            URL_ATUAL = nova_url
            print(f"[OK] Migrado para o servidor de backup: {URL_ATUAL}")
           
            requests.post(f"{URL_ATUAL}/entrar", json={"username": usuario})
        else:
            print("[ERRO] Todos os servidores estão fora do ar. Encerrando.")
            break