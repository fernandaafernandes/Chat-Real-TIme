# RPC-Chat: Sistema de Mensagens Distribuído

Este projeto implementa um chat em tempo real usando Python e Flask, com foco em conceitos de sistemas distribuídos. Inclui servidor e cliente que trocam mensagens via HTTP + JSON, com tratamento de falha de conexão e persistência temporária das mensagens.

## 🔍 Recursos principais

- Comunicação cliente-servidor via REST API (HTTP/JSON)
- Envio e visualização de mensagens em tempo real
- Armazenamento temporário de mensagens no servidor
- Lista de usuários conectados
- Detecção de queda de servidor e desligamento do cliente (try/except)

## 📁 Estrutura do projeto

```
rpc-chat/
├── cliente/
│   └── client.py
├── servidor/
│   ├── app.py
│   ├── routes.py
│   └── storage.py
├── scripts/
│   └── run_server.sh
└── tests/
    └── teste_api.py
```

## 🛠️ Tecnologias

- Python 3.10+
- Flask
- requests
- VirtualBox (ambiente de testes)
- Ubuntu Server 22.04 LTS

## 🌐 Configuração de rede (VirtualBox, Internal Network)

Em cada VM, configure IPs estáticos (exemplo Netplan em `/etc/netplan/00-installer-config.yaml`):

```yaml
network:
  version: 2
  renderer: networkd
  ethernets:
    enp0s3:
      addresses:
        - 10.0.0.1/24
```

### IPs sugeridos

- Servidor primário: 10.0.0.1
- Servidor secundário (backup): 10.0.0.10
- Cliente 1: 10.0.0.2
- Cliente 2: 10.0.0.3

## ▶️ Executando os servidores

1. No servidor primário (10.0.0.1):

```bash
cd /Users/fernandafernandes/Chat-Real-TIme/rpc-chat/servidor
python3 app.py
```

2. No servidor secundário (10.0.0.10):

```bash
cd /Users/fernandafernandes/Chat-Real-TIme/rpc-chat/servidor
python3 app.py
```

> O cliente deve ser configurado para tentar o IP primário (10.0.0.1) e, em caso de falha, recuar para o secundário (10.0.0.10).

## ▶️ Executando o cliente

```bash
cd /Users/fernandafernandes/Chat-Real-TIme/rpc-chat/servidor
python3 app.py
```

## ▶️ Executando o cliente

```bash
cd /Users/fernandafernandes/Chat-Real-TIme/rpc-chat/cliente
python3 client.py
```

## 🧾 Uso do cliente (menu)

1. Enviar mensagem
2. Ver mensagens
3. Ver usuários
4. Sair

- Ao enviar mensagem, servidor grava em `mensagens` e exibe no terminal.
- Na opção 2, cliente exibe todas as mensagens recebidas do servidor.

## ⚠️ Tratamento de exceções

- Se o servidor estiver offline no login inicial, cliente exibe erro e fecha.
- Se houver perda de conexão durante o uso, cliente informa e encerra com segurança.

## 🧪 Teste rápido de fluxo

1. Abra servidor
2. Abra 2 clientes em VMs diferentes
3. Digite usuário em cada cliente
4. Envie mensagens (opção 1) e depois veja o histórico (opção 2)
5. Pare o servidor para verificar o tratamento de queda do cliente

