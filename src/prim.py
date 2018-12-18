import re
import operator


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
		if edge.node1 not in nodes:
			node = Node(edge.node1, sys.maxsize, None)
			nodes.append(node)
		if edge.node2 not in nodes:
			node = Node(edge.node2, sys.maxsize, None)
			nodes.append(node)

	# first node is starting node
	nodes[0].distance = 0 

	while not nodes:
		curr_node = nodes.pop(0)

		for edge in graph:
			found = False
			if edge.node1 == curr_node.node:
				next_node = edge.node2
				found = True
			else if edge.node2 == curr_node.node:
				next_node = edge.node1
				found = True

			if found:
				new_distance = edge.distance


			
			for x in test_list:
			    if x.value == value:
			        print "i found it!"
			        break			


	nodes = sorted(nodes, key=operator.attrgetter('distance'))

	



f = open("../graph/graph_undirected.txt","r")

graph = []
for line in f:
	if not re.match("//", line):
		node1, node2, distance = line.split(" ")
		edge = Edge(node1, node2, distance)
		graph.append(edge)

prim(graph)


for edge in graph:
	attrs = vars(edge)
	print(', '.join("%s: %s" % item for item in attrs.items()))