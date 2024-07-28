from flask import Flask, render_template, request
from automatos import receber_entrada_afn, receber_entrada_afd, converter_afn_para_afd, simular_afn, simular_afd, verificar_equivalencia, minimizar_afd, visualizar_automato, visualizar_afd, AFN, AFD, converter_estados_legiveis, estado_para_string

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')



@app.route('/processar', methods=['POST'])
def processar():
    tipo = request.form.get('tipo')
    estados = [estado.strip() for estado in request.form.get('estados').split(',')]
    alfabeto = [simbolo.strip() for simbolo in request.form.get('alfabeto').split(',')]
    transicoes_brutas = [transicao.strip() for transicao in request.form.get('transicoes').split(';') if transicao.strip()]
    estado_inicial = request.form.get('estado_inicial').strip()
    estados_aceitacao = [estado.strip() for estado in request.form.get('estados_aceitacao').split(',')]
    palavras = [palavra.strip() for palavra in request.form.get('palavras').split(',')]

    # Constrói o dicionário de transições
    transicoes = {}
    for transicao in transicoes_brutas:
        partes = transicao.split(',')
        if len(partes) < 3:
            continue
        estado_de = partes[0].strip()
        simbolo = partes[1].strip()
        estado_para = partes[2].strip()
        if tipo == 'afn':
            if (estado_de, simbolo) not in transicoes:
                transicoes[(estado_de, simbolo)] = set()
            transicoes[(estado_de, simbolo)].add(estado_para)
        else:
            transicoes[(estado_de, simbolo)] = estado_para

    if tipo == 'afn':
        afn = AFN(set(estados), set(alfabeto), transicoes, estado_inicial, set(estados_aceitacao))
        afd = converter_afn_para_afd(afn)
        resultados_afn = {palavra: simular_afn(afn, palavra) for palavra in palavras}
        resultados_afd = {palavra: simular_afd(afd, palavra) for palavra in palavras}
        equivalente, palavra_diferente = verificar_equivalencia(afn, afd, palavras)
        afd_minimizado = minimizar_afd(afd)

        afd = converter_estados_legiveis(afd)
        afd_minimizado = converter_estados_legiveis(afd_minimizado)

        # Visualizar os automatos
        visualizar_automato(afn, 'static/visualizacao/afn')
        visualizar_afd(afd, 'static/visualizacao/afd')
        visualizar_afd(afd_minimizado, 'static/visualizacao/afd_minimizado')

        return render_template('resultado.html', afn=afn.to_dict(), afd=afd.to_dict(), resultados_afn=resultados_afn,
                               resultados_afd=resultados_afd, equivalente=equivalente,
                               palavra_diferente=palavra_diferente, afd_minimizado=afd_minimizado.to_dict())
    else:
        afd = AFD(set(estados), set(alfabeto), transicoes, estado_inicial, set(estados_aceitacao))
        resultados_afd = {palavra: simular_afd(afd, palavra) for palavra in palavras}
        afd_minimizado = minimizar_afd(afd)

        afd = converter_estados_legiveis(afd)
        afd_minimizado = converter_estados_legiveis(afd_minimizado)

        # Visualizar os automatos
        visualizar_afd(afd, 'static/visualizacao/afd')
        visualizar_afd(afd_minimizado, 'static/visualizacao/afd_minimizado')

        return render_template('resultado_afd.html', afd=afd.to_dict(), resultados_afd=resultados_afd, afd_minimizado=afd_minimizado.to_dict())

if __name__ == '__main__':
    app.run(debug=True)
