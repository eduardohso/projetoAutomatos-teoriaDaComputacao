from automatos import AFD
from automatos import completar_afd

def limpar_estado_neutro_completo(afd: AFD) -> AFD:
    
    # Remove todas as referências ao estado_neutro de um AFD, garantindo limpeza completa.

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
    
    # Particiona os estados do AFD em dois conjuntos: aceitação e não aceitação, removendo o estado_neutro.
    P = [afd.estados_aceitacao, afd.estados - afd.estados_aceitacao]
    return [p - {estado_neutro} for p in P]

def minimizar_afd(afd: AFD) -> AFD:

    # Minimiza o AFD dado usando o algoritmo de minimização de estados.
    estadoNeutro = "estadoNeutro"
    
    # Completa o AFD se necessário
    if not afd.esta_normalizado():
        afd = completar_afd(afd)
    
    # Particiona os estados, excluindo o estadoNeutro
    gruposEstados = particionar_estados(afd, estadoNeutro)
    estadosProcessar = [afd.estados_aceitacao.copy()]

    # Processo de minimização
    while estadosProcessar:
        estadosAtuais = estadosProcessar.pop()
        for simbolo in afd.alfabeto:
            estadosAlvo = {estado for estado in afd.estados if afd.transicoes.get((estado, simbolo)) in estadosAtuais}
            for grupo in gruposEstados[:]:
                estadosComuns = estadosAlvo & grupo
                estadosRestantes = grupo - estadosAlvo
                if estadosComuns and estadosRestantes:
                    gruposEstados.remove(grupo)
                    gruposEstados.append(estadosComuns)
                    gruposEstados.append(estadosRestantes)
                    if grupo in estadosProcessar:
                        estadosProcessar.remove(grupo)
                        estadosProcessar.append(estadosComuns)
                        estadosProcessar.append(estadosRestantes)
                    else:
                        if len(estadosComuns) <= len(estadosRestantes):
                            estadosProcessar.append(estadosComuns)
                        else:
                            estadosProcessar.append(estadosRestantes)

    # Remover todas as referências ao estadoNeutro antes de criar o AFD minimizado
    afd = limpar_estado_neutro_completo(afd)
    
    # Criar os estados e transições minimizadas
    estadosMinimizados = {frozenset(grupo) for grupo in gruposEstados}
    estadoInicialMinimizado = next(frozenset(grupo) for grupo in estadosMinimizados if afd.estado_inicial in grupo)
    estadosAceitacaoMinimizados = {frozenset(grupo) for grupo in estadosMinimizados if grupo & afd.estados_aceitacao}

    transicoesMinimizadas = {}
    for grupo in estadosMinimizados:
        for estado in grupo:
            for simbolo in afd.alfabeto:
                estadoDestino = afd.transicoes.get((estado, simbolo))
                if estadoDestino and estadoDestino != estadoNeutro:
                    for grupoDestino in estadosMinimizados:
                        if estadoDestino in grupoDestino:
                            transicoesMinimizadas[(grupo, simbolo)] = grupoDestino
                            break

    # Cria o AFD minimizado
    afdMinimizado = AFD(
        estados=estadosMinimizados,
        alfabeto=afd.alfabeto,
        transicoes=transicoesMinimizadas,
        estado_inicial=estadoInicialMinimizado,
        estados_aceitacao=estadosAceitacaoMinimizados
    )
    
    # Aplicar limpeza final ao AFD minimizado
    return limpar_estado_neutro_completo(afdMinimizado)

