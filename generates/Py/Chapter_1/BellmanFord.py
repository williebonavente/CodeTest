def bellman_ford(graph, start):
    """
        Calculate the shortest distances from a starting vertex to all other vertices
        in a weighted directed graph using the Bellman-Ford algorithm.

        Parameters:
        - graph (dict): A dictionary representing the graph. Each vertex is a key,
        and the value is another dictionary containing neighbors as keys and edge
        weights as values.
        - start: The starting vertex for the shortest path calculations.

        Returns:
        - distances (dict): A dictionary where keys are vertices and values are
        the shortest distances from the start vertex to each vertex. If a vertex
        is unreachable, its distance is set to positive infinity.
    
    """
    # Initialize distances with infinity for all vertices except the start vertex.
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0

    for _ in range(len(graph) - 1):
        for vertex in graph:
            for neighbor, weight in graph[vertex].items():
                if distances[vertex] + weight < distances[neighbor]:
                    distances[neighbor] = distances[vertex] + weight

    return distances