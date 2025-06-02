#! usr/env/python3
# Vergleich des Varianz-Einflusses in der linearen Regression mit verschiedenen Modellen
# mit zufälligen Daten, insgesamt 10 Modelle
# Erstellt am 25/01/25

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.linear_model import Ridge, Lasso
from sklearn.svm import SVR
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error

# Seed für reproduzierbare Ergebnisse
np.random.seed(42)

# Erstelle zufällige Daten
def generate_data(size=100):
    X = np.random.uniform(0, 10, size).reshape(-1, 1)
    y = 2 * X.flatten() + 1 + np.random.normal(0, 1, size)
    return X, y

# Testdaten fixieren
X_test_fixed = np.linspace(0, 10, 100).reshape(-1, 1)

models = {
    "LinearRegression": LinearRegression(),
    "Random Forest": RandomForestRegressor(n_estimators=10, random_state=42), "k-NN (k=5)": KNeighborsRegressor(n_neighbors=5),
    "Ridge": Ridge(alpha=1.0),
    "Lasso": Lasso(alpha=1.0),
    "SVR": SVR(kernel="linear"),
    "Decision Tree": DecisionTreeRegressor(random_state=42),
    "Gradient Boosting": GradientBoostingRegressor(random_state=42),
}

# Mehrfaches Trainieren und Vorhersagen sammeln
predictions = {model_name: [] for model_name in models.keys()}
mse_scores = {model_name: [] for model_name in models.keys()}

for _ in range(10):
    X, y = generate_data()
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    for model_name, model in models.items():
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        predictions[model_name].append(y_pred)
        mse = mean_squared_error(y_test, y_pred)
        mse_scores[model_name].append(mse)

# Durchschnittliche Vorhersagen und MSE berechnen
for name, scores in mse_scores.items():
    print(f"Durchschnittlicher MSE für {name}: {np.mean(scores):.2f}")

# Plotten der verschiedenen Modelle
plt.figure(figsize=(10, 6))
for model_name, preds in predictions.items():
    mean_pred = np.mean(preds, axis=0)
    var_pred = np.var(preds, axis=0)

    plt.plot(X_test, mean_pred, label=f"{model_name} (MSE: {np.mean(mse_scores[model_name]):.2f})")

# Ursprüngliche Daten plotten
plt.scatter(X, y, color="gray", alpha=0.5, label="Daten")
plt.title("Varianz in verschiedenen Regressionsmodellen")
plt.xlabel("Eingabe (X)")
plt.ylabel("Ausgabe (y)")
plt.legend()
plt.show()