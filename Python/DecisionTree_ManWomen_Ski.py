# file: DecisionTree_ManWomen_Ski.py

# Erstellt: 20/01/25

from sklearn.tree import DecisionTreeClassifier

# Trainingsdaten (Größe in cm, Gewicht in kg) und Labels (0 = Frau, 1 = Mann)
X=[[160, 60], [170, 70], [180, 80], [190, 90], [160, 50], [170, 60], [180, 70], [190, 80]]
Y=[0, 0, 0, 0, 1, 1, 1, 1]

# Modell erstellen
model = DecisionTreeClassifier()

# Modell trainieren
model.fit(X, Y)

# Vorhersage treffen
sample = [[165, 65]]
prediction = model.predict(sample)

# Ergebnis anzeigen
print(f"Vorhersage für {sample[0]}: {prediction}")

# Visualisierung des Entscheidungsbaums
from sklearn.tree import export_graphviz
from os import path
dotPath =  path.join(path.dirname(__file__), "tree.dot")
export_graphviz(model, out_file=dotPath, feature_names=["Größe", "Gewicht"], class_names=["Frau", "Mann"], filled=True)

# Umwandlung der .dot-Datei in ein Bild
import pydot
pngPath = path.join(path.dirname(__file__), "tree.png")
(graph,) = pydot.graph_from_dot_file(dotPath)
graph.write_png(pngPath)
print(f"Entscheidungsbaum wurde als {pngPath} gespeichert.")
