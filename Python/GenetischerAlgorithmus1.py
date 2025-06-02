#! env/usr/bin/python3
# file: GenetischerAlgorithmus1.py
# Es soll das Maximum der Funktion f(x) = x^2 für x in [0, 31] gefunden werden.

import random

# Parameter
POP_SIZE = 6            # Anzahl der Individuen
GENES = 5               # 5-Bit-Zahlen (Werte von 0 bis 31)
MUTATION_RATE = 0.1     # Wahrscheinlichkeit der Mutation
GENERATIONS = 20        # Anzahl der Iterationen

# Fitness-Funktion: f(x) = x^2
def fitness(x):
    return x ** 2

# Erstellt eine zufällige Binärpopulation
def create_population(size):
    return [random.randint(0, 31) for _ in range(size)]

# Selektiert die besten Individuen basierend auf Fitness
def selection(pop):
    return sorted(pop, key=fitness, reverse=True)[:2]  # Top 2

# Führt Crossover zwischen zwei Eltern durch
def crossover(parent1, parent2):
    point = random.randint(1, GENES - 1)  # Zufälliger Punkt zum Teilen
    mask = (1 << point) - 1  # Maske für den unteren Teil
    child1 = (parent1 & mask) | (parent2 & ~mask)
    child2 = (parent2 & mask) | (parent1 & ~mask)
    return child1, child2

# Führe zufällige Mutation durch
def mutate(x):
    if random.random() < MUTATION_RATE:
        bit = 1 << random.randint(0, GENES - 1)  # Zufälliges Bit umschalten
        x ^= bit  # XOR-Operation für Mutation
    return x

# Hauptfunktion des genetischen Algorithmus
def genetic_algorithm():
    population = create_population(POP_SIZE)
    
    for generation in range(GENERATIONS):
        population = sorted(population, key=fitness, reverse=True)  # Beste zuerst
        
        print(f"Generation {generation}: Beste Lösung = {population[0]}, Fitness = {fitness(population[0])}")
        
        new_population = selection(population)  # Wähle die besten Eltern
        
        # Erzeuge neue Kinder durch Crossover und Mutation
        while len(new_population) < POP_SIZE:
            p1, p2 = random.sample(new_population, 2)
            child1, child2 = crossover(p1, p2)
            new_population.extend([mutate(child1), mutate(child2)])
        
        population = new_population[:POP_SIZE]  # Halte Population konstant
    
    best = max(population, key=fitness)
    print(f"\nBeste gefundene Lösung: x = {best}, f(x) = {fitness(best)}")

# Starte den Algorithmus
genetic_algorithm()
