import math
import time
inf = math.inf

def dijkstra (grafo, origem, destino):
    timeout = 600
    s = origem
    inicio = time.time()
    dist = [inf]* grafo.ordem()
    prev = [None] * grafo.ordem()
    dist[s] = 0
    prev[s] = s
    V = set(range(grafo.ordem()))
    O = set(V)
    C = set()
    
    while C != V:
        if time.time() - inicio >= timeout:
            return inf, [], "Tempo excedido"
        if not O:
            break
        u = min(O, key=lambda x: dist[x])
        C.add(u)
        O.remove(u)
        for (v,peso) in grafo.vizinhos(u):
            if v not in C:
                novaDist = dist[u] + peso
                if novaDist < dist[v]:
                    dist[v] = novaDist
                    prev[v] = u
    tempo = time.time() - inicio
    caminho = reconstruir_caminho(prev, destino, grafo)
    return dist[destino], caminho, tempo

def reconstruir_caminho(prev, destino, grafo):
    if prev[destino] is None:
        return []
    caminho = []
    while prev[destino] != destino:
        caminho.insert(0, destino)
        destino = prev[destino]
    caminho.insert(0, destino)
    return caminho
