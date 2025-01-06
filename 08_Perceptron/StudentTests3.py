#! usr/bin/env python3
# Vorhersage, ob ein Student besteht oder nicht, basierend auf den Studien- und Schlafstunden
# Ohne Bibliotheken wie Numpy oder Scikit-Learn
# Mit der Darstellung der errors in einem Diagramm

import csv
from os import path
import random

class Perceptron:

    def __init__(self, learning_rate=0.1, epochs=10):
        self.learning_rate = learning_rate
        self.epochs = epochs
        self.weights = []
        self.bias = 0
        self.error_history = []  # To track errors over epochs

    def fit(self, X, y):
        n_features = len(X[0])              # Number of features
        self.weights = [0] * n_features     # Initialize weights

        # Over multiple epochs, it adjusts weights and biases to reduce the error for misclassified points.
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
            self.error_history.append(total_error)
            # the goal of the perceptron is to reach a point where the error is zero
            if total_error == 0:  # Stop early if no error
                break
        return self.error_history
        
    # Predicts the output based on the input data and the trained weights and bias
    # returns a list of predicted outputs
    def predict(self, X):
        predictions = []
        for x in X:
            # Linear combination of weights and input data
            linear_output = sum(xi * wi for xi, wi in zip(x, self.weights)) + self.bias
            # Step activation function
            y_predicted = 1 if linear_output > 0 else 0
            # Append the predicted output to the list
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

# Split data into training and test sets
def train_test_split(X, y, test_size=0.2):
    data = list(zip(X, y))
    random.shuffle(data)
    split_index = int(len(data) * (1 - test_size))
    train_data = data[:split_index]
    test_data = data[split_index:]
    X_train, y_train = zip(*train_data)
    X_test, y_test = zip(*test_data)
    return list(X_train), list(y_train), list(X_test), list(y_test)


# Evaluate the accuracy of the predictions
def evaluate_model(y_true, y_pred):
    """
    Manually evaluates the performance of the perceptron.
    :param y_true: List of true labels.
    :param y_pred: List of predicted labels.
    """
    # Initialize metrics
    tp = 0  # True Positives
    tn = 0  # True Negatives
    fp = 0  # False Positives
    fn = 0  # False Negatives

    # Compute confusion matrix elements
    for true, pred in zip(y_true, y_pred):
        if true == 1 and pred == 1:
            tp += 1
        elif true == 0 and pred == 0:
            tn += 1
        elif true == 0 and pred == 1:
            fp += 1
        elif true == 1 and pred == 0:
            fn += 1

    # Calculate metrics
    accuracy = (tp + tn) / len(y_true)
    precision = tp / (tp + fp) if (tp + fp) > 0 else 0
    recall = tp / (tp + fn) if (tp + fn) > 0 else 0
    f1_score = 2 * (precision * recall) / (precision + recall) if (precision + recall) > 0 else 0

    # Print metrics
    print(f"Accuracy: {accuracy:.2f}")
    print(f"Precision: {precision:.2f}")
    print(f"Recall: {recall:.2f}")
    print(f"F1 Score: {f1_score:.2f}")
    print("Confusion Matrix:")
    print(f"TP: {tp}, TN: {tn}, FP: {fp}, FN: {fn}")

def plot_data(X, y):
    for i in range(len(y)):
        color = 'blue' if y[i] == 1 else 'red'
        plt.scatter(X[i][0], X[i][1], color=color)
    plt.xlabel('Study Hours')
    plt.ylabel('Sleep Hours')
    plt.title('Data Visualization')
    plt.show()

# Main program
if __name__ == "__main__":
    # File path to the student data
    file_path = path.join(path.dirname(__file__), 'student_data2.csv')

    # Load training data from CSV
    X, y = load_data(file_path)

    print(f"Loaded {len(X)} data points.")
    

    # Split into training and testing sets
    X_train, y_train, X_test, y_test = train_test_split(X, y, test_size=0.2)

    import matplotlib.pyplot as plt
    plot_data(X_train, y_train)

    # Create and train the perceptron
    perceptron = Perceptron(learning_rate=0.1, epochs=40)

    error_history = perceptron.fit(X_train, y_train)
    plt.plot(range(len(error_history)), error_history)
    plt.xlabel("Epochs")
    plt.ylabel("Total Error")
    plt.title("Error Reduction Over Epochs")
    plt.show()

    # Make predictions on the test set
    y_pred = perceptron.predict(X_test)

    # Evaluate the model
    evaluate_model(y_test, y_pred)

