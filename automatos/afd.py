class AFD:
    def esta_normalizado(self) -> bool:
        """
        Verifica se o AFD está normalizado. Um AFD está normalizado se todos os estados têm transições
        definidas para todos os símbolos do alfabeto.
        
        Returns:
            bool: True se o AFD estiver normalizado, False caso contrário.
        """
        for estado in self.estados:
            for simbolo in self.alfabeto:
                if (estado, simbolo) not in self.transicoes:
                    return False
        return True
    
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
            'transicoes': {str(k): v for k, v in self.transicoes.items()},
            'estado_inicial': self.estado_inicial,
            'estados_aceitacao': self.estados_aceitacao
        }

    def __str__(self):
        return f"AFD(estados={self.estados}, alfabeto={self.alfabeto}, transicoes={self.transicoes}, estado_inicial={self.estado_inicial}, estados_aceitacao={self.estados_aceitacao})"
