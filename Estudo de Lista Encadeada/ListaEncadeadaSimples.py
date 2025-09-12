#Estudo de Algoritmo e estrutura de dados com a criação de um programa com complexidade O(1)
#Classes e funções necessárias para a criação e manipulação de uma lista encadeada simples

class Node:
    def __init__(self,valor):
        self.valor = valor #Armazena o Valor do nó
        self.proximo = None #Ponteiro para o próximo nó (inicialmente vazio)

class ListaEncadeada:
    def __init__(self):
        self.cabeca = None # A lista começa vazia (cabeça = None)

    def inserir_inicio(self, valor):
        """Insere valor ao início da lista encadeada"""
        novo_no = Node(valor) #1.Cria um novo nó
        novo_no.proximo = self.cabeca #2.Novo nó aponta para a antiga cabeça
        self.cabeca = novo_no #3.Novo nó assume função de cabeça
    
    def inserir_final(self, valor):
        novo_no = Node(valor)

        if self.cabeca is None: #Se a lista estiver vazia
            self.cabeca = novo_no #Novo nó vira cabeça
            return
        
        atual = self.cabeca #Começa pela cabeça
        while atual.proximo:
            atual = atual.proximo #Percorre até o último nó
        atual.proximo = novo_no #Último nó aponta para o novo

    def remover(self, valor):
        """Remove um nó com um valor especificado"""
        if self.cabeca is None :
            return False
        
        # Caso especial: remover a cabeça
        if self.cabeca.valor == valor: #Se o elemento a ser retirado for a cabeça
            self.cabeca = self.cabeca.proximo #Transforma o elemento após a cabeça 
        
        atual = self.cabeca
        while atual.proximo:     #Percorre a lista
            if atual.proximo.valor == valor:  #Encontrou o valor
                atual.proximo = atual.proximo.proximo  # "Pula" o nó
                return True
            atual = atual.proximo

        return False #Valor não encontrado
    
    def buscar(self, valor):
        """Busca um valor na lista"""
        atual = self.cabeca 
        while atual:
            if atual.valor == valor: #Encontrou o valor
                return True
            atual = atual.proximo #Se não vai para o próximo (como se houvesse um 'else' implícito)
        return False # Percorreu tudo e não encontrou

    def exibir(self):
        """Exibe a lista por completo"""
        elementos = [] #Lista para armazenar os elementos de cada nó
        atual = self.cabeca
        while atual:
            elementos.append(str(atual.valor)) #Adiciona valor à lista
            atual = atual.proximo 
        return ' -> '.join(elementos) + ' -> None'  #Formata a saída

    def tamanho(self):
        """Retorn o temanho da lista"""
        contador = 0
        atual = self.cabeca
        while atual:
            contador += 1 #Incrementa contador
            atual = atual.proximo
        return contador #Retorna total de nós