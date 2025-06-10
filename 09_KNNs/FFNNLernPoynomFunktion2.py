# Verbesserte Version des Codes, die eine Funktion approximiert
# ReLU-Aktivierungsfunktion und den gesamten Trainingsbereich verwendet
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam

# Ziel-Funktion definieren
def y_func(x):
    return 0.5 * (x + 0.8) * (x + 1.8) * (x - 0.2) * (x - 0.3) * (x - 1.9) + 1

# Daten erzeugen
x = np.linspace(-2, 2, 200).reshape(-1, 1)
y = y_func(x)

# GANZE Daten zum Training verwenden
x_train, y_train = x, y

# Modell definieren mit ReLU
model = Sequential([
    Dense(64, activation='relu', input_shape=(1,)),
    Dense(64, activation='relu'),
    Dense(1)
])

model.compile(optimizer=Adam(0.01), loss='mse')
model.fit(x_train, y_train, epochs=500, verbose=0)

# Vorhersagen
y_pred = model.predict(x)

# Plot
plt.figure(figsize=(10, 6))
plt.plot(x, y, label='Ziel-Funktion', color='black')
plt.plot(x, y_pred, label='Vorhersage', color='blue')
plt.legend()
plt.title('Approximation der Funktion y(x) mit ReLU und vollständigem Trainingsbereich')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.show()
