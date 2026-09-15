
#Feito por Manuela Cardozo
class CarrinhoCompras:
    def __init__(self, itens, valor_total, status_compra):
        self.itens = []
        self.valor_total = valor_total
        self.status_compra = status_compra

    def adicionar_item(self, item):
        self.itens.append(item)

    def remover_item(self, item):
        if item in self.itens:
            self.itens.remove(item)

    def calcular_total(self):
        total = sum(item.preco for item in self.itens)
        return total

    def listar_itens(self):
        return [item.nome for item in self.itens]
    
    def finalizar_compra(self):
        if self.status_compra == "aberta":
            self.status_compra = "finalizada"
            return "Compra finalizada com sucesso!"
        else:
            return "A compra já foi finalizada."

