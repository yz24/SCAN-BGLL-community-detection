import networkx as nx
import pandas as pd
import math
from sklearn import metrics
from BGLL import PyLouvain
import numpy as np

#
# G = nx.read_gml('data/lesmis.gml', label='label')
# print(G)
# G = nx.Graph()
# f = pd.read_csv('t.txt', sep=',', header=None)
# edge_list = []
# for i, j in zip(f[0], f[1]):
# 	edge_list.append((i, j))
# G.add_edges_from(edge_list)
#
# b = nx.betweenness_centrality(G)
# m = max(b.values())
# print(m)

# pyl = PyLouvain.from_file("data/karate.txt")
# partition, q = pyl.apply_method()
# print(partition)
# print(q)

labels_pre = [[1, 4, 10, 12, 13, 15], [17, 18, 19, 21, 22, 26, 0, 7, 8, 11, 14, 16, 20, 24, 25, 27, 33],
              [2, 5, 6, 23, 28, 32, 3, 29], [9, 30, 31]]
labels_pre = np.array(labels_pre)

m = max(max(labels_pre[i]) for i in range(labels_pre.size))
# print(m)
labels_pre_ = [-1 for i in range(m + 1)]
labels_true = [1 for i in range(m + 1)]
for i in range(labels_pre.size):
    for j in labels_pre[i]:
        labels_pre_[j] = i

print(labels_pre_)
print(labels_true)
NMI = metrics.normalized_mutual_info_score(labels_true, labels_pre_)
print(NMI)