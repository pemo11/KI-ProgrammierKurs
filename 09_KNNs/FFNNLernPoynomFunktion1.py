# Erster Versuch, der nicht gut funktioniert, da die Funktion zu komplex ist.
# FFNNLernPoynomFunktion1.py
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Ziel-Funktion definieren
def y_func(x):
    return 0.5 * (x + 0.8) * (x + 1.8) * (x - 0.2) * (x - 0.3) * (x - 1.9) + 1

# Daten erzeugen
x = np.linspace(-2, 2, 200).reshape(-1, 1)
y = y_func(x)

# Trainings-/Testdaten
x_train, y_train = x[:100], y[:100]
x_test, y_test = x[100:], y[100:]

# Modell definieren
model = Sequential([
    Dense(64, activation='tanh', input_shape=(1,)),
    Dense(64, activation='tanh'),
    Dense(1)
])

model.compile(optimizer='adam', loss='mse')
model.fit(x_train, y_train, epochs=500, verbose=0)

# Vorhersagen
y_pred_train = model.predict(x_train)
y_pred_test = model.predict(x_test)

# Plot
plt.figure(figsize=(10, 6))
plt.plot(x, y, label='Ziel-Funktion', color='black')
plt.scatter(x_train, y_pred_train, label='Train-Prediction', s=10, color='blue')
plt.scatter(x_test, y_pred_test, label='Test-Prediction', s=10, color='red')
plt.legend()
plt.title('Approximierung der Funktion y(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.show()
