# ASternSuche1.prg
# Erstellt: 20/01/25

import heapq

def a_star_algorithm(start, ziel, hindernisse, grid_size):
    """Implementierung des A*-Algorithmus in einer 2D-Gitterwelt."""
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

    while offene_liste:
        _, aktueller_knoten = heapq.heappop(offene_liste)

        # Ziel erreicht
        if aktueller_knoten == ziel:
            # Pfad rekonstruieren
            pfad = []
            while aktueller_knoten:
                pfad.append(aktueller_knoten)
                aktueller_knoten = vorgänger[aktueller_knoten]
            return pfad[::-1], g, f  # Rückgabe des Pfads und der Kosten

        # Nachbarn untersuchen
        for nachbar in nachbarn(aktueller_knoten):
            neue_kosten = g[aktueller_knoten] + 1  # Standardkosten für jeden Schritt
            if nachbar not in g or neue_kosten < g[nachbar]:
                g[nachbar] = neue_kosten
                f[nachbar] = neue_kosten + heuristik(nachbar, ziel)
                vorgänger[nachbar] = aktueller_knoten
                heapq.heappush(offene_liste, (f[nachbar], nachbar))

    return None, g, f  # Kein Pfad gefunden

# Spielfeldparameter
start = (0, 0)
ziel = (5, 5)
hindernisse = [(1, 1), (2, 2), (3, 3)]
grid_size = (7, 7)

# A*-Algorithmus ausführen
pfad, g, f = a_star_algorithm(start, ziel, hindernisse, grid_size)

# Ergebnisse anzeigen
if pfad:
    print("Gefundener Pfad:", pfad)
    print("Kosten g(n):")
    for k in g:
        print(f"Knoten {k}: g(n) = {g[k]}")
    print("\nGesamtkosten f(n):")
    for k in f:
        print(f"Knoten {k}: f(n) = {f[k]}")
else:
    print("Kein Pfad gefunden!")
