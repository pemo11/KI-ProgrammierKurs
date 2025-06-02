#! usr/bin/python3
# file: TSP_SimulatedAnnealing1.py

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

# Ergebnis ausgeben
result_df = pd.DataFrame({"Optimierte Route": best_route_named, "Index": best_route + [best_route[0]]})
# tools.display_dataframe_to_user(name="Optimierte Route mit Simulated Annealing", dataframe=result_df)

print(best_distance)
print(best_route_named)

import networkx as nx
import matplotlib.pyplot as plt

# Graph mit Städten als Knoten
# G = nx.Graph()
G = nx.DiGraph()
# edges = [("Hamburg", "Berlin"), ("Berlin", "München"), ("München", "Hamburg")]
edges = [(best_route_named[i], best_route_named[i + 1]) for i in range(len(best_route_named) - 1)]
G.add_edges_from(edges)

# Graph zeichnen
plt.figure(figsize=(5, 5))
nx.draw(G, with_labels=True, node_color="lightblue", node_size=2000, font_size=10)
plt.show()