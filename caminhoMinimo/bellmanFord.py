from listaAdjacencias import ListaAdjacencias
import time

def bellmanFord(grafo, origem, destino):

  
  dist = [float('inf')] * grafo.numVertices
  prev = [None] * grafo.numVertices
  dist[origem] = 0
  prev[origem] = origem
  
  inicio = time.time()
  
  for k in range(grafo.numVertices - 1):
    atualizou = False
    for u in range(grafo.numVertices):
      for (v, peso) in grafo.vizinhos(u):
        if dist[v] > dist[u] + peso:
          dist[v] = dist[u] + peso
          prev[v] = u
          atualizou = True
      if not atualizou:
        break
      
  tempo = time.time() - inicio   
      
  caminho = []

  atual = destino
  while atual != origem:
    caminho.append(atual)
    atual = prev[atual]
  caminho.append(origem)
  caminho.reverse()
  
  return caminho, dist[destino], tempo