
# Erneut benötigte Bibliotheken importieren, da der Code-Zustand zurückgesetzt wurde
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import tree

# Anzahl der Studenten (Datenpunkte)
num_students = 50

# Zufällige, plausible Daten generieren
np.random.seed(42)  # Für Reproduzierbarkeit
student_data = {
    "Stunden gelernt": np.random.randint(3, 20, num_students),  # 3 bis 20 Stunden gelernt
    "Vorlesungen besucht (%)": np.random.randint(30, 100, num_students),  # 30% bis 100%
    "Nachhilfe": np.random.choice([0, 1], num_students),  # 0 = Nein, 1 = Ja
}


# Neue, noch strengere Logik für "Prüfung bestanden", um eine bessere Verteilung zu erzeugen
def predict_passed(hours, lectures, tutoring):
    probability = (hours / 30) + (lectures / 150) + (0.02 if tutoring else 0.0)  # Noch strengere Bedingungen
    return 1 if probability > 0.5 else 0  # Mehr Nicht-Bestehen-Werte forcieren

# Neue Label-Spalte erstellen
student_data["Prüfung bestanden"] = [
    predict_passed(h, l, t) for h, l, t in zip(student_data["Stunden gelernt"], student_data["Vorlesungen besucht (%)"], student_data["Nachhilfe"])
]

# In DataFrame umwandeln
student_df = pd.DataFrame(student_data)

print(student_df)

# Überprüfung der Klassenverteilung nach der Anpassung
student_df["Prüfung bestanden"].value_counts()

# Label-Spalte erstellen
student_data["Prüfung bestanden"] = [
    predict_passed(h, l, t) for h, l, t in zip(student_data["Stunden gelernt"], student_data["Vorlesungen besucht (%)"], student_data["Nachhilfe"])
]

# In DataFrame umwandeln
student_df = pd.DataFrame(student_data)

# Decision Tree Modell trainieren
student_model = tree.DecisionTreeClassifier(criterion="entropy")
X_student = student_df.drop(columns=["Prüfung bestanden"])
y_student = student_df["Prüfung bestanden"]
student_model.fit(X_student, y_student)

# Visualisierung des Entscheidungsbaums
plt.figure(figsize=(12, 8))
tree.plot_tree(student_model, feature_names=["Stunden gelernt", "Vorlesungen (%)", "Nachhilfe"],
               class_names=["Nicht bestanden", "Bestanden"], filled=True)
plt.show()
