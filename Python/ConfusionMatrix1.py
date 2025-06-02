import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, precision_score, recall_score, accuracy_score
import seaborn as sns

predictions = np.array([0, 0, 1, 1, 0, 0, 2, 2, 1, 0])
ground_truth = np.array([0, 1, 1, 1, 1, 0, 2, 2, 2, 2])
class_names = ["Cat", "Dog", "Squirrel"]


# Confusion Matrix
cm = confusion_matrix(ground_truth, predictions)

#Calculate Metrics
precision = precision_score(ground_truth, predictions, average=None)
recall = recall_score(ground_truth, predictions, average=None)
accuracy = accuracy_score(ground_truth, predictions)

print("Confusion Matrix:\n", cm)
print("\nPrecision (Cat, Dog, Squirrel):", precision)
print("Recall (Cat, Dog, Squirrel):", recall)
print("Accuracy:", accuracy)


#Visualizing Confusion Matrix
plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", 
            xticklabels=class_names, yticklabels=class_names)
plt.xlabel("Predicted Labels")
plt.ylabel("True Labels")
plt.title("Confusion Matrix")
plt.show()