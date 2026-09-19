# Monitor de Sistemas

Aplicação desktop desenvolvida em **Python** para acompanhar informações básicas de uso do computador em tempo real. O projeto utiliza **psutil** para coletar métricas do sistema e **Tkinter** para exibi-las em uma interface gráfica simples.

## Funcionalidades

- monitoramento do uso da CPU;
- monitoramento do uso de memória RAM;
- acompanhamento da utilização do disco principal;
- leitura da temperatura do sistema quando suportada pelo sistema operacional e pelos sensores disponíveis;
- atualização automática das métricas a cada segundo;
- coleta do uso individual dos núcleos da CPU.

## Tecnologias

- Python
- Tkinter
- psutil

## Estrutura do projeto

```text
Monitor-de-sistemas/
├── main.py          # ponto de entrada da aplicação
├── utils.py         # interface gráfica e atualização das métricas
├── info_sistema.py  # coleta das informações do sistema
└── README.md
```

## Como executar

Clone o repositório:

```bash
git clone https://github.com/Bryan9895/Monitor-de-sistemas.git
cd Monitor-de-sistemas
```

Instale a dependência principal:

```bash
pip install psutil
```

No Ubuntu/Debian, caso o Tkinter não esteja instalado:

```bash
sudo apt install python3-tk
```

Execute:

```bash
python3 main.py
```

## Observações

A leitura de temperatura depende do suporte oferecido pelo sistema operacional e pelos sensores do hardware. Em equipamentos onde essa informação não está disponível, a aplicação continua funcionando sem exibir a temperatura.

A visualização detalhada do uso por núcleo já possui a coleta implementada e ainda pode ser aprimorada na interface.

## Objetivo do projeto

O projeto foi criado como exercício prático de desenvolvimento desktop e monitoramento de hardware, aplicando organização modular em Python, atualização periódica de interface e integração com informações fornecidas pelo sistema operacional.
