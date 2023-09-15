import heapq

def prim(graph):
    start = next(iter(graph))
    visited = set([start])
    edges = [
        (weight, start, neighbor)
        for neighbor, weight in graph[start].items()
    ]
    heapq.heapify(edges)
    mst = []

    while edges:
        weight, u, v = heapq.heappop(edges)
        if v not in visited:
            visited.add(v)
            mst.append((u, v, weight))
            for neighbor, weight in graph[v].items():
                if neighbor not in visited:
                    heapq.heappush(edges, (weight, v, neighbor))

    return mst
