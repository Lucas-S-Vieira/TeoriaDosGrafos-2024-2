from math import inf
import time
import listaAdjacencias

def floyd_warshall(grafo, origem, destino):
    timeout = 600
    inicio = time.time()
    n = grafo.ordem()
    dist = [[inf] * n for _ in range(n)]
    prev = [[None] * n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            if i is j:
                dist[i][j] = 0
                prev[i][j] = i
            elif grafo.possuiAresta(i,j):
                dist[i][j] = grafo.pesoAresta(i,j)
                prev[i][j] = i
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if time.time() - inicio >= timeout:
                    return inf, [], "Tempo excedido"
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    prev[i][j] = prev[k][j]
    
    tempo = time.time() - inicio
    caminho = reconstruir_caminho_fw (prev, origem, destino)
    return dist[origem][destino], caminho, tempo

def reconstruir_caminho_fw(prev, origem, destino):
    if prev[origem][destino] is None:
        return []
    
    caminho = []
    atual = destino
    while atual != origem:
        caminho.append(atual)
        atual = prev[origem][atual]
        if atual is None:
            return []
    
    caminho.append(origem)
    caminho.reverse()
    return caminho