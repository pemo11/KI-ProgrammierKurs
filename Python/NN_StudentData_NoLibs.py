import numpy as np

# Sigmoid-Aktivierungsfunktion und ihre Ableitung
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return sigmoid(x) * (1 - sigmoid(x))

# Normalisierungsfunktion (Min-Max-Skalierung)
def normalize(X):
    X_min = X.min(axis=0)
    X_max = X.max(axis=0)
    return (X - X_min) / (X_max - X_min), X_min, X_max

# Simulierter Datensatz
# Features: [Lernaufwand, Besuch der Vorlesung, Lernen per Karteikarten (True/False)]
np.random.seed(42)
X = np.random.rand(500, 2) * 10  # Lernaufwand und Besuch der Vorlesung (Werte von 0 bis 10)
karteikarten = np.random.choice([0, 1], size=(500, 1))  # True/False-Wert
X = np.hstack((X, karteikarten))  # Kombiniere die Features
y = (X[:, 0] * 0.5 + X[:, 1] * 0.3 + X[:, 2] * 2 > 10).astype(int).reshape(-1, 1)  # Dummy-Logik

# Datenaufteilung in Trainings- und Testdaten
split_ratio = 0.8
split_index = int(len(X) * split_ratio)
X_train, X_test = X[:split_index], X[split_index:]
y_train, y_test = y[:split_index], y[split_index:]

# Normalisierung (nur auf numerische Features anwenden)
X_train[:, :2], X_min, X_max = normalize(X_train[:, :2])
X_test[:, :2] = (X_test[:, :2] - X_min) / (X_max - X_min)

# Neuronales Netzwerk-Parameter
input_neurons = 3    # 3 Eingabefeatures (inkl. True/False-Wert)
hidden_neurons = 4   # Anzahl der Neuronen in der versteckten Schicht
output_neurons = 1   # Anzahl der Ausgabeneuronen
learning_rate = 0.01
epochs = 1000

# Gewichtsmatrizen initialisieren
np.random.seed(42)
weights_input_hidden = np.random.randn(input_neurons, hidden_neurons) * 0.01
weights_hidden_output = np.random.randn(hidden_neurons, output_neurons) * 0.01

bias_hidden = np.zeros((1, hidden_neurons))
bias_output = np.zeros((1, output_neurons))

# Training des Netzwerks
for epoch in range(epochs):
    # Vorwärtspropagation
    hidden_input = np.dot(X_train, weights_input_hidden) + bias_hidden
    hidden_output = sigmoid(hidden_input)
    
    final_input = np.dot(hidden_output, weights_hidden_output) + bias_output
    final_output = sigmoid(final_input)
    
    # Fehler berechnen
    error = y_train - final_output
    
    # Rückwärtspropagation
    d_output = error * sigmoid_derivative(final_output)
    d_hidden = np.dot(d_output, weights_hidden_output.T) * sigmoid_derivative(hidden_output)
    
    # Gewichts- und Bias-Updates
    weights_hidden_output += np.dot(hidden_output.T, d_output) * learning_rate
    weights_input_hidden += np.dot(X_train.T, d_hidden) * learning_rate
    bias_output += np.sum(d_output, axis=0, keepdims=True) * learning_rate
    bias_hidden += np.sum(d_hidden, axis=0, keepdims=True) * learning_rate
    
    # Fortschritt ausgeben
    if epoch % 100 == 0:
        loss = np.mean(error**2)
        print(f"Epoch {epoch}/{epochs} - Loss: {loss:.4f}")

# Testdaten evaluieren
hidden_input = np.dot(X_test, weights_input_hidden) + bias_hidden
hidden_output = sigmoid(hidden_input)
final_input = np.dot(hidden_output, weights_hidden_output) + bias_output
final_output = sigmoid(final_input)

predictions = (final_output > 0.5).astype(int)
accuracy = np.mean(predictions == y_test)
print(f"Test Accuracy: {accuracy:.4f}")

# Beispielvorhersage
new_student = np.array([[7, 5, 1]])  # 7 Stunden Lernaufwand, 5 Vorlesungsbesuche, Karteikarten=True
new_student[:, :2] = (new_student[:, :2] - X_min) / (X_max - X_min)  # Normalisieren

hidden_input = np.dot(new_student, weights_input_hidden) + bias_hidden
hidden_output = sigmoid(hidden_input)
final_input = np.dot(hidden_output, weights_hidden_output) + bias_output
final_output = sigmoid(final_input)

print(f"Besteht der Student die Prüfung? {'Ja' if final_output[0][0] > 0.5 else 'Nein'} "
      f"(Wahrscheinlichkeit: {final_output[0][0]:.2f})")
