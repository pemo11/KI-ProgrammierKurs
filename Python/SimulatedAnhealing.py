#!/usr/bin/env python3
# Simulated Annealing Algorithmus zur Optimierung
# Erstellt am 27/01/25

import numpy as np
import matplotlib.pyplot as plt

# Ziel: Funktion mit mehreren lokalen Minima
# f(x) = x^4 - 2x^2 + 0.5
def objective_function(x):
    return x**4 - 2 * x**2 + 0.5

# Simulated Annealing Algorithmus
def simulated_annealing(objective_function, bounds, max_iter, initial_temp, cooling_rate):
    # Starte mit einem zufälligen Punkt im Bereich der Grenzen
    current_x = np.random.uniform(bounds[0], bounds[1])
    current_energy = objective_function(current_x)

    best_x = current_x
    best_energy = current_energy

    temperature = initial_temp

    # Iteriere über die maximale Anzahl an Iterationen
    for i in range(max_iter):
        # Wähle einen neuen Punkt in der Nähe (Nachbarschaftssuche)
        new_x = current_x + np.random.uniform(-0.1, 0.1)

        # Begrenze den neuen Punkt auf die Grenzen
        new_x = np.clip(new_x, bounds[0], bounds[1])
        new_energy = objective_function(new_x)

        # Energieunterschied berechnen
        delta_energy = new_energy - current_energy

        # Akzeptanzregel: Nehme neuen Punkt an, wenn Energie geringer ist oder mit gewisser Wahrscheinlichkeit
        if delta_energy < 0 or np.random.rand() < np.exp(-delta_energy / temperature):
            current_x = new_x
            current_energy = new_energy

            # Aktualisiere das beste Ergebnis, falls der Punkt besser ist
            if current_energy < best_energy:
                best_x = current_x
                best_energy = current_energy

        # Temperatur reduzieren (Abkühlen)
        temperature *= cooling_rate

    return best_x, best_energy

# Parameter definieren
bounds = [-2, 2]  # Grenzen für x
max_iter = 1000   # Maximale Iterationen
initial_temp = 10 # Anfangstemperatur
cooling_rate = 0.95 # Abkühlrate

# Simulated Annealing ausführen
best_x, best_energy = simulated_annealing(objective_function, bounds, max_iter, initial_temp, cooling_rate)

print(f"Globales Minimum gefunden bei x = {best_x}, f(x) = {best_energy}")

# Visualisierung der Funktion und des globalen Minimums
x = np.linspace(bounds[0], bounds[1], 500)
y = objective_function(x)

plt.plot(x, y, label="f(x) = x^4 - 2x^2 + 0.5")
plt.scatter(best_x, best_energy, color="red", label="Gefundenes Minimum")
plt.title("Simulated Annealing: Finden des globalen Minimums")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.show()
