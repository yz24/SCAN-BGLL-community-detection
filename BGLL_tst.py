import math
import unittest
import numpy as np
from BGLL import PyLouvain
from sklearn import metrics


def compute_NMI(labels_true, labels_pre):
	labels_pre = np.array(labels_pre)

	m = max(max(labels_pre[i]) for i in range(labels_pre.size))
	# print(m)
	labels_pre_ = [-1 for i in range(m + 1)]
	# labels_true = [1 for i in range(m + 1)]
	for i in range(labels_pre.size):
		for j in labels_pre[i]:
			labels_pre_[j] = i
	print("Clustering : ", labels_pre_)
	NMI = metrics.normalized_mutual_info_score(labels_true, labels_pre_)
	return NMI


if __name__ == '__main__':
	filename = 'data/karate.txt'
	labels_true = [1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 2, 2, 1, 1, 2, 1, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
	if filename.split('.')[-1] == 'gml':
		pyl = PyLouvain.from_gml_file(filename)
	else:
		pyl = PyLouvain.from_file(filename)
	partition, q = pyl.apply_method()
	# print("Clustering : ")
	# print(partition)
	# for clu in partition:
	# 	print(clu)
	print("Modularity : ", q)
	if labels_true:
		NMI = compute_NMI(labels_true, partition)
		print("NMI", NMI)
