import os
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
    if len(sys.argv) != 2:
        print("Numero invalido de parametros! Argumentos esperados: main.py grafo.txt")
        sys.exit(1)

    # sys.argv[1] contem o nome do arquivo a ser lido
    grafo = leitura(sys.argv[1])
    
    nome_grafo = os.path.basename(sys.argv[1]) 
    nome_resultado = os.path.splitext(nome_grafo)[0] + "_resultado.txt"
    
    pasta_resultados = "resultados"
    os.makedirs(pasta_resultados, exist_ok=True)
    
    caminho_resultado = os.path.join(pasta_resultados, nome_resultado)
    
    with open(caminho_resultado, "w") as arquivo_resultado:
        for rodada in range(1, 11):
            
            origem, destino = grafo.gerarOrigemDestino()
            print(f"Rodada {rodada}", file=arquivo_resultado)
            print("Origem:", origem, "Destino:", destino, file=arquivo_resultado)
            print("Processando...", file=arquivo_resultado)
            
            
            custo_dj, caminho_dj, tempo_dj = dijkstra.dijkstra(grafo, origem, destino)
            custo_fw, caminho_fw, tempo_fw = floydWarshall.floyd_warshall(grafo, origem, destino)
            caminho_bf, custo_bf, tempo_bf = bellmanFord.bellmanFord(grafo, origem, destino)
            
            
            print("----------------------------------------", file=arquivo_resultado)
            print("Algoritmo de Dijkstra", file=arquivo_resultado)
            print("Tempo de execução:", tempo_dj, file=arquivo_resultado)
            print("Caminho:", caminho_dj, file=arquivo_resultado)
            print("Peso:", custo_dj, file=arquivo_resultado)
            print("----------------------------------------", file=arquivo_resultado)
            print("Algoritmo de Bellman-Ford", file=arquivo_resultado)
            print("Tempo de execução:", tempo_bf, file=arquivo_resultado)
            print("Caminho:", caminho_bf, file=arquivo_resultado)
            print("Peso:", custo_bf, file=arquivo_resultado)
            print("----------------------------------------", file=arquivo_resultado)
            print("Algoritmo de FloydWarshall", file=arquivo_resultado)
            print("Tempo de execução:", tempo_fw, file=arquivo_resultado)
            print("Caminho:", caminho_fw, file=arquivo_resultado)
            print("Peso:", custo_fw, file=arquivo_resultado)
            print("\n", file=arquivo_resultado)
            
            print(f"Rodada {rodada} concluída.")