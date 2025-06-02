import os
import numpy as np
import cv2
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# 1️⃣ Bildverzeichnis definieren (Hier sollten deine Pflanzenbilder liegen)
dataset_path = "C:\\Users\\pemo24\\Pictures\\Pflanzen"

# 2️⃣ Labels und Bilder einlesen
X = []  # Feature-Liste
y = []  # Klassen

label_dict = {"Loewenzahn": 0, "Gaensebluemchen": 1, "Klee": 2, "Diverse":3}  # Beispielhafte Labels

for label in label_dict:
    folder_path = os.path.join(dataset_path, label)
    print(f"*** Lese Bilder aus {folder_path}...")    
    for filename in os.listdir(folder_path):
        img_path = os.path.join(folder_path, filename)
        print(f"   >>> Verarbeite {img_path}...")    
        img = cv2.imread(img_path)  # Bild einlesen
        img = cv2.resize(img, (64, 64))  # Größe anpassen (damit alle gleich sind)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # In Graustufen umwandeln
        
        # Histogramm als Feature extrahieren (einfache Methode)
        hist = cv2.calcHist([img], [0], None, [256], [0, 256]).flatten()
        
        X.append(hist)
        y.append(label_dict[label])

# In NumPy-Arrays umwandeln
X = np.array(X)
y = np.array(y)

# 3️⃣ Trainings- und Testdaten aufteilen
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4️⃣ KNN-Modell mit k=3 erstellen
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)

# 5️⃣ Vorhersagen machen
y_pred = knn.predict(X_test)

# 6️⃣ Genauigkeit berechnen
accuracy = accuracy_score(y_test, y_pred)
print(f"Genauigkeit des Pflanzen-KNN-Modells: {accuracy:.2f}")
