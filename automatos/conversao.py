from automatos.afd import AFD
from automatos.afn import AFN

def converter_afn_para_afd(afn: AFN) -> AFD:
    """
    Converte um AFN (Autômato Finito Não-determinístico) em um AFD (Autômato Finito Determinístico).

    Args:
        afn (AFN): O autômato finito não-determinístico a ser convertido.

    Returns:
        AFD: O autômato finito determinístico resultante da conversão.
    """
    estados_dfa = set()
    transicoes_dfa = {}
    estados_aceitacao_dfa = set()

    estados_para_processar = [frozenset([afn.estado_inicial])]
    estados_dfa.add(frozenset([afn.estado_inicial]))

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

    return AFD(
        estados_dfa,
        afn.alfabeto,
        transicoes_dfa,
        frozenset([afn.estado_inicial]),
        estados_aceitacao_dfa
    )

def estado_para_string(estado):
    """
    Converte um estado (possivelmente um frozenset) em uma string legível.

    Args:
        estado: O estado a ser convertido.

    Returns:
        str: A representação em string do estado.
    """
    if isinstance(estado, frozenset):
        return '{' + ', '.join(sorted(estado_para_string(sub_estado) for sub_estado in estado)) + '}'
    return str(estado)

def converter_estados_legiveis(afd):
    """
    Converte os estados de um AFD para uma representação legível.

    Args:
        afd (AFD): O autômato finito determinístico a ser convertido.

    Returns:
        AFD: O autômato com estados convertidos para strings legíveis.
    """
    afd.estados = [estado_para_string(s) for s in afd.estados]
    afd.transicoes = {(estado_para_string(k[0]), k[1]): estado_para_string(v) for k, v in afd.transicoes.items()}
    afd.estado_inicial = estado_para_string(afd.estado_inicial)
    afd.estados_aceitacao = [estado_para_string(s) for s in afd.estados_aceitacao]
    return afd
