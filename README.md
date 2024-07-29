
# Projeto de Autômatos Finitos

## Descrição
Este projeto implementa uma aplicação web para trabalhar com Autômatos Finitos Determinísticos (AFD) e Autômatos Finitos Não-determinísticos (AFN). A aplicação permite:
- Inserir e visualizar AFNs e AFDs.
- Converter AFNs para AFDs.
- Simular a aceitação de palavras em AFNs e AFDs.
- Demonstrar a equivalência entre AFNs e AFDs convertidos.
- Minimizar AFDs.

## Requisitos

### Dependências
Certifique-se de ter o Python 3 instalado. As dependências do projeto podem ser instaladas usando `pip`:

```sh
pip install flask graphviz
```

### Instalação do Graphviz
Além da biblioteca `graphviz` do Python, é necessário instalar o software Graphviz no seu sistema.

- **Windows**: Baixe o instalador em https://graphviz.org/download/ e siga as instruções de instalação.
- **Linux**: Use o gerenciador de pacotes da sua distribuição. Por exemplo, no Debian/Ubuntu, use:
  ```sh
  sudo apt-get install graphviz
  ```

## Executando a Aplicação

1. **Clone o repositório**:
   ```sh
   git clone https://github.com/eduardohso/projetoAutomatos-teoriaDaComputacao.git
   cd projetoAutomatos-teoriaDaComputacao
   ```

2. **Inicie a aplicação**:
   ```sh
   python app.py
   ```

3. **Acesse a aplicação**:
   Abra seu navegador e vá para `http://127.0.0.1:5000`.

## Formatação dos Dados de Entrada

### Formato do AFN
Os dados para inserir um AFN devem seguir o formato abaixo:

- **Estados**: Lista de estados separados por vírgula.
- **Alfabeto**: Lista de símbolos do alfabeto separados por vírgula.
- **Transições**: Lista de transições no formato `estado,símbolo,destino`, separadas por ponto e vírgula.
- **Estado Inicial**: O estado inicial.
- **Estados de Aceitação**: Lista de estados de aceitação separados por vírgula.
- **Palavras**: Lista de palavras a serem testadas, separadas por vírgula.

#### Exemplo:
```
Estados: q0, q1, q2
Alfabeto: a, b
Transições: q0,a,q1; q1,b,q2; q2,a,q0
Estado Inicial: q0
Estados de Aceitação: q2
Palavras: a, ab, aba
```

### Formato do AFD
Os dados para inserir um AFD devem seguir o formato abaixo:

- **Estados**: Lista de estados separados por vírgula.
- **Alfabeto**: Lista de símbolos do alfabeto separados por vírgula.
- **Transições**: Lista de transições no formato `estado,símbolo,destino`, separadas por ponto e vírgula.
- **Estado Inicial**: O estado inicial.
- **Estados de Aceitação**: Lista de estados de aceitação separados por vírgula.
- **Palavras**: Lista de palavras a serem testadas, separadas por vírgula.

#### Exemplo:
```
Estados: q0, q1, q2
Alfabeto: a, b
Transições: q0,a,q1; q1,b,q2; q2,a,q0
Estado Inicial: q0
Estados de Aceitação: q2
Palavras: a, ab, aba
```

## Estrutura do Projeto

```
projetoAutomatos-teoriaDaComputacao/
│
├── app.py               # Arquivo principal da aplicação Flask
│
├── automatos/
│   ├── __init__.py       # Inicializa o módulo automatos
│   ├── afd.py            # Define a classe e métodos do AFD
│   ├── afn.py            # Define a classe e métodos do AFN
│   ├── conversao.py      # Contém a lógica de conversão de AFN para AFD
│   ├── entrada.py        # Processa os dados de entrada para AFN e AFD
│   ├── equivalencia.py   # Verifica a equivalência entre AFN e AFD
│   ├── minimizar.py      # Contém a lógica para minimizar o AFD
│   ├── simulacao.py      # Simula a aceitação de palavras em AFN e AFD
│   └── visualizar.py     # Simula a aceitação de palavras em AFN e AFD
│
├── templates/
│   ├── index.html         # Página principal da aplicação
│   ├── resultado.html     # Página de resultados para AFN
│   └── resultado_afd.html # Página de resultados para AFD
│
├── static/
│   ├── css/
│   │   └── style.css    # Estilos da aplicação
│   │
│   └── visualizacao/
│       ├── afn.png      # Visualização do AFN gerada
│       ├── afd.png      # Visualização do AFD gerada
│       └── afd_minimizado.png # Visualização do AFD minimizado gerada
│
└── README.md                  # Este arquivo
```

## Uso
1. **Insira os dados do autômato**: Preencha o formulário na página principal com os dados do AFN ou AFD.
2. **Processar**: Clique no botão para processar os dados e visualizar os resultados.
3. **Resultados**: Veja os resultados na página de resultados, incluindo visualizações dos autômatos e simulações das palavras.
