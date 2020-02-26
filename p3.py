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


# part 2 - BFS
# input is a directed graph, as created in part 1, 
# and a starting vertex v
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

# same as before, but now also returns the path to a given target
# or [] if no such path exists
def bfs_with_target(DG, s, t):
	# initialize
	visited = set()
	to_visit = [(s, [s])]

	while len(to_visit) > 0:
		# queue: grab first item
		node, path = to_visit[0]
		to_visit = to_visit[1:]
		visited.add(node)

		# if target found
		if node == t:
			return path

		# for all neighbors of node
		for neighbor in DG.neighbors(node):
			if not neighbor in visited:
				new_path = path + [neighbor]
				to_visit.append((neighbor, new_path))

	# t not found
	return []

def max_flow_bfs(DG, s, t):
	R = DG.copy()
	flow = 0

	path = bfs_with_target(R, s, t)
	fprime = 100000 # "infinite" value
	while len(path) > 0:
		# go thru each edge in the path to calculate f prime
		for i in range(len(path) - 1):
			frm = path[i]
			to = path[i+1]
			weight = R[frm][to]['weight']
			fprime = min(fprime, weight)

		# go thru each edge in the path and update R
		for i in range(len(path) - 1):
			frm = path[i]
			to = path[i+1]

			if not R.has_edge(to, frm):
				R.add_edge(to, frm, weight=0)
			old_weight = R[to][frm]['weight']
			R[to][frm]['weight'] = old_weight + fprime

			old_weight = R[frm][to]['weight']
			R[frm][to]['weight'] = old_weight - fprime
			if old_weight == fprime:
				R.remove_edge(frm, to)
		flow = flow + fprime			

		path = bfs_with_target(R, s, t)
	return flow


print("displaying graph:")
DG = createDirGraph([[0,1,1],[0,0,1],[0,0,0]])

print("Using BFS to find all nodes reachable from node 0:")
S = bfs(DG, 0)
print(S)
print(bfs_with_target(DG, 0, 2))

# directed weighted graph from class, max flow should be 30
DG2 = nx.DiGraph()
DG2.add_node(0)
DG2.add_node(1)
DG2.add_node(2)
DG2.add_node(3)
DG2.add_edge(0,1,weight=20)
DG2.add_edge(0,2,weight=10)
DG2.add_edge(1,2,weight=30)
DG2.add_edge(1,3,weight=10)
DG2.add_edge(2,3,weight=20)
print(max_flow_bfs(DG2, 0, 3))
