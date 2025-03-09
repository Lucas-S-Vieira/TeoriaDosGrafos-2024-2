import math
import time
inf = math.inf

def dijkstra (grafo, s):
    inicio = time.time()
    dist = [inf]* grafo.ordem()
    prev = [None] * grafo.ordem()
    dist[s] = 0
    prev[s] = s
    V = set(range(grafo.ordem()))
    O = set(V)
    C = set()
    
    while C != V:
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
    return dist, prev, tempo

def reconstruir_caminho(prev, destino, grafo):
    if prev[destino] is None:
        return [], math.inf
    caminho = []
    custo = 0
    while prev[destino] != destino:
        caminho.insert(0, destino)
        peso_aresta = grafo.pesoAresta(prev[destino], destino)
        if peso_aresta is None:
            print("Aresta não encontrada!")
            break
        custo += peso_aresta
        destino = prev[destino]
    caminho.insert(0, destino)
    return caminho, custo
