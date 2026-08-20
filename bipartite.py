def is_bipartite(graph):
    color = [-1] * len(graph)

    for start in range(len(graph)):

        if color[start] == -1:
            queue = [start]
            color[start] = 0

            while queue:
                node = queue.pop(0)

                for neighbour in graph[node]:

                    if color[neighbour] == -1:
                        color[neighbour] = 1 - color[node]
                        queue.append(neighbour)

                    elif color[neighbour] == color[node]:
                        return False

    return True


graph = [
    [1, 3],
    [0, 2],
    [1, 3],
    [0, 2]
]

if is_bipartite(graph):
    print("Graph is Bipartite")
else:
    print("Graph is Not Bipartite")