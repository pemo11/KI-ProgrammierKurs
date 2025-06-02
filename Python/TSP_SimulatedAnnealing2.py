#! usr/bin/python3
# file: TSP_SimulatedAnnealing2.py

import numpy as np
import random
import pandas as pd
# import ace_tools as tools

# Distanzmatrix für die 8 Städte
dist_matrix = np.array([
    [0, 280, 150, 400, 450, 480, 680, 790],
    [280, 0, 250, 600, 550, 200, 800, 580],
    [150, 250, 0, 300, 350, 400, 600, 500],
    [400, 600, 300, 0, 180, 600, 450, 580],
    [450, 550, 350, 180, 0, 600, 300, 400],
    [480, 200, 400, 600, 600, 0, 750, 450],
    [680, 800, 600, 450, 300, 750, 0, 300],
    [790, 580, 500, 580, 400, 450, 300, 0]
])

# Städte-Liste
cities = list(range(8))

# Funktion zur Berechnung der Gesamtdistanz einer Route
def total_distance(route, dist_matrix):
    distance = sum(dist_matrix[route[i], route[i + 1]] for i in range(len(route) - 1))
    distance += dist_matrix[route[-1], route[0]]  # Rückkehr zur Startstadt
    return distance

# Simulated Annealing Algorithmus
def simulated_annealing(dist_matrix, initial_temp=1000, cooling_rate=0.99, min_temp=1e-3, max_iterations=10000):
    current_route = random.sample(cities, len(cities))  # Zufällige Startlösung
    current_distance = total_distance(current_route, dist_matrix)
    best_route = current_route[:]
    best_distance = current_distance

    temperature = initial_temp

    for iteration in range(max_iterations):
        # Zwei zufällige Städte tauschen
        new_route = current_route[:]
        i, j = random.sample(range(len(cities)), 2)
        new_route[i], new_route[j] = new_route[j], new_route[i]

        # Neue Distanz berechnen
        new_distance = total_distance(new_route, dist_matrix)

        # Entscheidung: Akzeptieren oder nicht?
        if new_distance < current_distance or random.random() < np.exp((current_distance - new_distance) / temperature):
            current_route = new_route
            current_distance = new_distance

            # Beste Lösung aktualisieren
            if current_distance < best_distance:
                best_route = current_route[:]
                best_distance = current_distance

        # Temperatur verringern
        temperature *= cooling_rate

        # Abbruchbedingung
        if temperature < min_temp:
            break

    return best_route, best_distance

# Algorithmus ausführen
best_route, best_distance = simulated_annealing(dist_matrix)

# Städte-Namen
city_names = ["Hamburg", "Berlin", "Hannover", "Köln", "Frankfurt", "Dresden", "Freiburg", "München"]
best_route_named = [city_names[i] for i in best_route] + [city_names[best_route[0]]]  # Rückkehr zur Startstadt


# Farben für die Städte definieren
city_colors = {
    "Hamburg": "red", "Berlin": "blue", "Hannover": "green",
    "Köln": "orange", "Frankfurt": "purple", "Dresden": "cyan",
    "Freiburg": "magenta", "München": "yellow"
}

# Distanzmatrix für die 8 Städte (gleiche wie zuvor)
distances = {
    ("Hamburg", "Berlin"): 280, ("Berlin", "Hannover"): 250, ("Hannover", "Köln"): 300,
    ("Köln", "Frankfurt"): 180, ("Frankfurt", "Dresden"): 600, ("Dresden", "Freiburg"): 750,
    ("Freiburg", "München"): 300, ("München", "Hamburg"): 790
}

import networkx as nx
import matplotlib.pyplot as plt

# Beste gefundene Route (Beispiel)
best_route = ["Hamburg", "Berlin", "Hannover", "Köln", "Frankfurt", "Dresden", "Freiburg", "München", "Hamburg"]

# Erstelle einen gerichteten Graphen für die Route
G = nx.DiGraph()

# Kanten entsprechend der gefundenen Route hinzufügen
edges = [(best_route[i], best_route[i + 1]) for i in range(len(best_route) - 1)]
G.add_edges_from(edges)

# Positionen für eine bessere Darstellung (manuell angepasst)
positions = {
    "Hamburg": (0, 4), "Berlin": (3, 6), "Hannover": (2, 4),
    "Köln": (0, 2), "Frankfurt": (2, 2), "Dresden": (4, 5),
    "Freiburg": (1, 0), "München": (4, 1)
}

# Zeichnen des Graphen mit individuellen Farben für die Städte
# Farben den Knoten zuweisen
node_colors = [city_colors[city] for city in G.nodes()]

plt.figure(figsize=(8, 6))
nx.draw(G, pos=positions, with_labels=True, node_color=node_colors, node_size=2000, font_size=10, font_weight="bold", edge_color="black", arrows=True)

# Kantenbeschriftung mit den Distanzen
edge_labels = {edge: f"{distances[edge]} km" for edge in distances}
nx.draw_networkx_edge_labels(G, pos=positions, edge_labels=edge_labels, font_size=10)

# Anzeigen des Graphen
plt.title("Optimierte Route mit Simulated Annealing (Städte mit individuellen Farben)")
plt.show()

