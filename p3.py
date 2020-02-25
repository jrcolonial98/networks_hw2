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
	return DG

def bfs(DG, v):
	# initialize
	S = {v}
	visited = set()
	to_visit = [v]

	while len(to_visit) > 0:
		# queue: grab first item
		node = to_visit[0]
		to_visit = to_visit[1:]
		visited.add(node)

		# for all neighbors of node
		for neighbor in DG.neighbors(node):
			# do not repeat nodes
			if not neighbor in visited:
				to_visit.append(neighbor)
				S.add(neighbor)

	# return S
	return S



print("displaying graph:")
DG = createDirGraph([[0,1,1],[0,0,1],[0,0,0]])

print("Using BFS to find all nodes reachable from node 0:")
S = bfs(DG, 0)
print(S)
