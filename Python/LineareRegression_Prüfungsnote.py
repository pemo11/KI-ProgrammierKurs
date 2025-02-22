#! usr/env/bin python3
# file: LineareRegression_Prüfungsnote.py
# Ein sehr einfaches Beispiel für lineare Regression

import numpy as np
from sklearn.linear_model import LinearRegression

# Beispiel-Daten: [Lernaufwand, Vorlesungszeit, Karteikarten (0/1)]

X = np.array([
                [10,20, 1],
                [15, 25, 0],
                [8, 18, 1],
                [12, 22, 0],
                [20, 30, 1]
            ])

Y = np.array([2.0, 2.3, 1.8, 2.5, 1.5])

# Modell erstellen
model = LinearRegression()
model.fit(X, Y)

# Vorhersage treffen
new_student = np.array([[18, 28, 1]])

predicted_grade = model.predict(new_student)
karteikarten_Modus = "mit" if new_student[0][2] == 1 else "ohne"
print(f"Notenvorhersage für {new_student[0][0]} Stunden Lernaufwand und {new_student[0][1]} Vorlesungszeit {karteikarten_Modus} Karteikarten={predicted_grade[0]:.2f}")
      
