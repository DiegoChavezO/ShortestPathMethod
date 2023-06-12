import networkx as nx
import matplotlib.pyplot as plt
from collections import defaultdict

class Graph:
    def __init__(self, grafo):
        self.grafo = grafo
        self.nodos = len(grafo)

    def bfs(self, s, t, padre):
        visitado = [False] * self.nodos
        queue = []
        queue.append(s)
        visitado[s] = True

        while queue:
            u = queue.pop(0)
            for ind, val in enumerate(self.grafo[u]):
                if not visitado[ind] and val > 0:
                    queue.append(ind)
                    visitado[ind] = True
                    padre[ind] = u
                    if ind == t:
                        return True

        return False

    def ford_fulkerson(self, inicio, destino):
        padre = [-1] * self.nodos
        max_flujo = 0

        while self.bfs(inicio, destino, padre):
            ruta_flujo = float("Inf")
            s = destino
            while s != inicio:
                ruta_flujo = min(ruta_flujo, self.grafo[padre[s]][s])
                s = padre[s]

            max_flujo += ruta_flujo
            v = destino
            while v != inicio:
                u = padre[v]
                self.grafo[u][v] -= ruta_flujo
                self.grafo[v][u] += ruta_flujo
                v = padre[v]

        return max_flujo

    def display_graph(self):
        print("Grafo Residual Final:")
        for i in range(self.nodos):
            for j in range(self.nodos):
                print(self.grafo[i][j], end=" ")
            print()

        G = nx.DiGraph()
        for i in range(self.nodos):
            for j in range(self.nodos):
                if self.grafo[i][j] > 0:
                    G.add_edge(i, j, capacity=self.grafo[i][j])

        pos = nx.spring_layout(G)
        labels = nx.get_edge_attributes(G, 'capacidad')
        nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500)
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
        plt.title("Grafo Residual")
        plt.show()

grafo = []
vertices = int(input("Ingrese el numero de vertices: "))
for i in range(vertices):
    row = list(map(int, input(f"Ingrese las capacidades de los bordes del nodo {i + 1}: ").split()))
    grafo.append(row)

inicio = int(input("Ingrese el nodo inicial: ")) - 1
destino = int(input("Ingrese el nodo destino: ")) - 1

g = Graph(grafo)
max_flujo = g.ford_fulkerson(inicio, destino)
print("El máximo flujo en el grafo es:", max_flujo)
g.display_graph()
