from collections import deque

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.adj_list = [[] for _ in range(vertices)]

    def add_edge(self, u, v):
        self.adj_list[u].append(v)

    def bfs(self, start):
        visited = [False] * self.V
        queue = deque()
        queue.append(start)
        visited[start] = True

        while queue:
            vertex = queue.popleft()
            print(vertex, end=" ")

            for neighbor in self.adj_list[vertex]:
                if not visited[neighbor]:
                    queue.append(neighbor)
                    visited[neighbor] = True

    def dfs(self, start):
        visited = [False] * self.V
        self._dfs_helper(start, visited)

    def _dfs_helper(self, vertex, visited):
        visited[vertex] = True
        print(vertex, end=" ")

        for neighbor in self.adj_list[vertex]:
            if not visited[neighbor]:
                self._dfs_helper(neighbor, visited)


# Create a graph with 5 vertices
g = Graph(5)

# Add edges
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(2, 4)

# Perform BFS starting from vertex 0
print("BFS traversal:")
g.bfs(0)
print()

# Perform DFS starting from vertex 0
print("DFS traversal:")
g.dfs(0)
print()                