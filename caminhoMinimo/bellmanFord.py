from listaAdjacencias import ListaAdjacencias
import time

def bellmanFord(grafo, origem, destino):
    timeout = 600
    inicio = time.time()

    dist = [float('inf')] * grafo.numVertices
    prev = [None] * grafo.numVertices
    dist[origem] = 0
    prev[origem] = origem

    for k in range(grafo.numVertices - 1):
        for u in range(grafo.numVertices):
            for (v, peso) in grafo.vizinhos(u):
                if time.time() - inicio >= timeout:
                    return [], float('inf'), "Tempo excedido"
                if dist[v] > dist[u] + peso:
                    dist[v] = dist[u] + peso
                    prev[v] = u
    
    caminho = []
    atual = destino
    while atual != origem:
        caminho.append(atual)
        if atual is None:
            tempo = time.time() - inicio
            return [], float('inf'), tempo
        atual = prev[atual]
    caminho.append(origem)
    caminho.reverse()
    tempo = time.time() - inicio
    return caminho, dist[destino], tempo