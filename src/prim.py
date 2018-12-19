import re
import operator
import sys
import copy

class Edge():
	def __init__(self, node1, node2, distance):
		self.node1 = node1
		self.node2 = node2
		self.distance = distance

class Node():
	def __init__(self, node, distance, pred):
		self.node = node
		self.distance = distance
		self.pred = pred


def prim(graph):
	nodes = []

	# initialize the distances
	for edge in graph:
		found1 = False
		found2 = False
		for node in nodes:
			if edge.node1 == node.node:
				found1 = True
			elif edge.node2 == node.node:
				found2 = True

		if not found1:
			node = Node(edge.node1, sys.maxsize, None)
			nodes.append(node)
		if not found2:
			node = Node(edge.node2, sys.maxsize, None)
			nodes.append(node)

	# first node is starting node
	nodes[0].distance = 0 
	nodes_list = copy.deepcopy(nodes)

	while nodes_list:

		curr_node = nodes_list.pop(0)

		for edge in graph: 
			found = False
			if edge.node1 == curr_node.node:
				next_node = edge.node2
				new_distance = edge.distance
				found = True
			elif edge.node2 == curr_node.node:
				next_node = edge.node1
				new_distance = edge.distance
				found =True

			if found:
				for node_l in nodes_list:
					if node_l.node == next_node:
						if new_distance<node_l.distance:

							for node in nodes:
								if node.node == node_l.node:
									node.pred = curr_node.node
									node.distance = new_distance
									node_l.distance = new_distance
									break
							break

				nodes_list = sorted(nodes_list, key=operator.attrgetter('distance'))

	return nodes



f = open("../graph/graph_undirected2.txt","r")

graph = []
for line in f:
	if not re.match("//", line):
		node1, node2, distance = line.split(" ")
		edge = Edge(node1, node2, distance)
		edge.distance = int(edge.distance)
		graph.append(edge)

result = prim(graph)

print("Resulting minimum spanning tree:")

result.pop(0)

for node in result:
	print("node1: %s, node2: %s, distance: %s" % (node.pred, node.node, node.distance))