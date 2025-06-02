#! env/usr/bin/python3
# file: DecisionTree_StudentData_InformationsGewinn.py

import math

# Hilfsfunktion zur Berechnung der Entropie
def berechne_entropie(daten):
    total = len(daten)
    if total == 0:
        return 0
    true_count = sum(1 for d in daten if d[-1] == True)
    false_count = total - true_count
    p_true = true_count / total
    p_false = false_count / total
    entropie = 0
    if p_true > 0:
        entropie -= p_true * math.log2(p_true)
    if p_false > 0:
        entropie -= p_false * math.log2(p_false)
    return entropie

# Berechnung des Informationsgewinns
def berechne_informationsgewinn(daten, feature_index, threshold):
    total_entropie = berechne_entropie(daten)
    left_split = [d for d in daten if d[feature_index] <= threshold]
    right_split = [d for d in daten if d[feature_index] > threshold]
    gewichtete_entropie = (
        len(left_split) / len(daten) * berechne_entropie(left_split) +
        len(right_split) / len(daten) * berechne_entropie(right_split)
    )
    informationsgewinn = total_entropie - gewichtete_entropie
    return informationsgewinn

# Trainingsdaten
daten = [
    [12, 80, 1, True],
    [8, 60, 1, True],
    [6, 40, 0, False],
    [10, 50, 0, False],
    [15, 90, 0, True]
]

# Features: Stunden gelernt, Vorlesungen besucht, Nachhilfe
features = ["Stunden gelernt", "Vorlesungen besucht", "Nachhilfe"]

# Auswahl des besten Features
bestes_Feature = None
bester_threshold = None
bester_gewinn = -1

for feature_index in range(len(features)):
    werte = set(d[feature_index] for d in daten)
    for threshold in werte:
        informationsgewinn = berechne_informationsgewinn(daten, feature_index, threshold)
        if informationsgewinn > bester_gewinn:
            bestes_feature = features[feature_index]
            bester_threshold = threshold
            bester_gewinn = informationsgewinn

print(f"Bestes Feature: {bestes_feature}")
print(f"Threshold: {bester_threshold}")
print(f"Informationsgewinn: {bester_gewinn:.4f}")
