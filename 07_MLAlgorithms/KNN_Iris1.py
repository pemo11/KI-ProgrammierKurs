# file: KNN_Iris.py

# Importieren der benötigten Bibliotheken
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# Laden des Iris-Datensatzes
iris = load_iris()
X = iris.data  # Merkmale (Blütenmaße)
y = iris.target  # Zielvariablen (Blumenarten)

# Aufteilen des Datensatzes in Trainings- und Testdaten
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Erstellen und Trainieren des k-NN-Modells
k = 3  # Anzahl der Nachbarn
knn = KNeighborsClassifier(n_neighbors=k)
knn.fit(X_train, y_train)

# Vorhersagen auf den Testdaten
y_pred = knn.predict(X_test)

# Bewertung des Modells
accuracy = accuracy_score(y_test, y_pred)
print(f"Genauigkeit des Modells: {accuracy * 100:.2f}%")

# Beispielvorhersage für eine neue Blume
neue_blume = [[5.0, 3.5, 1.4, 0.2]]  # Werte für Blütenmaße
vorhersage = knn.predict(neue_blume)
print(f"Vorhergesagte Klasse: {iris.target_names[vorhersage[0]]}")
