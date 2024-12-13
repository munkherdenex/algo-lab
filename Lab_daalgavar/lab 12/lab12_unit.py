import unittest
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


class TestTopologicalSort(unittest.TestCase):
    def test_example_case(self):
        V = 6
        edges = [(2, 3), (3, 1), (4, 0), (4, 1), (5, 0), (5, 2)]

        graph = Graph(V)
        for u, v in edges:
            graph.add_edge(u, v)

        result = graph.topological_sort()

        valid_order = [4, 5, 2, 0, 3, 1]
        node_to_index = {node: index for index, node in enumerate(result)}

        for u, v in edges:
            self.assertTrue(node_to_index[u] < node_to_index[v])

        print("Topological Sort:", result)

if __name__ == "__main__":
    unittest.main()
