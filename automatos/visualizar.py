from graphviz import Digraph

def format_state(state):
    
    # Formata o estado para uma string legível.
    if isinstance(state, frozenset):
        return "{" + ", ".join(sorted(format_state(s) for s in state)) + "}"
    return str(state)

def visualizar_automato(automato, nome_arquivo):
    
    # Gera uma visualização de um autômato (AFN) e salva como um arquivo PNG.
    dot = Digraph()

    # Adicionar estados
    for estado in automato.estados:
        estado_formatado = format_state(estado)
        if estado in automato.estados_aceitacao:
            dot.node(estado_formatado, shape='doublecircle')
        else:
            dot.node(estado_formatado, shape='circle')

    # Adicionar transições
    for (origem, simbolo), destinos in automato.transicoes.items():
        origem_formatado = format_state(origem)
        for destino in destinos:
            destino_formatado = format_state(destino)
            dot.edge(origem_formatado, destino_formatado, label=simbolo)

    # Estado inicial
    dot.node('start', shape='none', height='0', width='0')
    dot.edge('start', format_state(automato.estado_inicial))

    # Salvar arquivo
    dot.render(nome_arquivo, format='png', cleanup=True)

def visualizar_afd(afd, filename):
    
    # Gera uma visualização de um AFD e salva como um arquivo PNG.
    dot = Digraph(comment='AFD')

    # Adicionar estados
    for estado in afd.estados:
        estado_formatado = format_state(estado)
        if estado in afd.estados_aceitacao:
            dot.node(estado_formatado, shape='doublecircle')
        else:
            dot.node(estado_formatado, shape='circle')

    # Adicionar transições
    for (origem, simbolo), destino in afd.transicoes.items():
        origem_formatado = format_state(origem)
        destino_formatado = format_state(destino)
        dot.edge(origem_formatado, destino_formatado, label=simbolo)

    # Estado inicial
    dot.node('start', shape='none', height='0', width='0')
    dot.edge('start', format_state(afd.estado_inicial))

    # Salvar arquivo
    dot.render(filename, format='png', cleanup=True)
