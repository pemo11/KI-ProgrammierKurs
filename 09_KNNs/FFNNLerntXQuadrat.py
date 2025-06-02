#! usr/bin/python3
# -*- coding: utf-8 -*-
# file: FFNNLerntXQuadrat.py

import torch
import torch.nn as nn
import torch.optim as optim
import matplotlib.pyplot as plt

# 1. Daten generieren
x = torch.linspace(-2, 2, 100).view(-1, 1)
y = x ** 2

# 2. Einfaches FFNN definieren
model = nn.Sequential(
    nn.Linear(1, 32),
    nn.ReLU(),
    nn.Linear(32, 1)
)

# 3. Verlustfunktion und Optimierer
criterion = nn.MSELoss()
optimizer = optim.Adam(model.parameters(), lr=0.01)

# 4. Training
num_epochs = 500
for epoch in range(num_epochs):
    # schaltet das Modell in den Trainingsmodus (optional, aber empfohlen)
    model.train()
    optimizer.zero_grad()
    
    # Vorwärtsdurchlauf
    y_pred = model(x)
    
    # Verlust berechnen
    loss = criterion(y_pred, y)
    
    # Rückwärtsdurchlauf und Optimierung
    loss.backward()
    optimizer.step()
    
    if (epoch + 1) % 10 == 0:
        print(f'Epoch [{epoch + 1}/{num_epochs}], Loss: {loss.item():.4f}')

# 5. Ergebnisse visualisieren
plt.plot(x.detach().numpy(), y.detach().numpy(), label='True y = x^2')
plt.plot(x.detach().numpy(), y_pred.detach().numpy(), label='NN Output')
plt.legend()
plt.grid(True)
plt.show()