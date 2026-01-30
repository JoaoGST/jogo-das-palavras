from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'supersecreto123'


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        session['lista_jogadores'] = [n.strip().capitalize() for n in request.form.get('jogadores').split(',') if n.strip()]
        session['lista_palavras'] = []
        session['letra'] = ''
        session['indice_jogador'] = 0
        return redirect(url_for('jogo'))
    return render_template('index.html')


@app.route('/jogo', methods=['GET', 'POST'])
def jogo():
    if 'lista_jogadores' not in session or not session['lista_jogadores']:
        return redirect(url_for('index'))

    lista_palavras = session.get('lista_palavras', [])
    jogadores = session['lista_jogadores']
    letra = session.get('letra', '')
    indice = session.get('indice_jogador', 0)

    mensagem = ''

    if request.method == 'POST':
        # Escolha da letra no início
        if 'letra' in request.form and not letra:
            session['letra'] = request.form['letra'].upper()
            letra = session['letra']

        # Jogador digitando palavra
        elif 'palavra' in request.form:
            palavra = request.form['palavra'].capitalize()

            # Recupera jogador atual após possíveis mudanças na lista
            if not jogadores:
                final_lista = lista_palavras
                session.clear()
                return render_template('fim.html', lista=final_lista)

            jogador_atual = jogadores[indice]

            if palavra.lower() == 'desistir':
                nome_desistente = jogador_atual
                jogadores.pop(indice)
                session['lista_jogadores'] = jogadores
                mensagem = f'{nome_desistente} desistiu!'

                if not jogadores:
                    final_lista = lista_palavras
                    session.clear()
                    return render_template('fim.html', lista=final_lista)
                # Não incrementa índice, pois lista encurtou
                if indice >= len(jogadores):
                    indice = 0
                session['indice_jogador'] = indice

            elif not palavra.startswith(letra):
                mensagem = 'Palavra não começa com a letra da rodada! Tente novamente.'
                # índice permanece, mesmo jogador repete a vez

            elif palavra in lista_palavras:
                mensagem = 'Esta palavra já foi inserida. Tente novamente.'
                # índice permanece, mesmo jogador repete a vez

            else:
                lista_palavras.append(palavra)
                session['lista_palavras'] = lista_palavras
                mensagem = f'Palavra "{palavra}" adicionada!'
                # passa a vez para o próximo jogador
                indice = (indice + 1) % len(jogadores)
                session['indice_jogador'] = indice

    # Depois de processar POST, garante que jogador_atual esteja correto
    if jogadores:
        jogador_atual = jogadores[session.get('indice_jogador', 0)]
    else:
        jogador_atual = None

    return render_template('jogo.html', letra=letra, lista=lista_palavras,
                           mensagem=mensagem, jogador=jogador_atual)


@app.route('/nova_letra')
def nova_letra():
    session['lista_palavras'] = []
    session['indice_jogador'] = 0
    session['letra'] = ''
    return redirect(url_for('jogo'))


if __name__ == '__main__':
    app.run(debug=True)
