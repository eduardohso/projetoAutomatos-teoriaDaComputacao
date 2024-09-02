def simular_afn(afn, palavra):

    # Simula a execução de um AFN em uma palavra fornecida.
    estados_atuais = {afn.estado_inicial}
    for simbolo in palavra:
        proximos_estados = set()
        for estado in estados_atuais:
            proximos_estados.update(afn.transicoes.get((estado, simbolo), []))
        estados_atuais = proximos_estados
    return bool(estados_atuais & afn.estados_aceitacao)

def simular_afd(afd, palavra):
    
    # Simula a execução de um AFD em uma palavra fornecida.
    estado_atual = afd.estado_inicial
    for simbolo in palavra:
        estado_atual = afd.transicoes.get((estado_atual, simbolo))
        if estado_atual is None:
            return False
    return estado_atual in afd.estados_aceitacao
