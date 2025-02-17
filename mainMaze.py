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
    
    mapa_vertices = {}
    num_vertices = 0
    inicio = None
    fim = None

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] != '#':
                mapa_vertices[(i, j)] = num_vertices
                if matriz[i][j] == 'S':
                    inicio = num_vertices
                elif matriz[i][j] == 'E':
                    fim = num_vertices
                num_vertices += 1

    grafo = listaAdjacencias.ListaAdjacencias(num_vertices)

    direcoes = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for (i, j), v1 in mapa_vertices.items():
        for di, dj in direcoes:
            ni, nj = i + di, j + dj
            if (ni, nj) in mapa_vertices:
                v2 = mapa_vertices[(ni, nj)]
                grafo.addAresta(v1, v2)
                grafo.addAresta(v2, v1)
    caminho = busca.bfs(grafo, inicio, fim)
    return grafo, inicio, fim, mapa_vertices

def caminho_para_coordenadas(caminho, mapa_vertices):
    id_para_coordenada = {v: k for k, v in mapa_vertices.items()}
    return [id_para_coordenada[id] for id in caminho]

# cria um grafo a partir de um arquivo:
def leituraGrafo(nomeArquivo):
    arquivo = open(nomeArquivo)

    str = arquivo.readline()
    str = str.split(" ")
    numVertices = int(str[0])
    numArestas = int(str[1])

    grafo = listaAdjacencias.ListaAdjacencias(numVertices)
    # grafo = matrizAdjacencias.MatrizAdjacencias(numVertices)

    for i in range(numArestas):
        str = arquivo.readline()
        str = str.split(" ")
        origem = int(str[0])
        destino = int(str[1])
        peso = int(str[2])
        grafo.addAresta(origem, destino, peso)

    return grafo

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Numero invalido de parametros! Argumentos esperados: main.py grafo.txt")
        sys.exit(1)

    # sys.argv[1] contem o nome do arquivo a ser lido
    grafo = leituraGrafo(sys.argv[1])

    grafo.printGrafo()

