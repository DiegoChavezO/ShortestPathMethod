import networkx as nx
import matplotlib.pyplot as plt
from collections import defaultdict

class Graph:
    def __init__(self, graph):
        self.graph = graph
        self.rows = len(graph)

    def bfs(self, s, t, parent):
        visited = [False] * self.rows
        queue = []
        queue.append(s)
        visited[s] = True

        while queue:
            u = queue.pop(0)
            for ind, val in enumerate(self.graph[u]):
                if not visited[ind] and val > 0:
                    queue.append(ind)
                    visited[ind] = True
                    parent[ind] = u
                    if ind == t:
                        return True

        return False

    def ford_fulkerson(self, source, sink):
        parent = [-1] * self.rows
        max_flow = 0

        while self.bfs(source, sink, parent):
            path_flow = float("Inf")
            s = sink
            while s != source:
                path_flow = min(path_flow, self.graph[parent[s]][s])
                s = parent[s]

            max_flow += path_flow
            v = sink
            while v != source:
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]

        return max_flow

    def display_graph(self):
        print("Final Residual Graph:")
        for i in range(self.rows):
            for j in range(self.rows):
                print(self.graph[i][j], end=" ")
            print()

        G = nx.DiGraph()
        for i in range(self.rows):
            for j in range(self.rows):
                if self.graph[i][j] > 0:
                    G.add_edge(i, j, capacity=self.graph[i][j])

        pos = nx.spring_layout(G)
        labels = nx.get_edge_attributes(G, 'capacity')
        nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500)
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
        plt.title("Residual Graph")
        plt.show()

# User input for the graph
graph = []
vertices = int(input("Enter the number of vertices: "))
for i in range(vertices):
    row = list(map(int, input(f"Enter the capacities for edges from vertex {i}: ").split()))
    graph.append(row)

source = int(input("Enter the source vertex: "))
sink = int(input("Enter the sink vertex: "))

g = Graph(graph)
max_flow = g.ford_fulkerson(source, sink)
print("The maximum flow in the graph is:", max_flow)
g.display_graph()
