# file: KNN_Iris3.py
# Versucht einen optimalen Wert für k zu finden, bei der die Genauigkeit maximal wird
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from os import path

from sklearn.model_selection import cross_val_score

file_path = path.join(path.dirname(__file__),  "iris_echt.csv")  # Pfad zur CSV-Datei
df = pd.read_csv(file_path)

# Merkmale und Zielwerte trennen
X = df[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']]  # Features
y = df['species']  # Zielwerte

# Aufteilen der Daten in Trainings- und Testdaten
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

accuracies = []
for k in range(1, 21):
    knn = KNeighborsClassifier(n_neighbors=k)
    scores = cross_val_score(knn, X_train, y_train, cv=5)
    accuracies.append(scores.mean())
print(f"Beste Genauigkeit: {max(accuracies):.2f} bei k = {accuracies.index(max(accuracies)) + 1}")
