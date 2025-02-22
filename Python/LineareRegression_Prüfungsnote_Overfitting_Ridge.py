#! usr/env/bin python3
# LineareRegression_Prüfungsnote_Overfitting_Ridge.py

import numpy as np
import pandas as pd
from sklearn.linear_model import Ridge
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Beispiel-Daten: [Lernaufwand, Vorlesungszeit, Karteikarten (0/1)]

# Zufälligen Datensatz erstellen mit z.B. 1000 Studenten
studentCount = 1000
np.random.seed(42)

learning_hours = np.random.randint(5, 20, studentCount)
lecture_hours = np.random.randint(15, 30, studentCount)
flashcards = np.random.randint(0, 2, studentCount)

# Simuliere Noten mit einer Formel
# Note = 3.5 - 0.05 * Lernaufwand + 0.02 * Vorlesungszeit + 0.1 * Karteikarten + Zufallsfehler
grades = (3.5
          - 0.05 * learning_hours 
          - 0.02 * lecture_hours 
          - 0.1 * flashcards
          + np.random.normal(0, 0.5, studentCount)).round(2)

student_data = pd.DataFrame({
    "Lernaufwand": learning_hours,
    "Vorlesungszeit": lecture_hours,
    "Karteikarten": flashcards,
    "Note": grades
})

print(student_data.head())

X = student_data[["Lernaufwand", "Vorlesungszeit", "Karteikarten"]].values
Y = student_data["Note"].values

# Daten in Trainings- und Testdaten aufteilen
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=0)

# Modell erstellen
model = Ridge(alpha=1.0)
model.fit(X_train, y_train)

# Vorhersage treffen
y_train_predicted_grade = model.predict(X_train)
y_test_predicted_grade = model.predict(X_test)

# Fehler berechnen (MSE)
train_error = mean_squared_error(y_train, y_train_predicted_grade)
test_error = mean_squared_error(y_test, y_test_predicted_grade)

print(f"Trainingsfehler (MSE): {train_error:.2f}")
print(f"Testfehler (MSE): {test_error:.2f}")

# Ausgabe der Kooeffizienten
print(f"Koeffizienten: {model.coef_}")
