# file: ASternSuche2.py
# erstellt: 20/01/25

import matplotlib.pyplot as plt
import heapq

def a_star_algorithm_visualized(start, ziel, hindernisse, grid_size):
    """Implementierung des A*-Algorithmus mit Visualisierung."""
    def heuristik(n, ziel):
        """Berechnet die Heuristik (Manhattan-Distanz)."""
        return abs(n[0] - ziel[0]) + abs(n[1] - ziel[1])

    def nachbarn(node):
        """Liefert die gültigen Nachbarn eines Knotens."""
        x, y = node
        möglichkeiten = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
        return [
            (nx, ny)
            for nx, ny in möglichkeiten
            if 0 <= nx < grid_size[0] and 0 <= ny < grid_size[1] and (nx, ny) not in hindernisse
        ]

    # Priority Queue (für die offene Liste)
    offene_liste = []
    heapq.heappush(offene_liste, (0, start))

    # Zurückgelegte Kosten (g) und Heuristik (h)
    g = {start: 0}
    f = {start: heuristik(start, ziel)}
    vorgänger = {start: None}
    geschlossene_liste = []

    while offene_liste:
        _, aktueller_knoten = heapq.heappop(offene_liste)

        # Ziel erreicht
        if aktueller_knoten == ziel:
            # Pfad rekonstruieren
            pfad = []
            while aktueller_knoten:
                pfad.append(aktueller_knoten)
                aktueller_knoten = vorgänger[aktueller_knoten]
            return pfad[::-1], geschlossene_liste  # Rückgabe des Pfads und besuchter Knoten

        # Nachbarn untersuchen
        geschlossene_liste.append(aktueller_knoten)
        for nachbar in nachbarn(aktueller_knoten):
            neue_kosten = g[aktueller_knoten] + 1  # Standardkosten für jeden Schritt
            if nachbar not in g or neue_kosten < g[nachbar]:
                g[nachbar] = neue_kosten
                f[nachbar] = neue_kosten + heuristik(nachbar, ziel)
                vorgänger[nachbar] = aktueller_knoten
                heapq.heappush(offene_liste, (f[nachbar], nachbar))

    return None, geschlossene_liste  # Kein Pfad gefunden

def zeichne_spielfeld(start, ziel, hindernisse, grid_size, pfad, geschlossene_liste):
    """Visualisiert das gesamte Spielfeld und den A*-Algorithmus."""
    plt.figure(figsize=(8, 8))
    plt.grid(True)
    plt.xticks(range(grid_size[0]))
    plt.yticks(range(grid_size[1]))
    plt.xlim(-0.5, grid_size[0] - 0.5)
    plt.ylim(-0.5, grid_size[1] - 0.5)

    # Hindernisse zeichnen
    for (hx, hy) in hindernisse:
        plt.scatter(hx, hy, color="red", s=200, label="Hindernis" if (hx, hy) == hindernisse[0] else "")

    # Besuchte Knoten zeichnen
    for (vx, vy) in geschlossene_liste:
        plt.scatter(vx, vy, color="lightblue", s=100, label="Besuchte Knoten" if (vx, vy) == geschlossene_liste[0] else "")

    # Pfad zeichnen
    for (px, py) in pfad:
        plt.scatter(px, py, color="blue", s=200, label="Pfad" if (px, py) == pfad[0] else "")

    # Start und Ziel zeichnen
    plt.scatter(*start, color="green", s=300, label="Start")
    plt.scatter(*ziel, color="yellow", s=300, edgecolors="black", label="Ziel")

    # Legende anzeigen
    plt.legend(loc="upper left")
    plt.title("A*-Algorithmus: Alle Schritte")
    plt.show()


# Spielfeldparameter
start = (0, 0)
ziel = (5, 5)
hindernisse = [(1, 1), (1,4), (2, 2), (2,5), (2,8), (3, 3), (3,6)]
grid_size = (7, 7)

# A*-Algorithmus ausführen
pfad, geschlossene_liste = a_star_algorithm_visualized(start, ziel, hindernisse, grid_size)

# Visualisierung anzeigen
if pfad:
    zeichne_spielfeld(start, ziel, hindernisse, grid_size, pfad, geschlossene_liste)
    print("Gefundener Pfad:", pfad)
else:
    print("Kein Pfad gefunden!")
