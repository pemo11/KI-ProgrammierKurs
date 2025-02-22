#! usr/env/bin python3
# file: LineareRegression_Prüfungsnote_Overfitting.py
# Overfitting erkennen

import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Beispiel-Daten: [Lernaufwand, Vorlesungszeit, Karteikarten (0/1)]

X = np.array([
                [10,20, 1],
                [15, 25, 0],
                [8, 18, 1],
                [12, 22, 0],
                [20, 30, 1],
                [18, 28, 1],
                [15, 25, 0],
                [10, 20, 1]
            ])

Y = np.array([2.0, 2.3, 1.8, 2.5, 1.5,2.8,1.6,3.0])

# Daten in Trainings- und Testdaten aufteilen
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=0)

# Modell erstellen
model = LinearRegression()
model.fit(X_train, y_train)

# Vorhersage treffen
y_train_predicted_grade = model.predict(X_train)
y_test_predicted_grade = model.predict(X_test)

# Fehler berechnen (MSE)
train_error1= np.mean((y_train - y_train_predicted_grade) ** 2)
test_error = np.mean((y_test - y_test_predicted_grade) ** 2)

from sklearn.metrics import mean_squared_error
train_error = mean_squared_error(y_train, y_train_predicted_grade)
test_error = mean_squared_error(y_test, y_test_predicted_grade)

print(f"Trainingsfehler (MSE): {train_error:.2f}")
print(f"Testfehler (MSE): {test_error:.2f}")

# Vergleich der Fehler
if train_error < test_error:
    print("Das Modell hat Overfitting")
else:
    print("Das Modell hat kein Overfitting")

