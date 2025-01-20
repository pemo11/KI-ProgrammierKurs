# file: ZielorientierterAgent2.py
# Erstellt: 20/01/25
# Dieses Mal mit Hindernissen, die zufällig gesetzt werden

class Agent:
    def __init__(self, start_position, ziel_position, hindernisse):
        self.position = start_position  # Aktuelle Position des Agenten
        self.ziel = ziel_position       # Zielposition des Agenten
        self.hindernisse = hindernisse  # Liste von Hindernispositionen
        self.schritte = 0               # Zählt die Schritte des Agenten

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
            # Ausweichbewegung (einfach: wechselt die Richtung)
            if x != ziel_x and not self.ist_hindernis((x + 1, y)):
                self.position = (x + 1, y)
            elif y != ziel_y and not self.ist_hindernis((x, y + 1)):
                self.position = (x, y + 1)
        self.schritte += 1
        print(f"Agent bewegt sich zu: {self.position}")

    def hat_ziel_erreicht(self):
        """Prüft, ob das Ziel erreicht wurde."""
        return self.position == self.ziel


# Start- und Zielposition sowie Hindernisse definieren
start = (0, 0)
ziel = (5, 7)
hindernisse = [(2, 2), (3, 2), (4, 2), (4, 3)]

# Agenten erstellen
agent = Agent(start, ziel, hindernisse)

# Agenten bewegen, bis das Ziel erreicht ist
while not agent.hat_ziel_erreicht():
    agent.bewege()

print(f"Der Agent hat das Ziel in {agent.schritte} Schritten erreicht!")
