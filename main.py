from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def menu():
    return render_template('Menu.html')


@app.route('/loja')
def loja():
    return "<h1>🛍️ Página da Loja</h1><p>Bem-vindo à loja!</p><br><a href='/'>Voltar ao Menu</a>"


@app.route('/estoque')
def estoque():
    return "<h1>📦 Página de Estoque</h1><p>Gerenciamento de produtos.</p><br><a href='/'>Voltar ao Menu</a>"

if __name__ == '__main__':
    app.run(debug=True, port=5000)