class Produto:
    def __init__(self, id, nome, preco, quantidade):
        self.id = id
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def __str__(self):
        return f"{self.nome} (R${self.preco}) - {self.quantidade} unidades"
    
class Node:
    def __init__(self, produto):
        self.produto = produto
        self.proximo = None

class ListaEncadeadaProdutos:
    def __init__(self):
        self.cabeca = None
    
    def adicionar(self, id, nome, preco, quantidade):
        novo_produto = Produto(id, nome, preco, quantidade)
        novo_no = Node(novo_produto)

        if self.cabeca == None:
            self.cabeca = novo_no
            return
        
        atual = self.cabeca
        while atual.proximo:
            atual = atual.proximo
        atual.proximo = novo_no

    def buscar_id(self, id):
        atual = self.cabeca
        while atual:
            if atual.produto.id == id:
                return atual.produto
            atual = atual.proximo
            return None
        
    def exibir_valor_estoque(self):
        atual = self.cabeca
        total = 0

        print('== ESTOQUE ==')
        while atual:
            produto = atual.produto
            print(f"{produto.id}: {produto}")
            total += produto.preco * produto.quantidade
            atual = atual.proximo
        print(f"Valor total em estoque: R${total:.2f}")

estoque = ListaEncadeadaProdutos()

estoque.adicionar(1, "Notebook", 2500.00, 5)
estoque.adicionar(2, "Mouse", 50.00, 20)
estoque.adicionar(3, "Teclado", 120.00, 15)
estoque.adicionar(4, "PlayStation5", 120.00, 30)

estoque.exibir_valor_estoque()