#! env/usr/bin/python3
# file: GradientBerechnen.py

import numpy as np

# Definiere die Funktion f(x, y) = x^2 + 3y^2
def f(x, y):
    return x**2 + 3*y**2

# Berechne den Gradienten numerisch mit einer kleinen Änderung h
def numerical_gradient(f, x, y, h=1e-5):
    df_dx = (f(x + h, y) - f(x - h, y)) / (2 * h)  # Zentrale Differenzenmethode für x
    df_dy = (f(x, y + h) - f(x, y - h)) / (2 * h)  # Zentrale Differenzenmethode für y
    return np.array([df_dx, df_dy])

# Beispielberechnung für (x, y) = (1, 1) -> (1,1) ist der zufällig gewählte Punkt
grad = numerical_gradient(f, 1, 1)
print(grad)  # Ausgabe: [2. 6.]

grad = numerical_gradient(f, 2, 2)
print(grad)  # Ausgabe: [4. 12.]
