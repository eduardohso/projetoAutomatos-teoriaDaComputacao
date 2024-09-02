from flask import Flask, render_template, request
from automatos import receber_entrada_afn, receber_entrada_afd, converter_afn_para_afd, simular_afn, simular_afd, verificar_equivalencia, minimizar_afd, visualizar_automato, visualizar_afd, AFN, AFD, converter_estados_legiveis, estado_para_string
from maquinaTuring import MaquinaTuringIncrementoBinario, MaquinaTuringLR

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/automatos')
def automatos():
    return render_template('automatos.html')

@app.route('/maquinaTuring')
def maquina_turing():
    return render_template('maquinaTuring.html')


@app.route('/processar_automato', methods=['POST'])
def processar_automato():
    tipo = request.form.get('tipo').lower()
    estados = [estado.strip() for estado in request.form.get('estados').split(',')]
    alfabeto = [simbolo.strip() for simbolo in request.form.get('alfabeto').split(',')]
    transicoes_brutas = [transicao.strip() for transicao in request.form.get('transicoes').split(';') if transicao.strip()]
    estado_inicial = request.form.get('estado_inicial').strip()
    estados_aceitacao = [estado.strip() for estado in request.form.get('estados_aceitacao').split(',')]
    palavras = [palavra.strip() for palavra in request.form.get('palavras').split(',')]

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

        visualizar_afd(afd, 'static/visualizacao/afd')
        visualizar_afd(afd_minimizado, 'static/visualizacao/afd_minimizado')

        return render_template('resultado_afd.html', afd=afd.to_dict(), resultados_afd=resultados_afd, afd_minimizado=afd_minimizado.to_dict())


@app.route('/processar_turing', methods=['POST'])
def processar_turing():
    tipo_problema = request.form.get('tipo_problema')
    estados = request.form['estados'].split(',')
    alfabeto_entrada = request.form['alfabeto_entrada'].split(',')
    alfabeto_fita = request.form['alfabeto_fita'].split(',')
    simbolo_vazio = request.form['simbolo_vazio']
    estado_inicial = request.form['estado_inicial']
    estados_finais = request.form['estados_finais'].split(',')
    transicoes_brutas = request.form['transicoes'].strip().split('\n')

    transicoes = {}
    for transicao in transicoes_brutas:
        partes = transicao.split('->')
        estado_simbolo = partes[0].strip()
        novo_estado_simbolo_direcao = partes[1].strip().split(',')
        transicoes[estado_simbolo] = (novo_estado_simbolo_direcao[0].strip(), 
                                      novo_estado_simbolo_direcao[1].strip(), 
                                      novo_estado_simbolo_direcao[2].strip())

    palavra_entrada = request.form['palavra_entrada']

    if tipo_problema == 'incremento_binario':
        mt = MaquinaTuringIncrementoBinario(estados, alfabeto_entrada, alfabeto_fita, simbolo_vazio, transicoes, estado_inicial, estados_finais)
        resultado, palavra_resultado = mt.executar(palavra_entrada)
        return render_template('maquinaTuring.html', resultado=resultado, palavra_resultado=palavra_resultado)
    
    elif tipo_problema == 'linguagem_par_a':
        mt = MaquinaTuringLR(estados, alfabeto_entrada, alfabeto_fita, simbolo_vazio, transicoes, estado_inicial, estados_finais)
        resultado, _ = mt.executar(palavra_entrada)
        return render_template('maquinaTuring.html', resultado=resultado)

if __name__ == "__main__":
    app.run(debug=True)
