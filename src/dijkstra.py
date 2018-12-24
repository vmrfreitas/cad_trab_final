from collections import deque, namedtuple
import re

inf = float('inf')
Aresta = namedtuple('Aresta', 'origem, destino, distancia')


def cria_aresta(origem, destino, distancia=1):
  return Aresta(origem, destino, distancia)


class Grafo:
    def __init__(self, arestas):

        self.arestas = [cria_aresta(*aresta) for aresta in arestas]
        self.vertices =  set(sum(([aresta.origem, aresta.destino] for aresta in self.arestas), []))

        vizinhos = {vertice: set() for vertice in self.vertices}
        for aresta in self.arestas:
        	vizinhos[aresta.origem].add((aresta.destino, aresta.distancia))
       	self.vizinhos = vizinhos 


    def dijkstra(self, origem, dest):
        
        distancias = {vertice: inf for vertice in self.vertices}
        anterior = {vertice: None for vertice in self.vertices}
        

        distancias[origem] = 0
        vertices = self.vertices.copy()

        while vertices:

            vert_atual = min(
                vertices, key=lambda vertice: distancias[vertice])
            vertices.remove(vert_atual)

            if distancias[vert_atual] == inf:
                break

            for vizinho, distancia in self.vizinhos[vert_atual]:
                outra_rota = distancias[vert_atual] + distancia

                if outra_rota < distancias[vizinho]:
                    distancias[vizinho] = outra_rota
                    anterior[vizinho] = vert_atual

        caminho, vert_atual = deque(), dest

        while anterior[vert_atual] is not None:
            caminho.appendleft(vert_atual)
            vert_atual = anterior[vert_atual]

        if caminho:
            caminho.appendleft(vert_atual)

        return caminho, distancias[dest]


f = open("../graph/graph_directed.txt","r")

grafo = []
primeira = True

for linha in f:
	if primeira:
		if not re.match("//", linha):
			origem, destino = linha.split(" ")
			primeira = False

	elif not re.match("//", linha):
		origem, destino, distancia = linha.split(" ")
		distancia = int(distancia)
		tupla = (origem, destino, distancia)
		grafo.append(tupla)

grafo_montado = Grafo(grafo)

caminho, distancia = grafo_montado.dijkstra("A", "F")

print("O caminho mínimo é:")
for elemento in caminho:
	print(elemento)

print("\nA distância é:")
print(distancia)