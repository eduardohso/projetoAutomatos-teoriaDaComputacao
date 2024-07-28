from automatos.afn import AFN
from automatos.afd import AFD

def receber_entrada_afn(dados):
    """
    Recebe os dados de entrada e cria um AFN (Autômato Finito Não-determinístico).

    Args:
        dados (dict): Dicionário contendo os dados do AFN.

    Returns:
        AFN: O autômato finito não-determinístico criado a partir dos dados fornecidos.
    """
    estados = set(estado.strip() for estado in dados["estados"])
    alfabeto = set(simbolo.strip() for simbolo in dados["alfabeto"])
    transicoes = {(estado.strip(), simbolo.strip()): set(destino.strip() for destino in destinos)
                  for (estado, simbolo), destinos in dados["transicoes"].items()}
    estado_inicial = dados["estado_inicial"].strip()
    estados_aceitacao = set(estado.strip() for estado in dados["estados_aceitacao"])

    afn = AFN(estados, alfabeto, transicoes, estado_inicial, estados_aceitacao)
    return afn

def receber_entrada_afd(dados):
    """
    Recebe os dados de entrada e cria um AFD (Autômato Finito Determinístico).

    Args:
        dados (dict): Dicionário contendo os dados do AFD.

    Returns:
        AFD: O autômato finito determinístico criado a partir dos dados fornecidos.
    """
    estados = set(estado.strip() for estado in dados["estados"])
    alfabeto = set(simbolo.strip() for simbolo in dados["alfabeto"])
    transicoes = {(estado.strip(), simbolo.strip()): destino.strip() 
                  for (estado, simbolo), destino in dados["transicoes"].items()}
    estado_inicial = dados["estado_inicial"].strip()
    estados_aceitacao = set(estado.strip() for estado in dados["estados_aceitacao"])

    afd = AFD(estados, alfabeto, transicoes, estado_inicial, estados_aceitacao)
    return afd
