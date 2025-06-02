#! usr/bin/python3
# -*- coding: utf-8 -*-
# file: FFNNLerntXQuadratMitRauschen.py
# This code trains a feedforward neural network to learn the function y = x^2 with added noise.

import torch
import torch.nn as nn
import torch.optim as optim
import matplotlib.pyplot as plt

# Daten vorbereiten
def create_data(noise_std=0.0):
    x = torch.linspace(-2, 2, 100).view(-1, 1)
    y_true = x ** 2
    if noise_std > 0:
        y = y_true + torch.normal(0, noise_std, size=x.shape)
    else:
        y = y_true
    return x, y, y_true


# Modell erstellen
def build_model():
    return nn.Sequential(
        nn.Linear(1, 64),
        nn.Tanh(),
        nn.Linear(64, 64),
        nn.Tanh(),
        nn.Linear(64, 1)
    )

# Trainingsfunktion
def train_model(model, x_train, y_train, x_test, y_test, epochs=1000):
    optimizer = optim.Adam(model.parameters(), lr=0.01)
    criterion = nn.MSELoss()
    train_losses = []
    test_losses = []
    for _ in range(epochs):
        model.train()
        optimizer.zero_grad()
        y_pred = model(x_train)
        loss = criterion(y_pred, y_train)
        loss.backward()
        optimizer.step()

        model.eval()
        with torch.no_grad():
            y_test_pred = model(x_test)
            test_loss = criterion(y_test_pred, y_test)
        train_losses.append(loss.item())
        test_losses.append(test_loss.item())
    return train_losses, test_losses, model(x_test).detach()

# Daten: mit und ohne Rauschen
x_all, y_clean, y_true = create_data(noise_std=0.0)
x_all_n, y_noisy, _ = create_data(noise_std=0.1)

# Split
x_train, x_test = x_all[:50], x_all[50:]
y_train_clean, y_test_clean = y_clean[:50], y_clean[50:]
y_train_noisy, y_test_noisy = y_noisy[:50], y_noisy[50:]

# Training ohne Rauschen
model_clean = build_model()
loss_clean_train, loss_clean_test, y_pred_clean = train_model(
    model_clean, x_train, y_train_clean, x_test, y_test_clean
)

# Training mit Rauschen
model_noisy = build_model()
loss_noisy_train, loss_noisy_test, y_pred_noisy = train_model(
    model_noisy, x_train, y_train_noisy, x_test, y_test_noisy
)

import pandas as pd
import matplotlib.pyplot as plt

min_len = min(len(loss_clean_train), len(loss_clean_test),
              len(loss_noisy_train), len(loss_noisy_test))

df = pd.DataFrame({
    'Epoch': list(range(min_len)),
    'Train Loss (Clean)': loss_clean_train[:min_len],
    'Test Loss (Clean)': loss_clean_test[:min_len],
    'Train Loss (Noisy)': loss_noisy_train[:min_len],
    'Test Loss (Noisy)': loss_noisy_test[:min_len],
})


# Als Tabelle anzeigen
print(df.head())

# Oder direkt als Plot
df.plot(x='Epoch', y=['Train Loss', 'Test Loss'])
plt.grid(True)
plt.title("Train/Test Loss-Verlauf")
plt.show()