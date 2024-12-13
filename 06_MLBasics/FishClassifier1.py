#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Klassifikation von Fischen nach Länge und Dichte
-----------------------------------------------
"""

import random
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import numpy as np
import pandas as pd

# Generate realistic random data for 50 fishes
# Assumptions:
# - Sea bass: length ~ Uniform(20, 30) cm, density ~ Uniform(0.8, 1.0)
# - Salmon: length ~ Uniform(25, 40) cm, density ~ Uniform(0.5, 0.7)
data = []

for _ in range(25):  # Generate 25 sea bass
    length = random.uniform(20, 30)
    density = random.uniform(0.8, 1.0)
    data.append([length, density, 'sea bass'])

for _ in range(25):  # Generate 25 salmon
    length = random.uniform(25, 40)
    density = random.uniform(0.5, 0.7)
    data.append([length, density, 'salmon'])

# Convert to DataFrame
df = pd.DataFrame(data, columns=['length', 'density', 'species'])

# Split into features and labels
X = df[['length', 'density']]
y = df['species']

# Train a logistic regression classifier
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
classifier = LogisticRegression()
classifier.fit(X_train, y_train)

# Test classifier accuracy
accuracy = classifier.score(X_test, y_test)
print(f"Classifier accuracy: {accuracy * 100:.2f}%")

# Function to classify a new fish
def classify_fish(length, density):
    prediction = classifier.predict([[length, density]])[0]
    return prediction

# Interactive part
print("\nClassify a new fish")
while True:
    try:
        length = float(input("Enter fish length (cm): "))
        density = float(input("Enter fish density: "))
        species = classify_fish(length, density)
        print(f"The fish is likely a {species}.\n")
    except ValueError:
        print("Invalid input. Please enter numerical values for length and density.")
    except KeyboardInterrupt:
        print("\nExiting the classifier.")
        break