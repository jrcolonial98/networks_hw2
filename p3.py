import networkx as nx
import matplotlib.pyplot as plt


# part 1 - create a directed graph
# input is a n x n 2d array, for example
#	[[1, 0], [0, 1]]
def createDirGraph(adj):
	DG = nx.DiGraph()
	for i in range(len(adj)):
		if not DG.has_node(i):
			DG.add_node(i)
		for j in range(len(adj[i])):
			if adj[i][j] == 1:
				if not DG.has_node(j):
					DG.add_node(j)
				DG.add_edge(i, j)
	nx.draw(DG)
	plt.show()

createDirGraph([[0,1,1],[0,0,1],[0,0,0]])
