from collections import deque

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.adj_list = [[] for _ in range(vertices)]

    def add_edge(self, u, v):
        self.adj_list[u].append(v)

    def count_nodes_at_level(self, start, target_level):
        visited = [False] * self.V
        queue = deque()
        queue.append((start, 0))
        visited[start] = True
        count = 0

        while queue:
            vertex, level = queue.popleft()
            if level == target_level:
                count += 1

            for neighbor in self.adj_list[vertex]:
                if not visited[neighbor]:
                    queue.append((neighbor, level + 1))
                    visited[neighbor] = True

        return count

# Example usage
g = Graph(8)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(1, 4)
g.add_edge(2, 5)
g.add_edge(2, 6)
g.add_edge(3, 7)

start_vertex = 0
target_level = 2

node_count = g.count_nodes_at_level(start_vertex, target_level)
print("Number of nodes at level", target_level, "from vertex", start_vertex, ":", node_count)