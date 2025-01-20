# file: BFSAufgabe1.py
# Erstellt 20/01/25
# Gibt auch die besuchten Knoten aus

from collections import deque

def bfs(start, ziel, graph):
    """Implementierung von Breadth-First Search (BFS), um den kürzesten Pfad und besuchte Knoten zu finden."""
    # Warteschlange und Vorgängerliste
    warteschlange = deque([start])
    vorgänger = {start: None}
    besucht = []  # Liste für die besuchten Knoten

    while warteschlange:
        aktueller_knoten = warteschlange.popleft()

        # Knoten als besucht markieren
        besucht.append(aktueller_knoten)

        # Ziel erreicht
        if aktueller_knoten == ziel:
            # Rekonstruiere den Pfad
            pfad = []
            while aktueller_knoten:
                pfad.append(aktueller_knoten)
                aktueller_knoten = vorgänger[aktueller_knoten]
            return pfad[::-1], besucht  # Pfad und besuchte Knoten zurückgeben

        # Nachbarn zur Warteschlange hinzufügen
        for nachbar in graph[aktueller_knoten]:
            if nachbar not in vorgänger:  # Nachbarn nur hinzufügen, wenn sie nicht bereits besucht sind
                vorgänger[nachbar] = aktueller_knoten
                warteschlange.append(nachbar)

    return None, besucht  # Kein Pfad gefunden, aber besuchte Knoten zurückgeben

# Beispielgraph (Adjazenzliste)
graph = {
    'A': ['B', 'C', 'D'],
    'B': ['E', 'F'],
    'C': [],
    'D': ['G'],
    'E': [],
    'F': ['G'],
    'G': []
}

# Start- und Zielknoten
start = 'A'
ziel = 'G'

# BFS ausführen
pfad, besucht = bfs(start, ziel, graph)

# Ergebnisse ausgeben
print("Besuchte Knoten in Reihenfolge:", besucht)
if pfad:
    print("Gefundener kürzester Pfad:", pfad)
else:
    print("Kein Pfad gefunden!")
