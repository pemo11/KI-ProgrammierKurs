#! usr/bin/env python3
# file: KMeansVSHierachicalClustering.py

import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
from scipy.cluster.hierarchy import dendrogram, linkage, fcluster

# 1. Daten erstellen
X, y = make_blobs(n_samples=300, centers=4, cluster_std=1.0, random_state=42)

# 2. k-Means Clustering
kmeans = KMeans(n_clusters=4, random_state=42)
kmeans_labels = kmeans.fit_predict(X)

# 3. Hierarchical Clustering (Agglomerative)
linkage_matrix = linkage(X, method='ward')
hierarchical_labels = fcluster(linkage_matrix, t=4, criterion='maxclust')

# 4. Visualisierung
fig, ax = plt.subplots(1, 3, figsize=(18, 6))

# Original Daten
ax[0].scatter(X[:, 0], X[:, 1], c='gray', edgecolor='k', s=50)
ax[0].set_title("Original Data (ohne Labels)")

# k-Means Ergebnis
ax[1].scatter(X[:, 0], X[:, 1], c=kmeans_labels, cmap='viridis', edgecolor='k', s=50)
ax[1].set_title("k-Means Clustering")

# Hierarchical Clustering Ergebnis
ax[2].scatter(X[:, 0], X[:, 1], c=hierarchical_labels, cmap='viridis', edgecolor='k', s=50)
ax[2].set_title("Hierarchical Clustering")

plt.show()

# 5. Dendrogramm für Hierarchical Clustering
plt.figure(figsize=(10, 7))
dendrogram(linkage_matrix)
plt.title("Dendrogram of Hierarchical Clustering")
plt.xlabel("Data Points")
plt.ylabel("Distance")
plt.show()
