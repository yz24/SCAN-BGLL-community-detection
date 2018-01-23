import networkx as nx
import math
import pandas as pd


def similarity(G, v, u):
	v_set = set(G.neighbors(v))
	u_set = set(G.neighbors(u))
	v_set.add(v)
	u_set.add(u)
	inter = v_set & u_set
	if inter == set():
		return 0
	# need to account for vertex itself, add 2(1 for each vertex)
	sim = len(inter) / (math.sqrt(len(v_set) * len(u_set)))
	return sim


def neighborhood(G, v, eps):
	eps_neighbors = []
	v_list = G.neighbors(v)
	for u in v_list:
		# print(similarity(G, u, v), u, v)
		if (similarity(G, u, v)) > eps:
			eps_neighbors.append(u)
	return eps_neighbors


def hasLabel(cliques, vertex):
	for k, v in cliques.items():
		if vertex in v:
			return True
	return False


def isNonMember(li, u):
	if u in li:
		return True
	return False


def sameClusters(G, clusters, u):
	n = G.neighbors(u)
	# belong
	b = []
	i = 0
	while i < len(n):
		for k, v in clusters.items():
			if n[i] in v:
				if k in b:
					continue
				else:
					b.append(k)
		i = i + 1
	if len(b) > 1:
		return False
	return True


def scan(G, eps=0.5, mu=2):
	c = 0
	clusters = dict()
	nomembers = []
	for n, nbrs in G.adjacency_iter():
		if hasLabel(clusters, n):
			continue
		else:
			N = neighborhood(G, n, eps)
			# test if vertex is core
			if len(N) > mu:
				'''Generate a new cluster-id c'''
				c = c + 1
				Q = neighborhood(G, n, eps)
				clusters[c] = []
				# append core vertex itself
				clusters[c].append(n)
				while len(Q) != 0:
					w = Q.pop(0)
					R = neighborhood(G, w, eps)
					# include current vertex itself
					R.append(w)
					for s in R:
						if not (hasLabel(clusters, s)) or isNonMember(nomembers, s):
							clusters[c].append(s)
						if not (hasLabel(clusters, s)):
							Q.append(s)
			else:
				nomembers.append(n)
	outliers = []
	hubs = []
	for v in nomembers:
		if not sameClusters(G, clusters, v):
			hubs.append(v)
		else:
			outliers.append(v)
	return clusters, hubs, outliers


def main():
	G = nx.Graph()
	f = pd.read_csv('t.txt', sep='\t', header=None)
	edge_list = []
	for i, j in zip(f[0], f[1]):
		edge_list.append((i, j))
	G.add_edges_from(edge_list)
	(clusters, hubs, outliers) = scan(G)

	print('clusters: ')
	for k, v in clusters.items():
		print(k, v)
	print('hubs ', hubs)
	print('outliers ', outliers)
	# print(G.edge)

main()
