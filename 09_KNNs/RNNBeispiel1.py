'''
Einfaches RNN-Beispiel in Python
Dies ist ein einfaches Beispiel für ein RNN, das Buchstaben klassifiziert.
Es verwendet eine manuelle Implementierung ohne Keras oder TensorFlow.
'''
import numpy as np

# Buchstabencodierung (manuell)
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


# Eingabe
text = "HALLO"  # Kategorie = "Gruß"
# Auch HEULEN wird der Kategorie Gruß zugeordnet
text = "HEULEN"  # Kategorie = "Empfindung"

# Gewichte
w_input = 0.6
w_hidden = 0.4
w_output = 1.2  # Gewicht für Klassifikationsausgabe

# Anfangszustand
hidden_state = 0.0

# Aktivierungsfunktion
def tanh(x):
    return np.tanh(x)

# Schritt-für-Schritt-Verarbeitung
for i, buchstabe in enumerate(text):
    x = buchstaben[buchstabe]
    hidden_state = tanh(w_input * x + w_hidden * hidden_state)

# Klassifikationsausgabe
raw_output = w_output * hidden_state
kategorie = 0 if raw_output < 0.5 else 1

print(f"Letzter Zustand (Gedächtnis): {hidden_state}")
print(f"Rohwert für Klassifikation: {raw_output}")
print(f"Vorhergesagte Kategorie: {'Gruß' if kategorie == 0 else 'Gefühl'}")
