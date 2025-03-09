import matrizAdjacencias
import listaAdjacencias
import info
import busca
import math
import sys
from caminhoMinimo import dijkstra, floydWarshall, bellmanFord

# cria um grafo a partir de um arquivo:
def leitura(nomeArquivo):
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
    if len(sys.argv) != 4:
        print("Numero invalido de parametros! Argumentos esperados: main.py grafo.txt origem(number) destino(number)")
        sys.exit(1)

    # sys.argv[1] contem o nome do arquivo a ser lido
    grafo = leitura(sys.argv[1])
    origem = int(sys.argv[2])
    destino = int(sys.argv[3])

    #grafo.printGrafo()

    dist, prev, tempo = dijkstra.dijkstra(grafo, origem)
    caminho, custo = dijkstra.reconstruir_caminho(prev, destino, grafo)
    
    print("Algoritmo de Dijkstra")
    print("Tempo de execução:", tempo)
    print("Caminho:", caminho)
    print("Peso:", custo)
    
    dist_fw, pred_fw, tempo_fw = floydWarshall.floyd_warshall(grafo)
    caminho_fw = floydWarshall.reconstruir_caminho_fw(pred_fw, origem, destino)
    custo_fw = dist_fw[origem][destino] if caminho_fw else math.inf
    
    print("Algoritmo de FW")
    print("Tempo de execução:", tempo_fw)
    print("Caminho:", caminho_fw)
    print("Peso:", custo_fw)