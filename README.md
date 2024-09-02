
# Projeto de Autômatos Finitos e Máquina de Turing

## Descrição
Este projeto implementa uma aplicação web para trabalhar com Autômatos Finitos Determinísticos (AFD), Autômatos Finitos Não-determinísticos (AFN), e uma Máquina de Turing. A aplicação permite:

- Inserir e visualizar AFNs e AFDs.
- Converter AFNs para AFDs.
- Simular a aceitação de palavras em AFNs e AFDs.
- Demonstrar a equivalência entre AFNs e AFDs convertidos.
- Minimizar AFDs.
- Simular operações em uma Máquina de Turing, incluindo incremento de números binários e reconhecimento de linguagem regular.


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
## Máquina de Turing
A Máquina de Turing implementada neste projeto é capaz de resolver problemas computacionais específicos, como:

- **Incremento de Número Binário**: Dado um número binário, a máquina incrementa seu valor em 1.
- **Reconhecimento de Linguagem Regular**: A máquina verifica se uma palavra de entrada pertence a uma linguagem regular específica, como palavras com um número par de 'a's.

### Formatação dos Dados de Entrada

- **Estados**: Lista de estados separados por vírgula.
- **Alfabeto de Entrada**: Lista de símbolos do alfabeto de entrada separados por vírgula.
- **Alfabeto da Fita**: Lista de símbolos do alfabeto da fita separados por vírgula.
- **Transições**: Lista de transições no formato `estado_atual,símbolo_lido -> novo_estado,símbolo_escrito,direção`, separadas por ponto e vírgula.
- **Estado Inicial**: O estado inicial.
- **Estados de Aceitação**: Lista de estados de aceitação separados por vírgula.
- **Símbolo Vazio**: Símbolo usado para representar espaços vazios na fita.
- **Palavra de Entrada**: A palavra que será processada pela Máquina de Turing.

### Exemplo:
Para o problema de incremento de número binário:

```
Estados: q0,q_aceita
Alfabeto de Entrada: 0, 1
Alfabeto da Fita: 0, 1, _
Transições: 
   q0,1 -> q0,0,<
   q0,0 -> q_aceita,1,N
   q0,_ -> q_aceita,1,N
Estado Inicial: q0
Estados de Aceitação: q_aceita
Símbolo Vazio: _
Palavra de Entrada: 011
```
## Implementação e Funcionamento
### Lógica do Incremento de Número Binário
- **Objetivo**: Simular uma operação de incremento binário usando uma Máquina de Turing.
- **Funcionamento**: A máquina percorre a palavra da direita para a esquerda, aplicando regras de transição que simulam a adição binária. Ao final, a palavra resultante é exibida como o número binário incrementado.

### Lógica de Reconhecimento de Linguagem Regular
- **Objetivo**: Verificar se a palavra de entrada possui um número par de 'a's.
- **Funcionamento**: A máquina percorre a fita, marcando os 'a's processados e, ao final, determina se o número total é par ou ímpar. A palavra é aceita ou rejeitada com base nessa contagem.

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
├── maquinaTuring/
│   ├── __init__.py            # Inicializa o módulo da Máquina de Turing
│   ├── incrementaBinario.py   # Implementa a função de incremento binário
│   ├── reconheceLR.py         # Implementa a função de reconhecimento de linguagem regular
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
├── templates/
│   ├── automatos.html         # Página para inserção e simulação de autômatos
│   ├── index.html             # Página principal da aplicação
│   ├── maquinaTuring.html     # Página para inserção e simulação da Máquina de Turing
│   ├── resultado_afd.html     # Página de resultados para AFD
│   └── resultado.html         # Página de resultados para AFN e AFD
│
│
└── README.md                  # Este arquivo
```

## Uso

1. **Insira os dados do autômato ou da Máquina de Turing**: Preencha o formulário na página principal com os dados do AFN, AFD ou Máquina de Turing.
2. **Processar**: Clique no botão correspondente para processar os dados e visualizar os resultados.
3. **Resultados**: Veja os resultados na página de resultados, incluindo visualizações dos autômatos, simulações das palavras.

