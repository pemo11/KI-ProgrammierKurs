#! /usr/bin/env python3
# Cross-Validierung mit einem Entscheidungsbaum
# Damit soll die Bewertung des Modells verbessert werden.

# Erstellt am 26/01/25

from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Den Iris-Datensatz laden
data = load_iris()
X = data.data  # Eingabedaten (Merkmale)
y = data.target  # Zielvariablen (Labels)

# Modell definieren (z. B. Entscheidungsbaum)
model = DecisionTreeClassifier(random_state=42)

# Daten aufteilen
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Modell trainieren
model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)

# Genauigkeit auf Testdaten
accuracy = accuracy_score(y_test, model.predict(X_test))
print("Genauigkeit ohne Cross-Validierung:", accuracy)

# Modell noch einmal definieren
model = DecisionTreeClassifier(random_state=42)

# 5-fache Cross-Validierung
scores = cross_val_score(model, X, y, cv=5)

# Ergebnisse anzeigen
print("Einzelergebnisse der Cross-Validierung:", scores)
print("Mittlere Genauigkeit:", scores.mean())
print("Standardabweichung:", scores.std())
