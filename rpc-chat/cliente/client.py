import requests

URL = "http://localhost:5000"

usuario = input("Digite seu nome: ")

requests.post(f"{URL}/entrar", json={"username": usuario})

while True:
    print("\n1 - Enviar mensagem")
    print("2 - Ver mensagens")
    print("3 - Ver usuários")
    print("4 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        msg = input("Mensagem: ")
        requests.post(f"{URL}/enviar", json={
            "username": usuario,
            "message": msg
        })

    elif opcao == "2":
        res = requests.get(f"{URL}/mensagens")
        for m in res.json():
            print(f"{m['hora']} - {m['usuario']}: {m['texto']}")

    elif opcao == "3":
        res = requests.get(f"{URL}/usuarios")
        print("Usuários:", res.json())

    elif opcao == "4":
        requests.post(f"{URL}/sair", json={"username": usuario})
        break