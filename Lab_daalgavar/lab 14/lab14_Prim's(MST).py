import heapq

def prims(n, edges, start):
    graph = {i: [] for i in range(1, n + 1)}
    for u, v, w in edges:
        graph[u].append((w, v))
        graph[v].append((w, u))

    pq = []
    visited = set()
    min_weight = 0

    visited.add(start)
    for edge in graph[start]:
        heapq.heappush(pq, edge)

    while pq:
        weight, node = heapq.heappop(pq)
        if node not in visited:
            visited.add(node)
            min_weight += weight
            for next_edge in graph[node]:
                if next_edge[1] not in visited:
                    heapq.heappush(pq, next_edge)

    return min_weight

n = 5
edges = [
    (1, 2, 3),
    (1, 3, 4),
    (4, 2, 6),
    (5, 2, 2),
    (2, 3, 5),
    (3, 5, 7)
]
start = 1

print("Minimum weight:", prims(n, edges, start))
