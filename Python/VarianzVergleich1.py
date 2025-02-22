#! usr/env/python3
# Vergleich des Varianz-Einflusses in der linearen Regression mit verschiedenen Modellen
# mit zufälligen Daten, insgesamt 10 Modelle
# Erstellt am 25/01/25

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Seed für reproduzierbare Ergebnisse
np.random.seed(42)

# Erstelle zufällige Daten
def generate_data(size=100):
    X = np.random.uniform(0, 10, size).reshape(-1, 1)
    y = 2 * X + 1 + np.random.normal(0, 1, size).reshape(-1, 1)
    return X, y

# Initialisieren von Modellen und Arrays für Vorhersagen
models = []
predictions = []

# Mehrere Modelle trainieren, um die Varianz zu vergleichen
for i in range(10):
    X, y = generate_data()
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    model = LinearRegression()
    model.fit(X_train, y_train)
    models.append(model)
    # Vorhersagen für Testdaten speichern
    y_pred = model.predict(X_test)
    predictions.append(y_pred)


# Testdatenpunkt (fixiert für alle Modelle)
X_test_fixed = np.linspace(0, 10, 100).reshape(-1, 1)

# Plotten der verschiedenen Modelle
plt.figure(figsize=(10, 6))
for i, model in enumerate(models):
    y_pred_fixed = model.predict(X_test_fixed)
    plt.plot(X_test_fixed, y_pred_fixed, label=f"Model {i+1}")

# Ursprüngliche Daten plotten
X_full, y_full = generate_data(size=100)
plt.scatter(X_full, y_full,  color="gray", alpha=0.5, label="Originldaten")

plt.title("Varianz in der linearen Regression")
plt.xlabel("Eingabe (X)")
plt.ylabel("Ausgabe (y)")
plt.legend()
plt.show()
