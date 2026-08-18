from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/boletim")
def boletim():
    return render_template('boletim.html')


@app.route("/validacao", methods=['GET', 'POST'])
def validacao():
    nome = request.form.get('nome', '')
    sobrenome = request.form.get('sobrenome', '')
    idade = request.form.get('idade', '')
    resultado = None

    if nome or sobrenome or idade:
        try:
            idade_num = int(idade)
        except (TypeError, ValueError):
            idade_num = None

        if idade_num is not None:
            resultado = {
                'nome': nome,
                'sobrenome': sobrenome,
                'idade': idade_num,
                'pode_votar': idade_num >= 16,
                'pode_dirigir': idade_num >= 18,
            }

    return render_template(
        'validacao.html',
        nome=nome,
        sobrenome=sobrenome,
        idade=idade,
        resultado=resultado
    )


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
