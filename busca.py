import listaAdjacencias
import matrizAdjacencias

# versao recursiva do DFS (Aula 07 - slide 7):
def dfsRecursivo(grafo, u):
    R = []
    visitado = [False]*grafo.ordem()
    dfsAux(grafo, R, visitado, u)
    return R
def dfsAux(grafo, R, visitado, u):
    visitado[u] = True
    R.append(u)
    for (v,p) in grafo.vizinhos(u):
        if not visitado[v]:
            dfsAux(grafo, R, visitado, v)

# versao iterativa do DFS (Aula 07 - slide 8):
def dfsIterativo(grafo, s):
    R = []
    visitado = [False] * grafo.ordem()
    pilha = []
    pilha.append(s)
    while pilha:
        u = pilha.pop()
        if not visitado[u]:
            visitado[u] = True
            R.append(u)
            for (v, p) in grafo.vizinhos(u):
                if not visitado[v]:
                    pilha.append(v)
    return R

# BFS (Aula 07 - slide 15):
def bfs(grafo, s, e):
    R = []
    visitado = [False] * grafo.ordem()
    fila = []
    fila.append(s)
    visitado[s] = True
    while fila:
        u = fila.pop(0)
        R.append(u)
        for (v, p) in grafo.vizinhos(u):
            if not visitado[v]:
                visitado[v] = True
                fila.append(v)
    return R