class AFN:
    def __init__(self, estados, alfabeto, transicoes, estado_inicial, estados_aceitacao):
        self.estados = estados
        self.alfabeto = alfabeto
        self.transicoes = transicoes
        self.estado_inicial = estado_inicial
        self.estados_aceitacao = estados_aceitacao

    def to_dict(self):
        return {
            'estados': self.estados,
            'alfabeto': self.alfabeto,
            'transicoes': {str(k): list(v) for k, v in self.transicoes.items()},
            'estado_inicial': self.estado_inicial,
            'estados_aceitacao': self.estados_aceitacao
        }

    def __str__(self):
        return f"AFN(estados={self.estados}, alfabeto={self.alfabeto}, transicoes={self.transicoes}, estado_inicial={self.estado_inicial}, estados_aceitacao={self.estados_aceitacao})"
