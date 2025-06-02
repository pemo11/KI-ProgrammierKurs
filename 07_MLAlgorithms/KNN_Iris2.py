# file: KNN_Iris2.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from os import path

# CSV-Datei laden
# file_path = path.join(path.dirname(__file__),  "iris_daten.csv")  # Pfad zur CSV-Datei
file_path = path.join(path.dirname(__file__),  "iris_echt.csv")  # Pfad zur CSV-Datei
df = pd.read_csv(file_path)

# Merkmale und Zielwerte trennen
X = df[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']]  # Features
# y = df['target']  # Zielwerte
y = df['species']  # Zielwerte

# Aufteilen der Daten in Trainings- und Testdaten
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
neue_blume = pd.DataFrame(
    [[5.0, 3.5, 1.4, 0.2]],  # Werte für Blütenmaße
    columns=["sepal_length", "sepal_width", "petal_length", "petal_width"]  # Passende Spaltennamen
)
vorhersage = knn.predict(neue_blume)
print(f"Vorhergesagte Klasse: {vorhersage[0]}")
