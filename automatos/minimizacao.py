from automatos import AFD
from automatos import completar_afd

def limpar_estado_neutro_completo(afd: AFD) -> AFD:
    """
    Remove todas as referências ao estado_neutro de um AFD, garantindo limpeza completa.
    
    Args:
        afd (AFD): O AFD a ser limpo.
    
    Returns:
        AFD: O AFD sem o estado_neutro.
    """
    estado_neutro = "estado_neutro"
    
    # Remover o estado_neutro do conjunto de estados
    afd.estados.discard(estado_neutro)
    
    # Remover transições associadas ao estado_neutro
    afd.transicoes = {k: v for k, v in afd.transicoes.items() if v != estado_neutro and k[0] != estado_neutro}
    
    # Remover estados que contenham o estado_neutro
    afd.estados = {estado for estado in afd.estados if estado_neutro not in estado}
    
    # Garantir que o estado_neutro não esteja nos estados de aceitação
    afd.estados_aceitacao = {s for s in afd.estados_aceitacao if s != estado_neutro}
    
    return afd

def particionar_estados(afd: AFD, estado_neutro: str) -> list:
    """
    Particiona os estados do AFD em dois conjuntos: aceitação e não aceitação, removendo o estado_neutro.
    
    Args:
        afd (AFD): O AFD a ser particionado.
        estado_neutro (str): O estado neutro a ser removido das partições.
    
    Returns:
        list: Lista de partições sem o estado_neutro.
    """
    P = [afd.estados_aceitacao, afd.estados - afd.estados_aceitacao]
    return [p - {estado_neutro} for p in P]

def minimizar_afd(afd: AFD) -> AFD:
    """
    Minimiza o AFD dado usando o algoritmo de minimização de estados.

    Args:
        afd (AFD): O AFD a ser minimizado.

    Returns:
        AFD: O AFD minimizado.
    """
    estado_neutro = "estado_neutro"
    
    # Completa o AFD se necessário
    if not afd.esta_normalizado():
        afd = completar_afd(afd)
    
    # Particiona os estados, excluindo o estado_neutro
    P = particionar_estados(afd, estado_neutro)
    W = [afd.estados_aceitacao.copy()]

    # Processo de minimização
    while W:
        A = W.pop()
        for simbolo in afd.alfabeto:
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

    # Remover todas as referências ao estado_neutro antes de criar o AFD minimizado
    afd = limpar_estado_neutro_completo(afd)
    
    # Criar os estados e transições minimizadas
    estados_minimizados = {frozenset(g) for g in P}
    estado_inicial_minimizado = next(frozenset(g) for g in estados_minimizados if afd.estado_inicial in g)
    estados_aceitacao_minimizados = {frozenset(g) for g in estados_minimizados if g & afd.estados_aceitacao}

    transicoes_minimizadas = {}
    for grupo in estados_minimizados:
        for estado in grupo:
            for simbolo in afd.alfabeto:
                estado_destino = afd.transicoes.get((estado, simbolo))
                if estado_destino and estado_destino != estado_neutro:
                    for g in estados_minimizados:
                        if estado_destino in g:
                            transicoes_minimizadas[(grupo, simbolo)] = g
                            break

    # Cria o AFD minimizado
    afd_minimizado = AFD(
        estados=estados_minimizados,
        alfabeto=afd.alfabeto,
        transicoes=transicoes_minimizadas,
        estado_inicial=estado_inicial_minimizado,
        estados_aceitacao=estados_aceitacao_minimizados
    )
    
    # Aplicar limpeza final ao AFD minimizado
    return limpar_estado_neutro_completo(afd_minimizado)
