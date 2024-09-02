from automatos.simulacao import simular_afn, simular_afd

def verificar_equivalencia(afn, afd, palavras):

    # Verifica a equivalência entre um AFN e um AFD para um conjunto de palavras fornecidas.
    for palavra in palavras:
        aceita_afn = simular_afn(afn, palavra)
        aceita_afd = simular_afd(afd, palavra)
        if aceita_afn != aceita_afd:
            return False, palavra  # Retorna False e a palavra que causa a diferença
    return True, None
