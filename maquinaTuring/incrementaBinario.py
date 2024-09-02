class MaquinaTuringIncrementoBinario:
    def __init__(self, estados, alfabetoEntrada, alfabetoFita, simboloBranco, transicoes, estadoInicial, estadosFinais):
        self.estados = estados
        self.alfabetoEntrada = alfabetoEntrada
        self.alfabetoFita = alfabetoFita
        self.simboloBranco = simboloBranco
        self.transicoes = transicoes
        self.estadoInicial = estadoInicial
        self.estadosFinais = estadosFinais
        self.fita = []
        self.estadoAtual = self.estadoInicial
        self.posicaoCabeca = 0

    def inicializarFita(self, palavraEntrada):
        self.fita = list(palavraEntrada) + [self.simboloBranco] * (len(palavraEntrada) + 1)
        self.posicaoCabeca = len(palavraEntrada) - 1  # Começa do bit mais à direita

    def expandirFitaSeNecessario(self):
        if self.posicaoCabeca == len(self.fita):
            self.fita.append(self.simboloBranco)
        elif self.posicaoCabeca < 0:
            self.fita.insert(0, self.simboloBranco)
            self.posicaoCabeca = 0

    def passo(self):
        simboloAtual = self.fita[self.posicaoCabeca]
        chaveTransicao = f'{self.estadoAtual},{simboloAtual}'
        if chaveTransicao in self.transicoes:
            proximoEstado, simboloEscrito, direcao = self.transicoes[chaveTransicao]
            self.fita[self.posicaoCabeca] = simboloEscrito
            self.estadoAtual = proximoEstado
            self.moverCabeca(direcao)
            self.expandirFitaSeNecessario()
        else:
            self.estadoAtual = None

    def moverCabeca(self, direcao):
        if direcao == '>':
            self.posicaoCabeca += 1
        elif direcao == '<':
            self.posicaoCabeca -= 1
            if self.posicaoCabeca < 0:
                self.posicaoCabeca = 0

    def executar(self, palavraEntrada):
        self.inicializarFita(palavraEntrada)
        while self.estadoAtual is not None and self.estadoAtual not in self.estadosFinais:
            self.passo()

        if self.estadoAtual in self.estadosFinais:
            palavraResultado = ''.join(self.fita).rstrip(self.simboloBranco)
            return "Sim", palavraResultado
        else:
            return "Não", None
