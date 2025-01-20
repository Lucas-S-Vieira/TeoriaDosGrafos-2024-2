import listaAdjacencias

# versao recursiva do DFS (Aula 07 - slide 7):
def dfsRecursivo(grafo, u):
    R = []
    visitado = [False] * grafo.ordem()
    dfsRecursivoAux(grafo, R, visitado, u)
    return R
    
def dfsRecursivoAux(grafo, R, visitado, u):
    visitado[u] = True
    R.append(u)
    for (v,p) in grafo.vizinhos(u):
        if not visitado[v]:
            dfsRecursivoAux(grafo, R, visitado, v)
    

# versao iterativa do DFS (Aula 07 - slide 8):
def dfsIterativo(grafo, s):
    R = []
    pilha = []
    visitado = [False] * grafo.ordem()
    pilha.append(s)
    visitado[s] = True
    while (pilha):
        print ("teste while")
        u = pilha.pop()
        R.append(u)
        for (v,p) in grafo.vizinhos(u):
            if not visitado[v]:
                pilha.append(v)
                visitado[v] = True
    return R
        

# BFS (Aula 07 - slide 15):
def bfs(grafo, u):
    R = []
    fila = []
    visitado = [False] * grafo.ordem()
    fila.append(u)
    visitado[u] = True
    while (fila):
        s = fila.pop(0)
        R.append(s)
        for (v,p) in grafo.vizinhos(s):
            if not visitado[v]:
                fila.append(v)
                visitado[v] = True
    return R