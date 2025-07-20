import numpy as np

# Eingabewort
text = "HEULEN"
text = "HALLO"

# Buchstaben als einfache Werte
buchstaben = {
    'H': 1.0,
    'A': 0.5,
    'L': 0.8,
    'O': 0.2,
    'E': 0.6,
    'U': 0.4,
    'N': 0.3,
    'C': 0.9
}

# Gewichte (manuell festgelegt)
w_input = 0.6
w_hidden = 0.4

# Initialzustand
hidden_state = 0.0

# Aktivierungsfunktion
def tanh(x):
    return np.tanh(x)

# Verarbeitung des Wortes
for buchstabe in text:
    x = buchstaben.get(buchstabe, 0.0)
    hidden_state = tanh(w_input * x + w_hidden * hidden_state)

# Klassifikation mit 3 Kategorien → simulierte Gewichtsmatrix (3 Neuronen)
W_out = np.array([[-1.0],   # für Gruß
                  [ 1.5],   # für Gefühl
                  [-0.5]])  # für Frage

# Bias-Terme für jede Kategorie (manuell)
b_out = np.array([0.1, 0.2, 0.3])

# Ausgabe berechnen: y = W_out * h + b
raw_output = W_out @ np.array([[hidden_state]]) + b_out.reshape(-1, 1)

# Softmax-Funktion zur Wahrscheinlichkeitsverteilung
def softmax(x):
    e_x = np.exp(x - np.max(x))  # numerische Stabilität
    return e_x / np.sum(e_x)

# Wahrscheinlichkeiten
probs = softmax(raw_output)

# Ausgabe
kategorien = ["Gruß", "Gefühl", "Frage"]
for i, k in enumerate(kategorien):
    print(f"{k:>7}: {probs[i,0]:.4f}")
