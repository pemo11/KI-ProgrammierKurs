#! usr/bin/env python3
# file: SVM_OvoVsOvR.py

import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.svm import SVC
from sklearn.multiclass import OneVsOneClassifier, OneVsRestClassifier
from sklearn.metrics import accuracy_score

# 1. Generate synthetic data
X, y = make_blobs(n_samples=150, centers=3, cluster_std=1.2, random_state=42)
# Classes: 0, 1, 2

# 2. Create SVM classifiers
ovo_classifier = OneVsOneClassifier(SVC(kernel='linear', random_state=42))
ovr_classifier = OneVsRestClassifier(SVC(kernel='linear', random_state=42))

# 3. Fit both classifiers
ovo_classifier.fit(X, y)
ovr_classifier.fit(X, y)

# 4. Predictions for training data
y_pred_ovo = ovo_classifier.predict(X)
y_pred_ovr = ovr_classifier.predict(X)

# 5. Calculate accuracy
accuracy_ovo = accuracy_score(y, y_pred_ovo)
accuracy_ovr = accuracy_score(y, y_pred_ovr)

print(f"Accuracy (One-vs-One): {accuracy_ovo:.2f}")
print(f"Accuracy (One-vs-Rest): {accuracy_ovr:.2f}")

# 6. Plot decision boundaries
def plot_decision_boundaries(X, y, model, title):
    # Create a meshgrid for the feature space
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx, yy = np.meshgrid(np.linspace(x_min, x_max, 200),
                         np.linspace(y_min, y_max, 200))
    # Predict over the grid
    Z = model.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)

    # Plot decision boundaries and data points
    plt.contourf(xx, yy, Z, alpha=0.3, cmap=plt.cm.coolwarm)
    plt.scatter(X[:, 0], X[:, 1], c=y, edgecolor='k', cmap=plt.cm.coolwarm)
    plt.title(title)
    plt.xlabel("Feature 1")
    plt.ylabel("Feature 2")
    plt.show()

# Plot OvO decision boundaries
plot_decision_boundaries(X, y, ovo_classifier, "One-vs-One (OvO) Decision Boundaries")

# Plot OvR decision boundaries
plot_decision_boundaries(X, y, ovr_classifier, "One-vs-Rest (OvR) Decision Boundaries")
