from automatos.afd import AFD

def minimizar_afd(afd):
    """
    Minimiza um autômato finito determinístico (AFD) usando o algoritmo de partição.

    Args:
        afd (AFD): O autômato finito determinístico a ser minimizado.

    Returns:
        AFD: O autômato finito determinístico minimizado.
    """
    # Inicializa as partições
    P = [afd.estados_aceitacao, afd.estados - afd.estados_aceitacao]
    W = [afd.estados_aceitacao.copy()]

    while W:
        A = W.pop()
        for simbolo in afd.alfabeto:
            # Conjunto de estados cujas transições com o símbolo atual levam a estados em A
            X = {estado for estado in afd.estados if afd.transicoes.get((estado, simbolo)) in A}
            for Y in P[:]:
                interseccao = X & Y
                diferenca = Y - X
                if interseccao and diferenca:
                    P.remove(Y)
                    P.append(interseccao)
                    P.append(diferenca)
                    if Y in W:
                        W.remove(Y)
                        W.append(interseccao)
                        W.append(diferenca)
                    else:
                        if len(interseccao) <= len(diferenca):
                            W.append(interseccao)
                        else:
                            W.append(diferenca)

    # Cria os novos estados minimizados
    estados_minimizados = {frozenset(g) for g in P}
    estado_inicial_minimizado = next(frozenset(g) for g in P if afd.estado_inicial in g)
    estados_aceitacao_minimizados = {frozenset(g) for g in P if g & afd.estados_aceitacao}

    # Cria as novas transições minimizadas
    transicoes_minimizadas = {}
    for grupo in estados_minimizados:
        for estado in grupo:
            for simbolo in afd.alfabeto:
                estado_destino = afd.transicoes.get((estado, simbolo))
                if estado_destino:
                    grupo_destino = next(frozenset(g) for g in P if estado_destino in g)
                    transicoes_minimizadas[(grupo, simbolo)] = grupo_destino

    return AFD(
        estados=estados_minimizados,
        alfabeto=afd.alfabeto,
        transicoes=transicoes_minimizadas,
        estado_inicial=estado_inicial_minimizado,
        estados_aceitacao=estados_aceitacao_minimizados
    )
