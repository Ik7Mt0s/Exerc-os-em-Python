import ListaEncadeadaSimples

# Criando a lista encadeada
lista = ListaEncadeadaSimples.ListaEncadeada()

# Inserindo elementos
lista.inserir_final(10)
lista.inserir_final(20)
lista.inserir_inicio(5)
lista.inserir_final(30)

print("Lista:", lista.exibir())  # 5 -> 10 -> 20 -> 30 -> None
print("Tamanho:", lista.tamanho())  # 4

# Buscando elementos
print("Buscar 20:", lista.buscar(20))  # True
print("Buscar 99:", lista.buscar(99))  # False

# Removendo elementos
lista.remover(20)
print("Após remover 20:", lista.exibir())  # 5 -> 10 -> 30 -> None

lista.remover(5)
print("Após remover 5:", lista.exibir())  # 10 -> 30 -> None

'''
TERMINAL:
Lista: 5 -> 10 -> 20 -> 30 -> None
Tamanho: 4
Buscar 20: True
Buscar 99: False
Após remover 20: 5 -> 10 -> 30 -> None
Após remover 5: 10 -> 30 -> None
'''