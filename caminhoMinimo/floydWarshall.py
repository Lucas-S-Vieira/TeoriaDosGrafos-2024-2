import math
import time

def floyd_warshall(grafo):
    inicio = time.time()
    n = grafo.ordem()
    dist = [[math.inf] * n for _ in range(n)]
    pred = [[None] * n for _ in range(n)]
    
    for i in range(n):
        dist[i][i] = 0
        for (j, peso) in grafo.vizinhos(i):
            dist[i][j] = peso
            pred[i][j] = i
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    pred[i][j] = pred[k][j]
    
    tempo = time.time() - inicio
    return dist, pred, tempo

def reconstruir_caminho_fw(pred, origem, destino):
    if pred[origem][destino] is None:
        return [], math.inf
    
    caminho = []
    atual = destino
    while atual != origem:
        caminho.append(atual)
        atual = pred[origem][atual]
        if atual is None:
            return [], math.inf  # Não há caminho
    
    caminho.append(origem)
    caminho.reverse()
    return caminho