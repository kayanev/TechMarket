from flask import Flask, render_template, request, redirect, url_for
from models import Produto, CarrinhoCompras, Usuario

# Feito por Kayane Balielo
app = Flask(__name__)

lista_produtos_memoria = [
    Produto(1, "Queijo", "Laticínios", 22.00, 10),
    Produto(2, "Café Torrado e Moído", "Bebidas", 24.00, 5),
    Produto(3, "Laranja-pêra", "Hortifruti", 6.00, 20)
]

carrinho_atual = CarrinhoCompras()

@app.route("/loja", methods=["GET"])
def exibir_loja():
    return render_template("loja.html", lista_produtos=lista_produtos_memoria)

@app.route("/adicionar_carrinho", methods=["POST"])
def adicionar_ao_carrinho():
    id_prod = request.form.get("id_produto")
    qtd_str = request.form.get("quantidade", "1")
    msg = ""

    try:
        id_num = int(id_prod)
        qtd = int(qtd_str)

        produto_encontrado = next((p for p in lista_produtos_memoria if p.id_produto == id_num), None)

        if produto_encontrado and produto_encontrado.quantidade_estoque >= qtd:
            carrinho_atual.adicionar_item(produto_encontrado, qtd)
            msg = f"'{produto_encontrado.nome}' adicionado ao carrinho!"
        else:
            msg = "Erro: Quantidade solicitada indisponível no estoque!"

    except (ValueError, TypeError):
        msg = "Erro: Dados inválidos."

    return render_template("loja.html", lista_produtos=lista_produtos_memoria, mensagem=msg)

@app.route("/carrinho", methods=["GET"])
def exibir_carrinho():
    return render_template("carrinho.html", carrinho=carrinho_atual)

@app.route("/remover_carrinho", methods=["POST"])
def remover_do_carrinho():
    id_prod = request.form.get("id_produto", "")
    try:
        id_num = int(id_prod)
        if carrinho_atual.remover_item(id_num):
            msg = "Item removido com sucesso!"
        else:
            msg = "Erro ao remover item."
    except ValueError:
        msg = "ID de produto inválido."

    return render_template("carrinho.html", carrinho=carrinho_atual, mensagem=msg)

@app.route("/finalizar_compra", methods=["POST"])
def finalizar_compra():
    if carrinho_atual.finalizar_compra():
        msg = "Compra finalizada com sucesso! Estoque atualizado."
    else:
        msg = "Erro ao finalizar compra: estoque insuficiente ou carrinho vazio."

    return render_template("carrinho.html", carrinho=carrinho_atual, mensagem=msg)

if __name__ == "__main__":
    app.run(debug=True)
