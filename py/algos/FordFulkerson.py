def ford_fulkerson(graph, source, sink):
    def bfs(graph, source, sink, parent):
        visited = [False] * len(graph)
        queue = []
        queue.append(source)
        visited[source] = True

        while queue:
            u = queue.pop(0)
            for v, capacity in enumerate(graph[u]):
                if visited[v] is False and capacity > 0:
                    queue.append(v)
                    visited[v] = True
                    parent[v] = u
        return visited[sink]

    max_flow = 0
    parent = [-1] * len(graph)

    while bfs(graph, source, sink, parent):
        path_flow = float("inf")
        s = sink
        while s != source:
            path_flow = min(path_flow, graph[parent[s]][s])
            s = parent[s]
        max_flow += path_flow
        v = sink
        while v != source:
            u = parent[v]
            graph[u][v] -= path_flow
            graph[v][u] += path_flow
            v = parent[v]

    return max_flow
