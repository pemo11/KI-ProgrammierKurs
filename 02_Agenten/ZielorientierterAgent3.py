# file: ZielorientierterAgent3.py
# erstellt: 20/01/20

import matplotlib.pyplot as plt
import time

class Agent:
    
    def __init__(self, start_position, ziel_position, hindernisse, spielfeld_size):
        self.position = start_position  # Aktuelle Position des Agenten
        self.ziel = ziel_position       # Zielposition des Agenten
        self.hindernisse = hindernisse  # Liste von Hindernispositionen
        self.spielfeld_size = spielfeld_size  # Größe des Spielfelds
        self.schritte = 0               # Zählt die Schritte des Agenten
        self.route = [start_position]   # Speichert die Route des Agenten

    def ist_hindernis(self, position):
        """Prüft, ob eine Position ein Hindernis ist."""
        return position in self.hindernisse

    def bewege(self):
        """Bewegt den Agenten einen Schritt in Richtung des Ziels."""
        x, y = self.position
        ziel_x, ziel_y = self.ziel

        # Versuch: Bewegung in Richtung des Ziels
        neuer_x, neuer_y = x, y
        if x < ziel_x:
            neuer_x = x + 1
        elif x > ziel_x:
            neuer_x = x - 1

        if y < ziel_y:
            neuer_y = y + 1
        elif y > ziel_y:
            neuer_y = y - 1

        # Prüfen, ob die neue Position ein Hindernis ist
        if not self.ist_hindernis((neuer_x, neuer_y)):
            self.position = (neuer_x, neuer_y)
        else:
            # Ausweichbewegung: Bewege zuerst entlang der x-Achse, dann y-Achse
            if x != ziel_x and not self.ist_hindernis((x + 1, y)):
                self.position = (x + 1, y)
            elif y != ziel_y and not self.ist_hindernis((x, y + 1)):
                self.position = (x, y + 1)

        self.schritte += 1
        self.route.append(self.position)

    def hat_ziel_erreicht(self):
        """Prüft, ob das Ziel erreicht wurde."""
        return self.position == self.ziel

    def zeichne_spielfeld(self):
        """Visualisiert das Spielfeld mit dem Agenten, Ziel und Hindernissen."""
        plt.figure(figsize=(8, 8))
        plt.grid(True)
        plt.xticks(range(self.spielfeld_size[0] + 1))
        plt.yticks(range(self.spielfeld_size[1] + 1))
        plt.xlim(-0.5, self.spielfeld_size[0] - 0.5)
        plt.ylim(-0.5, self.spielfeld_size[1] - 0.5)

        # Hindernisse zeichnen
        for (hx, hy) in self.hindernisse:
            plt.scatter(hx, hy, color="red", s=200, label="Hindernis" if (hx, hy) == self.hindernisse[0] else "")

        # Ziel zeichnen
        plt.scatter(*self.ziel, color="green", s=200, label="Ziel")

        # Route des Agenten zeichnen
        for pos in self.route:
            plt.scatter(*pos, color="blue", s=100, label="Agent (Route)" if pos == self.route[0] else "")
        
        # Aktuelle Position des Agenten hervorheben
        plt.scatter(*self.position, color="yellow", s=300, edgecolors="black", label="Agent (Aktuell)")

        # Legende anzeigen
        plt.legend(loc="upper left")
        plt.show()


# Start- und Zielposition sowie Hindernisse definieren
start = (0, 0)
ziel = (5, 7)
hindernisse = [(2, 2), (3, 2), (4, 2), (4, 3)]
spielfeld_size = (10, 10)

# Agenten erstellen
agent = Agent(start, ziel, hindernisse, spielfeld_size)

# Agenten bewegen, bis das Ziel erreicht ist
while not agent.hat_ziel_erreicht():
    agent.bewege()
    agent.zeichne_spielfeld()
    time.sleep(0.5)

print(f"Der Agent hat das Ziel in {agent.schritte} Schritten erreicht!")
