import matrizAdjacencias
import listaAdjacencias
import info
import busca
import sys

def leituraMaze(arquivo):
    matriz = []
    with open(arquivo, 'r') as f:
        for linha in f:
            linha = linha.rstrip('\n')
            matriz.append(list(linha))
    linhas = len(matriz)
    colunas = len(matriz[0])
    grafo = listaAdjacencias.ListaAdjacencias((linhas*colunas))
    inicio = None
    fim = None
    direcoes = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    for i in range(linhas):
        for j in range(colunas):
            if matriz[i][j] != '#':
                for di, dj in direcoes:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < linhas and 0 <= nj < colunas:
                        if matriz[ni][nj] != '#':
                            pai = i * colunas + j
                            filho = ni * colunas + nj
                            grafo.addAresta(pai, filho)
                if matriz[i][j] == 'S':
                    inicio = i*colunas +j
                elif matriz[i][j] == 'E':
                    fim = i*colunas +j
    return grafo, inicio, fim, colunas 

def coordenada(indice, colunas):
    i = indice // colunas
    j = indice % colunas
    return (i, j)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Numero invalido de parametros! Argumentos esperados: mainMaze.py maze.txt")
        sys.exit(1)

    # sys.argv[1] contem o nome do arquivo a ser lido
    
    import time as time
    start = time.time()
    grafo, inicio, fim, colunas = leituraMaze(sys.argv[1])
    caminho = busca.bfs(grafo, inicio, fim) 
    
    coordenadas = [coordenada(indice, colunas) for indice in caminho]
    
    print("Caminho:", coordenadas)
    print("Tempo de execução:", time.time() - start)