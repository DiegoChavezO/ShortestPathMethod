alfabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
'''
import networkx as nx

grafo = nx.DiGraph()

alfabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
def pedirDatos():
    name = input('ingresa el nombre del programa: \n')
    NumNodes = int(input("ingrese el número de nodos: \n"))
    return name, NumNodes

def crearTabla(NumNodes):
    nodos = []
    matriz = []
    for i in range(NumNodes):
        fila = []
        nodos.append(alfabet[i])
        for j in range(NumNodes):
            valor = int(input(f"Ingresa el valor que va de {alfabet[i]} a {alfabet[j]}:  "))
            fila.append(valor) 
        matriz.append(fila)         
    return nodos, matriz

def aristas(NumNodes):
    for i in range(NumNodes):
        grafo.add_nodes_from(alfabet[i])
        for j in range(NumNodes):
            valor = int(input(f"Ingresa el valor que va de {alfabet[i]} a {alfabet[j]}:  "))
            grafo.add_edge(alfabet[i], alfabet[j], capacity=valor)
                 




nombre, node = pedirDatos()
crearTabla(node)
nodoEntrada = input("Ingrese el nodo de entrada: ")
nodoSalida = input("ingrese el nodo de Salida: ")

from networkx.algorithms.flow import shortest_augmenting_path

resultado_valor, grafo_final=nx.maximum_flow(grafo,nodoEntrada,nodoSalida,flow_func=shortest_augmenting_path)
print("resultado: ",resultado_valor)
print("=======")
print("camino final: ",grafo_final)
'''
import networkx as nx
import matplotlib.pyplot as plt

class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)

        if self.rank[x_root] < self.rank[y_root]:
            self.parent[x_root] = y_root
        elif self.rank[x_root] > self.rank[y_root]:
            self.parent[y_root] = x_root
        else:
            self.parent[y_root] = x_root
            self.rank[x_root] += 1

def kruskal(graph):
    num_vertices = len(graph)
    disjoint_set = DisjointSet(num_vertices)
    minimum_spanning_tree = []

    edges = []
    for i in range(num_vertices):
        for j in range(i + 1, num_vertices):
            if graph[i][j] != 0:
                edges.append((i, j, graph[i][j]))

    edges.sort(key=lambda x: x[2])

    for edge in edges:
        source, destination, weight = edge
        if disjoint_set.find(source) != disjoint_set.find(destination):
            disjoint_set.union(source, destination)
            minimum_spanning_tree.append(edge)

    return minimum_spanning_tree

def pedirDatos():
    name = input('ingresa el nombre del programa: \n')
    NumNodes = int(input("ingrese el número de nodos: \n"))
    return name, NumNodes

def crearTabla(NumNodes):
    nodos = []
    matriz = []
    for i in range(NumNodes):
        fila = []
        nodos.append(alfabet[i])
        for j in range(NumNodes):
            valor = int(input(f"Ingresa el valor que va de {i+1} a {j+1}:  "))
            fila.append(valor) 
        matriz.append(fila)         
    return matriz
# Ejemplo de grafo
nombre, NumNodes = pedirDatos()
graph = crearTabla(NumNodes)


# Calcula el árbol de expansión mínima
minimum_spanning_tree = kruskal(graph)

# Crea el grafo con NetworkX
G = nx.Graph()
for edge in minimum_spanning_tree:
    source, destination, weight = edge
    G.add_edge(source, destination, weight=weight)
#imprime el valor:
print(minimum_spanning_tree)
valor_maximo = 0
for i in minimum_spanning_tree:
    valor_maximo = i[2]
print(f"El valor máximo de flujo es: {valor_maximo}")
# Grafica el árbol de expansión mínima
pos = nx.spring_layout(G)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx(G, pos)
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.axis('off')
plt.show()
