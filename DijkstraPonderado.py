import heapq

def dijkstra_pond(grafo, start, vertices):
    # Número de vértices do grafo, adicionei porque ele tava pegando vértice 1 como 0, então não chegava até ao 71
    num_vertices = len(grafo) + 1

    #Inicialização das variáveis, dist é um vetor que armazena as distâncias
    dist = [float('inf')] * num_vertices
    dist[start] = 0
    resultado = 0

    # Fila de prioridade para selecionar o próximo vértice a ser visitado
    priority_queue = [(dist, start)]

    #Loop da lista de vértices que serão feitas as entregas
    while vertices:
        #Loop para selecionar a melhor rota do vertice[i] ao vertice[i+1]
        while priority_queue:
            # Extrai o vértice com menor distância da fila de prioridade
            current_dist, current_vertex = heapq.heappop(priority_queue)

            # Verifica se o vértice atual está na lista de vértices a calcular
            if current_vertex in vertices:
                print(f"A distância mínima entre {start} e {current_vertex} é: {current_dist}")
                
                #o vértice inicial passa a ser o próximo da lista, distância final e atual são atualizadas
                start = current_vertex
                resultado += current_dist
                dist[start] = 0

                # Remove o vértice da lista de vértices a calcular
                vertices.remove(current_vertex)

                # Verifica se a lista de vértices foi completamente calculada
                if not vertices:
                    break

            # Percorre todos os vizinhos do vértice atual
            for vizinho in (grafo[current_vertex]):

                # Ignora vértices sem aresta
                if vizinho[1] == 0:
                    continue

                # Calcula a ponderação
                pond = calculate_pond(vizinho[0])

                # Calcula a nova distância até o vizinho
                new_dist = dist[current_vertex] + vizinho [1] + pond

                # Verifica se a nova distância é menor que a armazenada
                if vizinho and vizinho[0] < len(dist):
                    if new_dist < dist[vizinho[0]]:
                        # Atualiza a distância
                        dist[vizinho[0]] = new_dist
            

                        # Adiciona o vizinho à fila de prioridade
                        heapq.heappush(priority_queue, (new_dist, vizinho[0]))
        
    print("Resultado Final é = ",resultado)

#Função da Heurística
def calculate_pond(vertice):
    result = 0
    
    #ruas com semáforo
    if 34 <= vertice <= 43:
        result = 200

    #ruas com buracos/más condições de asfalto  
    elif 7 <= vertice <= 23:
        result = 100

    #ruas escuras
    elif (1 <= vertice <= 6) or (63 <= vertice <= 71):
        result = 100
    
    return result

#Grafo da parte comercial da cidade de Russas
grafo = {
    1: [(2, 101), (7, 64)],
    2: [(1, 101), (3, 107), (8,64)],
    3: [(2, 107), (4, 129), (9,64)],
    4: [(3, 129), (5, 64), (10,65)],
    5: [(4,64), (6,95), (11,65)],
    6: [(5,95), (12,65)],
    7: [(1,64), (8,98), (15,43)],
    8: [(7,98), (2,64), (16,46)],
    9: [(3,64), (8,114), (17,49)],
    10: [(4,65), (9,128),(11,74), (13,47), (18,54)],
    11: [(5,65), (10,74), (12,98)],
    12: [(6,65), (11,98)],
    13: [(10,47), (14,125), (19,60)],
    14: [(13,125), (20,67)],
    15: [(7,43), (16,106), (24,40)],
    16: [(8,46), (15,106), (17,114), (25,51)],
    17: [(9,49), (16,114), (18,135), (21,48), (26,66)],
    18: [(10,54), (17,135), (19,47)],
    19: [(13,60), (18,47), (20,137), (23,49), (30,60)],
    20: [(14,67), (19,137), (31,64)],
    21: [(17,48), (22,35), (27,60)],
    22: [(21,35), (23,22), (28,53)],
    23: [(19,49), (22,22), (29,61)],
    24: [(15,40), (25,105), (34,56)],
    25: [(16,51), (24,105), (26,115), (35,61)],
    26: [(17,66), (25,115), (27,51), (36,68)],
    27: [(21,60), (26,51), (28,32), (37,67)],
    28: [(22,53), (27,32), (29,22), (32,127), (38,61)],
    29: [(23,61), (28,22), (30,47)],
    30: [(19,60), (29,47), (31,143)],
    31: [(20,64), (30,143)],
    32: [(28,127), (33,121), (39,57)],
    33: [(32,121), (40,41)],
    34: [(24,56), (35,100), (44,33)],
    35: [(25,61), (34,100), (36,116), (42,71), (45,33)],
    36: [(26,68) ,(35,116), (37,57)],
    37: [(27,67), (36,57), (38,42)],
    38: [(28,61), (37,42), (39,127)],
    39: [(32,57), (38,127), (40,119)],
    40: [(33,41), (39,119), (41,99), (43,331), (51,37)],
    41: [(40,99), (59,61)],
    42: [(35,71), (43,65), (46,50), (53,132)],
    43: [(40,331), (42,65), (47,26), (54,39)],
    44: [(34,33), (45,99), (46,182), (52,50)],
    45: [(35,33), (44,99), (46,80)],
    46: [(42,50), (44,182), (45,80), (53,70)],
    47: [(43,26), (48,149), (51,361), (54,75)],
    48: [(47,149), (49,57), (56,59)],
    49: [(48,57), (50,74), (57,49)],
    50: [(49,74), (51,50), (58,38)],
    51: [(40,37), (47,361), (50,50)],
    52: [(44,50), (53,182)],
    53: [(42,132), (46,70), (52,182), (54,51)],
    54: [(43,139), (47,75), (55,44), (56,161)],
    55: [(54,44), (56,110), (65,81)],
    56: [(48,59), (54,161), (55,110), (57,56), (60,51), (66,103)],
    57: [(49,49), (56,56), (58,62), (61,69)],
    58: [(50,38), (57,62), (59,141), (62,55)],
    59: [(41,61), (58,141)],
    60: [(56,51), (61,60), (66,52)],
    61: [(57,69), (60,60), (62,63), (67,51)],
    62: [(58,55), (61,63), (68,49)],
    63: [(53,88), (64,18), (66,175), (69,185)],
    64: [(54,76), (63,18), (65,27)],
    65: [(55,81), (64,27), (66,123)], 
    66: [(56,103), (60,52), (63,175), (65,123), (67,57), (68,151), (69,63), (70,43)],
    67: [(61,51), (66,57), (68,86)],
    68: [(62,49), (66,151), (67,86), (71,68)],
    69: [(63,181), (66,63)],
    70: [(66,43), (71,164)],
    71: [(68,68), (70,164)],
}

start_vertex = #Vértice Inicial
vertices_to_calculate = []  # Lista de vértices a calcular

dijkstra_pond(grafo, start_vertex, vertices_to_calculate) #Chama a função de Dijkstra com Heurísticas, passando o grafo, vértice inicial e a lista de vértices que irá passar
