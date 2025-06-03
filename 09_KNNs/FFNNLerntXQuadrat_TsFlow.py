# #! usr/bin/python3
# -*- coding: utf-8 -*-
# Einfache Feedforward Neural Network lernt die Funktion f(x) = x^2 mit TensorFlow/Keras
# file: FFNNLerntXQuadrat_TsFlow.py

import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import Callback

# Eigener Callback zur Ausgabe des Losses pro Epoche
class LossLogger(Callback):
    def on_epoch_end(self, epoch, logs=None):
        print(f"Epoche {epoch+1}: Loss = {logs['loss']:.6f}, Val_Loss = {logs['val_loss']:.6f}")

# Daten erzeugen (ohne Rauschen)
x = np.linspace(-2, 2, 100).reshape(-1, 1)
y = x ** 2

x_train, y_train = x[:50], y[:50]
x_test, y_test = x[50:], y[50:]

# Modell definieren
model = Sequential([
    Dense(32, activation='tanh', input_shape=(1,)),
    Dense(32, activation='tanh'),
    Dense(1)
])

model.compile(optimizer=Adam(0.01), loss='mse')

# Training
anzahl_epochen = 300

history = model.fit(x_train,
                    y_train, 
                    validation_data=(x_test, y_test),
                    epochs=anzahl_epochen,
                    verbose=0,
                    callbacks=[LossLogger()]
                    )

# Ergebnis plotten
plt.figure(figsize=(10, 6))
plt.plot(history.history['loss'], label='Train Loss')
plt.plot(history.history['val_loss'], label='Test Loss')
plt.title('Loss-Verlauf beim Lernen von f(x) = x^2')
plt.xlabel('Epoche')
plt.ylabel('MSE Loss')
plt.grid(True)
plt.legend()

# Vorhersagen
y_train_pred = model.predict(x_train)
y_test_pred = model.predict(x_test)

# Ergebnisplot: Funktionen
plt.subplot(1, 2, 2)
plt.plot(x, y, label='Wahre Funktion f(x)=x²', color='black')
plt.scatter(x_train, y_train_pred, label='Train-Vorhersage', color='blue', s=20)
plt.scatter(x_test, y_test_pred, label='Test-Vorhersage', color='red', s=20)
plt.title('Modellvorhersage vs. echte Funktion')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()


