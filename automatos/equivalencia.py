from automatos.simulacao import simular_afn, simular_afd

def verificar_equivalencia(afn, afd, palavras):
    """
    Verifica a equivalência entre um AFN e um AFD para um conjunto de palavras fornecidas.

    Args:
        afn (AFN): Autômato Finito Não-determinístico.
        afd (AFD): Autômato Finito Determinístico.
        palavras (list): Lista de palavras a serem testadas.

    Returns:
         - Retorna True e None se são equivalentes,
               ou False e a palavra que causou a diferença.
    """
    for palavra in palavras:
        aceita_afn = simular_afn(afn, palavra)
        aceita_afd = simular_afd(afd, palavra)
        if aceita_afn != aceita_afd:
            return False, palavra  # Retorna False e a palavra que causa a diferença
    return True, None
