'''
Einfaches RNN-Beispiel in Python
Erneut eine Wort-Klassizifierung
Dieses Mal aber per TensorFlow
'''

import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, SimpleRNN, Dense
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.preprocessing.sequence import pad_sequences

# 1. Wörter und Kategorien
worte = ["HALLO", "TSCHÜSS", "HEULEN", "LACHEN"]
kategorien = [0, 0, 1, 1]  # 0 = Gruß, 1 = Gefühl

# 2. Buchstaben zu Zahlen
alphabet = sorted(list(set("".join(worte))))
buchstabe2index = {b: i+1 for i, b in enumerate(alphabet)}  # +1 weil 0 Padding ist
vocab_size = len(buchstabe2index) + 1

# 3. Wörter in Sequenzen umwandeln
sequences = [[buchstabe2index[b] for b in wort] for wort in worte]
maxlen = max(len(seq) for seq in sequences)
X = pad_sequences(sequences, maxlen=maxlen, padding='post')
y = to_categorical(kategorien, num_classes=2)

# 4. Modell erstellen
model = Sequential([
    Embedding(input_dim=vocab_size, output_dim=8, input_length=maxlen),
    SimpleRNN(16),
    Dense(2, activation="softmax")  # 2 Klassen
])

model.compile(
    optimizer="adam",
    loss="categorical_crossentropy",
    metrics=["accuracy"]
    )

# 5. Trainieren
model.fit(X, y, epochs=100, verbose=0)

# 6. Testen
testwort = "HEULEN"
testwort = "HALLO"  # Testwort ändern
test_seq = [buchstabe2index.get(b, 0) for b in testwort]
test_seq_padded = pad_sequences([test_seq], maxlen=maxlen, padding='post')
probs = model.predict(test_seq_padded)

# 7. Ausgabe
kategorienamen = ["Gruß", "Gefühl"]
wahrscheinlichkeit = probs[0]
for i, p in enumerate(wahrscheinlichkeit):
    print(f"{kategorienamen[i]:>6}: {p:.4f}")
