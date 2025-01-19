#! usr/env/bin python3
# file: Dendogram_ClusterQualitaet.py

import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.datasets import make_blobs

# 1. Daten generieren
X, y = make_blobs(n_samples=100, centers=3, cluster_std=1.2, random_state=42)

# 2. Hierarchisches Clustering (Agglomerative)
# Verwende die Ward-Methode, um die Summe der quadrierten Abstände zu minimieren
linkage_matrix = linkage(X, method='ward')

# 3. Dendrogramm erstellen
plt.figure(figsize=(12, 6))
dendrogram(linkage_matrix, truncate_mode='level', p=5, leaf_rotation=90, leaf_font_size=10)
plt.title("Dendrogramm - Hierarchical Clustering")
plt.xlabel("Datenpunkte oder Cluster")
plt.ylabel("Distanz (Höhe der Verbindung)")
plt.axhline(y=10, color='r', linestyle='--', label="Cluster-Schnittpunkt (Höhe = 10)")
plt.legend()
plt.show()

# 4. Cluster-Anzahl bestimmen
from scipy.cluster.hierarchy import fcluster

# Schneide das Dendrogramm bei einer bestimmten Höhe (z. B. 10)
cluster_labels = fcluster(linkage_matrix, t=10, criterion='distance')

# 5. Visualisierung der Cluster
plt.figure(figsize=(8, 6))
plt.scatter(X[:, 0], X[:, 1], c=cluster_labels, cmap='viridis', edgecolor='k', s=50)
plt.title("Cluster-Zuordnung basierend auf Dendrogramm")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.show()
