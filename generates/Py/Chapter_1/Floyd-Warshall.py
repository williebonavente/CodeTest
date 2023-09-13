def floyd_warshall(graph):
    distances = {vertex: {v: float('inf') for v in graph} for vertex in graph}

    for vertex in graph:
        distances[vertex][vertex] = 0

    for u in graph:
        for v in graph[u]:
            distances[u][v] = graph[u][v]

    for k in graph:
        for i in graph:
            for j in graph:
                distances[i][j] = min(distances[i][j], distances[i][k] + distances[k][j])

    return distances
