import requests

URL = "http://10.0.0.1:5000"

usuario = input("Digite seu nome: ")


try:
    requests.post(f"{URL}/entrar", json={"username": usuario})
except requests.exceptions.ConnectionError:
    print("Erro: O servidor está offline. Ligue o servidor antes de iniciar o cliente.")
    exit()

while True:
    print("\n1 - Enviar mensagem")
    print("2 - Ver mensagens")
    print("3 - Ver usuários")
    print("4 - Sair")

    opcao = input("Escolha: ")

    try:
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
            print("Saindo do chat...")
            break
        
        else:
            print("Opção inválida!")

    except requests.exceptions.ConnectionError:
        print("\n  CONEXÃO PERDIDA: O servidor foi encerrado ou a rede caiu.")
        print("Encerrando o programa cliente...")
        break