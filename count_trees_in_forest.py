from collections import deque

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.adj_list = [[] for _ in range(vertices)]

    def add_edge(self, u, v):
        self.adj_list[u].append(v)

    def count_trees_in_forest(self):
        visited = [False] * self.V
        count = 0

        def dfs_helper(vertex):
            visited[vertex] = True

            for neighbor in self.adj_list[vertex]:
                if not visited[neighbor]:
                    dfs_helper(neighbor)

        for vertex in range(self.V):
            if not visited[vertex]:
                dfs_helper(vertex)
                count += 1

        return count

# Example usage
g = Graph(6)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(3, 4)
g.add_edge(4, 5)

num_trees = g.count_trees_in_forest()
print("Number of trees in the forest:", num_trees)