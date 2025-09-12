class No:
    """Classe que representa um nó (criança) na lista circular"""
    def __init__(self, nome):
        self.nome = nome
        self.proximo = None

class ListaCircular:
    """Classe que representa a lista circular simples usando apenas cauda"""
    
    def __init__(self):
        self.cauda = None
        self.tamanho = 0
    
    def esta_vazia(self):
        """Verifica se a lista está vazia"""
        return self.cauda is None
    
    def adicionar(self, nome):
        """Adiciona uma nova criança ao círculo"""
        novo_no = No(nome)
        
        if self.esta_vazia():
            self.cauda = novo_no
            novo_no.proximo = self.cauda  # Aponta para si mesmo
        else:
            novo_no.proximo = self.cauda.proximo  # Novo nó aponta para o primeiro
            self.cauda.proximo = novo_no  # Último nó aponta para o novo
            self.cauda = novo_no  # Novo nó se torna a nova cauda
        
        self.tamanho += 1
    
    def obter_primeiro(self):
        """Retorna o primeiro nó da lista circular"""
        if self.esta_vazia():
            return None
        return self.cauda.proximo
    
    def remover(self, no_anterior):
        """Remove o nó seguinte ao nó fornecido"""
        if self.esta_vazia():
            return None
        
        no_remover = no_anterior.proximo
        
        # Caso especial: remover o único nó restante
        if no_remover == no_anterior:
            self.cauda = None
        else:
            no_anterior.proximo = no_remover.proximo
            # Se estivermos removendo a cauda, atualizamos a cauda
            if no_remover == self.cauda:
                self.cauda = no_anterior
        
        self.tamanho -= 1
        return no_remover.nome
    
    def __str__(self):
        """Representação em string da lista circular"""
        if self.esta_vazia():
            return "Círculo vazio"
        
        elementos = []
        primeiro = self.cauda.proximo
        atual = primeiro
        
        while True:
            elementos.append(atual.nome)
            atual = atual.proximo
            if atual == primeiro:
                break
        
        return " -> ".join(elementos) + " -> ..."

def batata_quente(criancas, passes):
    """
    Simula o jogo da batata quente
    
    Args:
        criancas: lista com os nomes das crianças
        passes: número de passes antes de eliminar uma criança
    
    Returns:
        tuple: (vencedor, ordem_eliminacao)
    """
    if not criancas:
        return None, []
    
    if passes < 1:
        raise ValueError("O número de passes deve ser pelo menos 1")
    
    # Cria a lista circular com as crianças
    circulo = ListaCircular()
    for crianca in criancas:
        circulo.adicionar(crianca)
    
    ordem_eliminacao = []
    
    # Começa com o primeiro nó (o que a cauda aponta)
    atual = circulo.obter_primeiro()
    
    # Encontra o nó anterior ao atual para facilitar a remoção
    anterior = circulo.cauda  # A cauda é anterior ao primeiro nó
    
    # Simula o jogo até restar apenas uma criança
    while circulo.tamanho > 1:
        # Passa a batata M vezes
        for _ in range(passes):
            anterior = atual
            atual = atual.proximo
        
        # Remove a criança que está com a batata
        eliminada = circulo.remover(anterior)
        ordem_eliminacao.append(eliminada)
        
        # Atualiza o ponteiro atual para a próxima criança
        atual = anterior.proximo
    
    # A última criança restante é a vencedora
    vencedor = circulo.obter_primeiro().nome if not circulo.esta_vazia() else None
    
    return vencedor, ordem_eliminacao

def main():
    """Função principal para demonstrar o jogo"""
    print("=== JOGO DA BATATA QUENTE (com cauda) ===\n")
    
    # Exemplo 1
    criancas = ["Ana", "João", "Maria", "Pedro", "Carla"]
    passes = 3
    
    print(f"Crianças: {criancas}")
    print(f"Passes por rodada: {passes}\n")
    
    vencedor, eliminados = batata_quente(criancas, passes)
    
    print("Ordem de eliminação:")
    for i, crianca in enumerate(eliminados, 1):
        print(f"{i}º eliminado: {crianca}")
    
    print(f"\n🎉 VENCEDOR: {vencedor}!")
    
    print("\n" + "="*50 + "\n")
    
    # Exemplo 2
    criancas2 = ["Alice", "Bob", "Charlie", "Diana", "Eva", "Frank"]
    passes2 = 5
    
    print(f"Crianças: {criancas2}")
    print(f"Passes por rodada: {passes2}\n")
    
    vencedor2, eliminados2 = batata_quente(criancas2, passes2)
    
    print("Ordem de eliminação:")
    for i, crianca in enumerate(eliminados2, 1):
        print(f"{i}º eliminado: {crianca}")
    
    print(f"\n🎉 VENCEDOR: {vencedor2}!")
    
    print("\n" + "="*50 + "\n")
    
    # Teste com casos especiais
    print("=== TESTES ESPECIAIS ===")
    
    # Teste com apenas uma criança
    print("\nTeste com uma criança:")
    vencedor3, eliminados3 = batata_quente(["Sózinho"], 10)
    print(f"Vencedor: {vencedor3}, Eliminados: {eliminados3}")
    
    # Teste com dois passes
    print("\nTeste com 2 passes:")
    vencedor4, eliminados4 = batata_quente(["A", "B", "C"], 2)
    print(f"Vencedor: {vencedor4}, Eliminados: {eliminados4}")

if __name__ == "__main__":
    main()