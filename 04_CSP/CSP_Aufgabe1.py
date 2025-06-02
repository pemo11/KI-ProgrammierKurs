# file: CSP_Aufgabe1.py
# Erstellt: 20/01/25

from constraint import Problem

# CSP-Problem erstellen
problem = Problem()

# Variablen mit ihren Domänen hinzufügen
colors = ["Rot", "Blau", "Grün"]
nodes = ["A", "B", "C", "D"]
for node in nodes:
    problem.addVariable(node, colors)

# Nebenbedingungen definieren (keine zwei benachbarten Knoten dürfen dieselbe Farbe haben)
edges = [("A", "B"), ("A", "C"), ("A", "D"), ("B", "D"), ("C", "D")]
for edge in edges:
    problem.addConstraint(lambda x, y: x != y, edge)

# Lösung finden
solutions = problem.getSolutions()

# Ergebnisse anzeigen
print(f"Anzahl der Lösungen: {len(solutions)}")
for solution in solutions:
    print(solution)
