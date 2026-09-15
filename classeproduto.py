# Autor: Adrian Jacob
class Produto:
    def __init__(self, nome, preco, quantidade, categoria):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
        self.categoria = categoria

    def adicionar_estoque(self, quantidade):
        self.quantidade += quantidade

    def remover_estoque(self, quantidade):
        if quantidade <= self.quantidade:
            self.quantidade -= quantidade
        else:
            print("Quantidade insuficiente em estoque.")

    def __str__(self):
        return f"Produto: {self.nome} | Preço: R${self.preco:.2f} | Quantidade: {self.quantidade} | Categoria: {self.categoria}"

estoque = []

while True:
    print("\n=== MEU CARRINHO ===")
    print("1 - Adicionar Novo Produto")
    print("2 - Remover Produto")
    print("3 - Listar Produtos")
    print("0 - Sair")
    
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("\nNome do produto: ")
        preco = float(input("Preço: R$ "))
        qtd = int(input("Quantidade inicial: "))
        categoria = input("Categoria: ")
        
        novo_produto = Produto(nome, preco, qtd, categoria)
        estoque.append(novo_produto)
        print(f"'{nome}' cadastrado com sucesso!")

    elif opcao == "2":
        nome_busca = input("\nDigite o nome do produto que deseja remover: ")
        encontrado = False

        for prod in estoque:
            if prod.nome.lower() == nome_busca.lower():
                estoque.remove(prod)
                print(f"Produto '{prod.nome}' removido do sistema!")
                encontrado = True
                break
        
        if not encontrado:
            print("Produto não encontrado.")

    elif opcao == "3":
        print("\n--- LISTA DE PRODUTOS ---")
        if not estoque:
            print("Nenhum produto cadastrado.")
        else:
            for p in estoque:
                print(p)

    elif opcao == "0":
        print("\nSaindo do programa...")
        break

    else:
        print("Opção inválida! Tente novamente.")
