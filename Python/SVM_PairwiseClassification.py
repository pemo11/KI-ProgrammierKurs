#! usr/bin/env python3
# file: SVM_PairwiseClassification.py

import numpy as np
import matplotlib.pyplot as plt
from sklearn.svm import SVC
from sklearn.datasets import make_blobs
from sklearn.multiclass import OneVsOneClassifier

# 1. Generate synthetic data (similar to your diagram)
X, y = make_blobs(n_samples=100, centers=[(1, 4), (5, 5), (3, 1)], cluster_std=0.8, random_state=42)

# Labels: 1, 2, 3 (as in the diagram)
y = y + 1

# 2. Train an SVM with One-vs-One strategy
# Linear kernel is used for simplicity
model = OneVsOneClassifier(SVC(kernel='linear', random_state=42))
model.fit(X, y)

# 3. Plot decision boundaries
def plot_decision_boundaries(X, y, model):
    # Create a grid of points
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx, yy = np.meshgrid(np.linspace(x_min, x_max, 200),
                         np.linspace(y_min, y_max, 200))
    
    # Predict on the grid
    Z = model.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    
    # Plot decision boundaries
    plt.contourf(xx, yy, Z, alpha=0.3, cmap=plt.cm.coolwarm)
    plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.coolwarm, edgecolor='k', s=50)
    plt.xlabel("x1")
    plt.ylabel("x2")
    plt.title("SVM with Pairwise (One-vs-One) Classification")
    plt.show()

# Visualize the decision boundaries
plot_decision_boundaries(X, y, model)

# 4. Test prediction
new_points = np.array([[2, 4], [4, 3], [6, 6]])
predicted_labels = model.predict(new_points)

# Display predictions
for point, label in zip(new_points, predicted_labels):
    print(f"Point {point} is predicted to belong to class {label}")
