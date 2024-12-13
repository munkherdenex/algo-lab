from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def topological_sort_util(self, v, visited, stack):
        visited[v] = True

        for neighbor in self.graph[v]:
            if not visited[neighbor]:
                self.topological_sort_util(neighbor, visited, stack)

        stack.append(v)

    def topological_sort(self):
        visited = [False] * self.V
        stack = []

        for i in range(self.V):
            if not visited[i]:
                self.topological_sort_util(i, visited, stack)

        return stack[::-1]  


V = 6
edges = [(2, 3), (3, 1), (4, 0), (4, 1), (5, 0), (5, 2)]

graph = Graph(V)
for u, v in edges:
    graph.add_edge(u, v)

print("Topological Sort:", graph.topological_sort())
