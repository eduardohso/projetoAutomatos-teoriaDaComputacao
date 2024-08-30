# automatos/__init__.py

# Importações comuns para facilitar o uso de submódulos
from .afd import AFD
from .afn import AFN
from .conversao import converter_afn_para_afd, converter_estados_legiveis, estado_para_string, completar_afd
from .simulacao import simular_afd, simular_afn
from .minimizacao import minimizar_afd
from .visualizar import visualizar_automato, visualizar_afd
from .entrada import receber_entrada_afn, receber_entrada_afd
from .equivalencia import verificar_equivalencia