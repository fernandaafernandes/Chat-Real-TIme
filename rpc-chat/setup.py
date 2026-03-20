import os

estrutura = [
    "rpc-chat/servidor",
    "rpc-chat/cliente",
    "rpc-chat/docs",
    "rpc-chat/tests",
    "rpc-chat/scripts"
]

arquivos = [
    "rpc-chat/servidor/app.py",
    "rpc-chat/servidor/routes.py",
    "rpc-chat/servidor/storage.py",
    "rpc-chat/cliente/client.py",
    "rpc-chat/tests/teste_api.py",
    "rpc-chat/scripts/run_server.sh",
    "rpc-chat/requirements.txt",
    "rpc-chat/README.md",
    "rpc-chat/.gitignore"
]

# Criar pastas
for pasta in estrutura:
    os.makedirs(pasta, exist_ok=True)

# Criar arquivos vazios
for arquivo in arquivos:
    with open(arquivo, "w") as f:
        pass

print("Estrutura criada com sucesso 🚀")