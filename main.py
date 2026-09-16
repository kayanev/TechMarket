# Atalho no VS Code: Ctrl+Shift+B roda o Flask com debug (uv run flask --app main run --debug)

from flask import Flask, render_template

app = Flask(__name__)

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, template_folder='templates')

class Produto:
    def __init__(self, nome, categoria, preco, quantidade):
        self.nome = nome
        self.categoria = categoria
        self.preco = float(preco)
        self.quantidade = int(quantidade)

produtos_db = []

@app.route('/')
@app.route('/estoque')
def renderizar_cadastro():
    produtos_com_index = list(enumerate(produtos_db))
    return render_template('estoque.html', produtos=produtos_com_index)

@app.route('/estoque', methods=['POST'])
def cadastrar_produto():
    nome = request.form.get('nome')
    categoria = request.form.get('categoria')
    preco = request.form.get('preco')
    qtd = request.form.get('qtd')

    novo_produto = Produto(nome, categoria, preco, qtd)
    produtos_db.append(novo_produto)

    return redirect(url_for('renderizar_cadastro'))

@app.route('/alterar-estoque', methods=['POST'])
def alterar_estoque():
    index = int(request.form.get('index'))
    nova_qtd = int(request.form.get('qtd'))

    if 0 <= index < len(produtos_db):
        produtos_db[index].quantidade = nova_qtd

    return redirect(url_for('renderizar_cadastro'))

@app.route('/remover-produto', methods=['POST'])
def remover_produto():
    index = int(request.form.get('index'))

    if 0 <= index < len(produtos_db):
        produtos_db.pop(index)

    return redirect(url_for('renderizar_cadastro'))

if __name__ == '__main__':
    app.run(debug=True)

@app.route("/", methods=["GET"])
def home():
    """Renderiza a pagina principal."""
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
