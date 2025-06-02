# env/usr/bin/python3
# file: GradientBerechen_SteigungsVektor.py

from matplotlib import pyplot as plt
import numpy as np

# Berechne den Gradienten numerisch mit einer kleinen Änderung h
def numerical_gradient(f, x, y, h=1e-5):
    df_dx = (f(x + h, y) - f(x - h, y)) / (2 * h)  # Zentrale Differenzenmethode für x
    df_dy = (f(x, y + h) - f(x, y - h)) / (2 * h)  # Zentrale Differenzenmethode für y
    return np.array([df_dx, df_dy])


def f(x, y):
    return x**2 + 3*y**2

# Punkt (1,1) und sein Gradient
x0, y0 = 1, 1
grad = numerical_gradient(f, x0, y0)

# Berechnung des Einheitsvektors
grad_magnitude = np.linalg.norm(grad)  # Länge des Gradientenvektors
unit_grad = grad / grad_magnitude  # Einheitsvektor

# Plot
plt.figure(figsize=(7, 7))
plt.quiver(x0, y0, grad[0], grad[1], color="red", angles="xy", scale_units="xy", scale=1, label="Gradient")
plt.quiver(x0, y0, unit_grad[0], unit_grad[1], color="green", angles="xy", scale_units="xy", scale=1, label="Einheitsvektor")

plt.xlim(0, 2)
plt.ylim(0, 2)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Gradient und Richtung des steilsten Anstiegs bei (1,1)")
plt.legend()
plt.grid()
plt.show()
