vertexList = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
edgeList = [(0, 1), (1, 2), (1, 3), (3, 4), (4, 5), (1, 6)]
graphs = (vertexList, edgeList)

# Runtime: O(V+E)
def BFS(graph, start):
    vertexList, edgeList = graph
    visitedList = []
    queue = [start]
    adjacencyList = [[] for vertex in vertexList]

    # fill adjacencyList from graph
    for edge in edgeList:
        adjacencyList[edge[0]].append(edge[1])

    # BFS
    while queue:
        current = queue.pop(0)
        for neighbor in adjacencyList[current]:
            if not neighbor in visitedList:
                queue.append(neighbor)
        visitedList.append(current)
    return visitedList


print(BFS(graphs, 0))
