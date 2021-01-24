import heapq

# Uses min-heap
# Runtime: O[(V+E)log(V)]
def shortestPath(graph, start, dest):
    h = []
    heapq.heappush(h, (0, start))
    while h:
        # pop the one with min cost
        cost, vertex = heapq.heappop(h)
        if vertex == dest:
            print(f"Path from {start} to {dest} exists with cost {cost}")
            return
        for neighbor, neighbor_cost in graph[vertex]:
            heapq.heappush(h, (cost+neighbor_cost, neighbor))


if __name__ == "__main__":
    graph = {"A": [("B", 4), ("C", 2)],
             "B": [("C", 5), ("D", 10)],
             "C": [("E", 3)],
             "D": [("F", 11)],
             "E": [("D", 4)]}
    shortestPath(graph, "A", "D")
    shortestPath(graph, "A", "E")
    shortestPath(graph, "B", "D")
    shortestPath(graph, "A", "C")

    graph2 = {"A": [("B", 1), ("C", 5)],
             "B": [("C", 1), ("D", 10)],
             "C": [("E", 3)],
             "D": [("F", 11)],
             "E": [("D", 4)]}
    shortestPath(graph2, "A", "C")

