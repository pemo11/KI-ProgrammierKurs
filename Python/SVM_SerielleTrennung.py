#! usr/bin/env python3
# file: SVM_SerielleTrennung.py

import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.svm import SVC

# 1. Daten erzeugen (zweidimensional, für visuelle Darstellung)
X, y = make_blobs(n_samples=100, centers=2, random_state=6, cluster_std=1.5)

# 2. Lineare SVM (für lineare Trennung)
linear_svm = SVC(kernel='linear', C=1)
linear_svm.fit(X, y)

# 3. Nicht-lineare SVM (mit RBF-Kernel, für nicht-lineare Trennung)
rbf_svm = SVC(kernel='rbf', C=1, gamma=0.5)
rbf_svm.fit(X, y)

# 4. Hilfsfunktion: Entscheidungsgrenzen plotten
def plot_decision_boundary(model, ax, title):
    # Erstelle ein Raster von Punkten
    xx, yy = np.meshgrid(np.linspace(X[:, 0].min()-1, X[:, 0].max()+1, 100),
                         np.linspace(X[:, 1].min()-1, X[:, 1].max()+1, 100))
    Z = model.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    
    # Entscheidungsgrenze und Punkte plotten
    ax.contourf(xx, yy, Z, alpha=0.3, cmap=plt.cm.coolwarm)
    ax.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.coolwarm, edgecolor='k', s=50)
    ax.set_title(title)

# 5. Visualisierung
fig, ax = plt.subplots(1, 2, figsize=(12, 6))

# Lineare SVM
plot_decision_boundary(linear_svm, ax[0], "Lineare SVM")

# Nicht-lineare SVM (RBF)
plot_decision_boundary(rbf_svm, ax[1], "Nicht-lineare SVM (RBF)")

plt.tight_layout()
plt.show()
