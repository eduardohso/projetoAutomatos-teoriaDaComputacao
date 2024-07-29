from automatos.afn import AFN
from automatos.afd import AFD

def completar_afd(afd: AFD) -> AFD:
    """
    Completa o AFD adicionando um estado neutro, se necessário, para garantir que todos os estados tenham transições definidas para cada símbolo do alfabeto.
    
    Args:
        afd (AFD): O AFD a ser completado.
    
    Returns:
        AFD: O AFD completado.
    """
    estado_neutro = 'estado_neutro'
    novos_estados = afd.estados | {estado_neutro}
    novas_transicoes = afd.transicoes.copy()

    # Adiciona transições para o estado neutro
    for estado in afd.estados:
        for simbolo in afd.alfabeto:
            if (estado, simbolo) not in novas_transicoes:
                novas_transicoes[(estado, simbolo)] = estado_neutro

    # Estado neutro transita para ele mesmo para qualquer símbolo
    for simbolo in afd.alfabeto:
        novas_transicoes[(estado_neutro, simbolo)] = estado_neutro

    return AFD(
        estados=novos_estados,
        alfabeto=afd.alfabeto,
        transicoes=novas_transicoes,
        estado_inicial=afd.estado_inicial,
        estados_aceitacao=afd.estados_aceitacao
    )

def converter_afn_para_afd(afn: AFN) -> AFD:
    """
    Converte um AFN para um AFD equivalente.
    
    Args:
        afn (AFN): O AFN a ser convertido.
    
    Returns:
        AFD: O AFD convertido.
    """
    estados_dfa = set()
    transicoes_dfa = {}
    estados_aceitacao_dfa = set()

    # Estado inicial do AFD é um conjunto contendo o estado inicial do AFN
    estados_para_processar = [frozenset([afn.estado_inicial])]
    estados_dfa.add(frozenset([afn.estado_inicial]))

    # Processa todos os estados
    while estados_para_processar:
        estado_atual = estados_para_processar.pop()

        for simbolo in afn.alfabeto:
            novo_estado = frozenset()
            for subestado in estado_atual:
                if (subestado, simbolo) in afn.transicoes:
                    novo_estado |= afn.transicoes[(subestado, simbolo)]

            if novo_estado:
                transicoes_dfa[(estado_atual, simbolo)] = novo_estado
                if novo_estado not in estados_dfa:
                    estados_dfa.add(novo_estado)
                    estados_para_processar.append(novo_estado)

                if novo_estado & afn.estados_aceitacao:
                    estados_aceitacao_dfa.add(novo_estado)

    afd = AFD(
        estados=estados_dfa,
        alfabeto=afn.alfabeto,
        transicoes=transicoes_dfa,
        estado_inicial=frozenset([afn.estado_inicial]),
        estados_aceitacao=estados_aceitacao_dfa
    )

    return completar_afd(afd)

def estado_para_string(estado):
    """
    Converte um estado em uma string legível.
    
    Args:
        estado: O estado a ser convertido, pode ser uma string ou um frozenset.
    
    Returns:
        str: O estado convertido em string.
    """
    if isinstance(estado, frozenset):
        return '{' + ', '.join(sorted(estado_para_string(sub_estado) for sub_estado in estado)) + '}'
    return str(estado)

def converter_estados_legiveis(afd):
    """
    Converte os estados e transições do AFD para strings legíveis.
    
    Args:
        afd (AFD): O AFD a ser convertido.
    
    Returns:
        AFD: O AFD com estados e transições convertidos para strings legíveis.
    """
    afd.estados = [estado_para_string(s) for s in afd.estados]
    afd.transicoes = {(estado_para_string(k[0]), k[1]): estado_para_string(v) for k, v in afd.transicoes.items()}
    afd.estado_inicial = estado_para_string(afd.estado_inicial)
    afd.estados_aceitacao = [estado_para_string(s) for s in afd.estados_aceitacao]
    return afd
