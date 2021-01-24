vertexList = ['0', '1', '2', '3', '4', '5', '6']
edgeList = [(0, 1), (0, 2), (1, 0), (1, 3), (2, 0), (2, 4),
            (2, 5), (3, 1), (4, 2), (4, 6), (5, 2), (6, 4)]
graphs = (vertexList, edgeList)

# Runtime: O(V+E)
def DFS(graph, start):
    vertexList, edgeList = graph
    visitedList = []
    stack = [start]
    adjacencyList = [[] for vertex in vertexList]

    # fill adjacencyList from graph
    for edge in edgeList:
        adjacencyList[edge[0]].append(edge[1])

    # DFS
    while stack:
        current = stack.pop()
        for neighbor in adjacencyList[current]:
            if not neighbor in visitedList:
                stack.append(neighbor)
        visitedList.append(current)
    return visitedList


print(DFS(graphs, 0))
