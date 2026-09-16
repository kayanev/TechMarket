from flask import Flask, render_template, request
from classeproduto import * 
from usuario import *
from carrinho import *

app = Flask(__name__)

usuario_admin_padrao = Usuario(1, "admin", "admin@techmarket.com", "admin", "administrador")

lista_produtos_memoria = [ Produto(3,"Queijo","Laticínios",22.0),
    Produto(6,"Café Torrado e Moído",24.0),
    Produto(2, "Laranja-pêra",6.0)
    ]

carrinho_atual = CarrinhoCompras()

@app.route("/loja", methods=["GET"])
def exibir_loja():
    return render_template("loja.html", lista_produtos=lista_produtos_memoria)

@app.route("/adicionar\_carrinho", methods=["POST"]) 
def adicionar_ao_carrinho():
    id_prod = request.form.get("id_produto,")
    qtd_str = request.form.get("quantidade", "1")
    msg = ""
    try:
        id_num = int(id_prod)
        qtd = int(qtd_str)

        produto_encontrado = None 
        
        for p in lista_produtos_memoria: 
            if p.id_produto == id_num: produto_encontrado = p 
            break

        if produto_encontrado and produto_encontrado.quantidade_estoque >= qtd:
            carrinho_atual.adicionar_item(produto_encontrado, qtd)
            msg = f"'{produto_encontrado.nome}' adicionado ao carrinho!" 
        
        else: msg = "Erro: Quantidade solicitada indisponível no estoque!"

    except ValueError:
        msg = "Erro: Dados inválidos."

    return render_template("loja.html", lista_produtos=lista_produtos_memoria, mensagem=msg)

def main():
    usuario_admin_padrao = Usuario("01", "admin", "admin@gmail.com","admin", "Administrador")

    print("=== TELA DE LOGIN ===")
    usuario_informado = input("Insira seu usuario para autenticação: ")
    senha_informada = input("Digite sua senha para autenticação: ")

    if usuario_informado == usuario_admin_padrao.nome and usuario_admin_padrao.autenticar(senha_informada): 
        print(" Login efetuado com sucesso!") 
    else: 
        print(" Usuário ou senha incorretos.")

    usuario_admin_padrao.alterar_senha("baleia")
    print(usuario_admin_padrao.obter_dados_perfil())

if __name__ == "__main__": 
    app.run(debug=True)

