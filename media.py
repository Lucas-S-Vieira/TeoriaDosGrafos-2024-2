import os
import math

# Defina o caminho para o arquivo de resultados
nome_resultado = "resultados/USA-road-dt.DC_resultado.txt"

# Dicionário para armazenar os dados de cada algoritmo
algoritmos = {
    "Dijkstra": {"tempos": [], "custos": [], "exceeded": False},
    "Bellman-Ford": {"tempos": [], "custos": [], "exceeded": False},
    "FloydWarshall": {"tempos": [], "custos": [], "exceeded": False},
}

# Variável para identificar o algoritmo atual
algoritmo_atual = None

with open(nome_resultado, "r") as arq:
    for linha in arq:
        linha = linha.strip()
        # Identifica a seção do algoritmo
        if linha.startswith("Algoritmo de"):
            parte = linha.split("Algoritmo de ")[1].strip()
            if "Dijkstra" in parte:
                algoritmo_atual = "Dijkstra"
            elif "Bellman-Ford" in parte:
                algoritmo_atual = "Bellman-Ford"
            elif "Floyd" in parte:
                algoritmo_atual = "FloydWarshall"
        # Extrai o tempo de execução
        elif linha.startswith("Tempo de execução:"):
            if algoritmo_atual:
                valor = linha.split("Tempo de execução:")[1].strip()
                if valor.lower() == "tempo excedido":
                    algoritmos[algoritmo_atual]["exceeded"] = True
                else:
                    try:
                        tempo_valor = float(valor)
                        algoritmos[algoritmo_atual]["tempos"].append(tempo_valor)
                    except ValueError:
                        # Em caso de erro, marca como excedido
                        algoritmos[algoritmo_atual]["exceeded"] = True
        # Extrai o custo (peso)
        elif linha.startswith("Peso:"):
            if algoritmo_atual:
                valor = linha.split("Peso:")[1].strip()
                try:
                    custo_valor = float(valor)
                except ValueError:
                    custo_valor = math.inf
                algoritmos[algoritmo_atual]["custos"].append(custo_valor)

# Função para calcular a média considerando apenas valores finitos.
def calcular_media(valores):
    valores_finitos = [v for v in valores if v != math.inf]
    if not valores_finitos:
        return math.inf
    return sum(valores_finitos) / len(valores_finitos)

# Calcula e exibe as médias para cada algoritmo.
for nome, dados in algoritmos.items():
    # Se alguma rodada teve "Tempo excedido", a média do tempo será "TEMPO_EXCEDIDO"
    if dados["exceeded"]:
        media_tempo = "TEMPO_EXCEDIDO"
    else:
        media_t = calcular_media(dados["tempos"])
        media_tempo = "inf" if media_t == math.inf else f"{media_t:.6f}"
    # Média do custo: se todos forem inf, retorna inf; senão, média dos finitos.
    media_c = calcular_media(dados["custos"])
    media_custo = "inf" if media_c == math.inf else f"{media_c:.6f}"
    
    print(f"{nome}:")
    print(f"  Média do tempo de execução: {media_tempo}")
    print(f"  Média do custo: {media_custo}")
