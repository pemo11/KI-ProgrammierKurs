#! usr/bin/env python3
# Vorhersage, ob ein Student besteht oder nicht, basierend auf den Studien- und Schlafstunden
# Ohne Bibliotheken wie Numpy oder Scikit-Learn
# Die Daten sind in einer CSV-Datei gespeichert

import csv
from os import path

class Perceptron:
    def __init__(self, learning_rate=0.1, epochs=10):
        self.learning_rate = learning_rate
        self.epochs = epochs
        self.weights = []
        self.bias = 0

    def fit(self, X, y):
        n_features = len(X[0])  # Number of features
        self.weights = [0] * n_features  # Initialize weights

        for epoch in range(self.epochs):
            total_error = 0
            for i in range(len(X)):
                # Linear combination
                linear_output = sum(x * w for x, w in zip(X[i], self.weights)) + self.bias
                # Step activation function
                y_predicted = 1 if linear_output > 0 else 0
                # Compute the error
                error = y[i] - y_predicted
                total_error += abs(error)
                # Update weights and bias
                for j in range(n_features):
                    self.weights[j] += self.learning_rate * error * X[i][j]
                self.bias += self.learning_rate * error

            print(f"Epoch {epoch + 1}: Total Error = {total_error}")
            if total_error == 0:  # Stop early if no error
                break

    def predict(self, X):
        predictions = []
        for x in X:
            linear_output = sum(xi * wi for xi, wi in zip(x, self.weights)) + self.bias
            y_predicted = 1 if linear_output > 0 else 0
            predictions.append(y_predicted)
        return predictions


# Read the CSV file
def load_data(file_path):
    X = []
    y = []
    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            X.append([float(row['StudyHours']), float(row['SleepHours'])])
            y.append(int(row['Pass']))
    return X, y


# File path to the student data
file_path = path.join(path.dirname(__file__), 'student_data.csv')

# Load training data from CSV
X_train, y_train = load_data(file_path)

# Create and train the perceptron
perceptron = Perceptron(learning_rate=0.1, epochs=10)
perceptron.fit(X_train, y_train)

# Test data for prediction
X_test = [
    [2.5, 1],  # New student data
    [4, 1.5],
    [6, 3],
    [3, 0.5]
]

# Make predictions
predictions = perceptron.predict(X_test)
for i, prediction in enumerate(predictions):
    print(f"Input: {X_test[i]} => Predicted Output: {'Pass' if prediction == 1 else 'Fail'}")
