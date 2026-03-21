# RPC Chat - Sistema de Mensagens Distribuído

Este projeto consiste em um sistema de chat em tempo real desenvolvido para o curso de Análise e Desenvolvimento de Sistemas (Sistemas Distribuidos). O objetivo é demonstrar a comunicação entre múltiplas máquinas virtuais (VMs) utilizando o protocolo HTTP e o conceito de RPC (Remote Procedure Call). O sistema permite que usuários enviem mensagens de clientes para um servidor central, que as armazena e exibe em tempo real.

## Funcionalidades

- **Comunicação RPC**: Utiliza chamadas de procedimento remoto via HTTP para enviar mensagens.
- **Interface de Linha de Comando**: Cliente simples para identificação do usuário e envio de mensagens.
- **Armazenamento Temporário**: Servidor armazena mensagens em uma lista temporária e exibe logs no terminal.
- **Suporte a Múltiplas VMs**: Configurado para funcionar em ambiente virtualizado com IPs fixos.
- **Logs em Tempo Real**: Mensagens são exibidas no terminal do servidor conforme chegam.

## Tecnologias e Ambiente

- **Linguagem**: Python 3
- **Framework**: Flask
- **Virtualização**: Oracle VirtualBox
- **Sistema Operacional**: Ubuntu Server 22.04 LTS
- **Rede**: Configuração de Rede Interna (Internal Network)

## Pré-requisitos

- Python 3 instalado nas VMs.
- Oracle VirtualBox para virtualização.
- Conhecimento básico de configuração de rede em Ubuntu.

## Configuração de Rede (IP Fixo)

Para garantir a comunicação estável, as VMs devem ser configuradas com IPs estáticos no mesmo segmento de rede:

- **VM Servidor**: 10.0.0.1
- **VM Cliente 01**: 10.0.0.2
- **VM Cliente 02**: 10.0.0.3

A máscara de sub-rede utilizada é 255.255.255.0 (/24).

### Configuração no Ubuntu

Edite o arquivo de configuração do Netplan (geralmente `/etc/netplan/00-installer-config.yaml` ou similar):

```yaml
network:
  ethernets:
    enp0s3:
      addresses:
        - 10.0.0.1/24  # Para o servidor, ajuste conforme necessário
     
```

Aplique as mudanças com `sudo netplan apply`.

## Instalação e Execução

### No Servidor

1. Acesse a pasta do projeto: `cd /caminho/para/o/projeto`
2. Execute o servidor: `python3 servidor/app.py`

### Nos Clientes

1. Acesse a pasta do projeto em cada VM cliente: `cd /caminho/para/o/projeto`
2. Execute o cliente: `python3 cliente/client.py`

### Interação

- Digite seu nome de usuário quando solicitado.
- Comece a enviar mensagens. Elas aparecerão no terminal do servidor conforme configurado no arquivo `routes.py`.

## Observações de Configuração

- **Firewall**: O firewall do Ubuntu deve permitir conexões na porta 5000. Execute: `sudo ufw allow 5000`
- **Netplan**: A configuração de IP persistente deve ser feita no diretório `/etc/netplan/` para evitar perda de conexão após reiniciar a VM.
- **Indentação**: O código Python deve seguir rigorosamente a indentação de 4 espaços para evitar erros de execução no servidor.
- **Dependências**: Certifique-se de que o Flask está instalado: `pip install flask`

## Estrutura do Projeto

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


