# file: ZielorientierterAgent1.py
# Erstellt: 20/01/25
# Sehr einfacher Agent nach dem Try-and-Error-Prinzip
class Agent:
    def __init__(self, start_position, ziel_position):
        self.position = start_position  # Aktuelle Position des Agenten
        self.ziel = ziel_position       # Zielposition des Agenten
        self.stepCount = 0              # Anzahl der Schritte
    
    def bewege(self):
        """Bewegt den Agenten einen Schritt in Richtung des Ziels."""
        x, y = self.position
        ziel_x, ziel_y = self.ziel

        if x < ziel_x:
            x += 1
            self.stepCount += 1
        elif x > ziel_x:
            x -= 1
            self.stepCount += 1
        
        if y < ziel_y:
            y += 1
            self.stepCount += 1
        elif y > ziel_y:
            y -= 1
            self.stepCount += 1
        
        self.position = (x, y)
        print(f"Agent bewegt sich zu: {self.position}")

    """Gibt die Anzahl der Schritte zurück, die der Agent benötigt hat."""
    def get_StepCount(self):
        # Berechnen der Manhattandistanz
        x1, y1 = self.position
        x2, y2 = self.ziel
        return abs(x2 - x1) + abs(y2 - y1)

    def hat_ziel_erreicht(self):
        """Prüft, ob das Ziel erreicht wurde."""
        return self.position == self.ziel


# Start- und Zielposition definieren
start = (0, 0)
ziel = (5, 7)

# Agenten erstellen
agent = Agent(start, ziel)
stepCount = agent.get_StepCount()

# Agenten bewegen, bis das Ziel erreicht ist
while not agent.hat_ziel_erreicht():
    agent.bewege()

# stepCount = agent.stepCount

print(f"Der Agent hat das Ziel nach {stepCount} Schritten erreicht!")
