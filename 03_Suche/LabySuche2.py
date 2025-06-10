# A*-ALGORITHMUS FÜR LABYRINTH-LÖSUNG
# ===================================

import heapq

# Das Labyrinth als 2D-Array
maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],  # Zeile 0
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],  # Zeile 1 - Ausgang bei (1,0)
    [1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1],  # Zeile 2
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1],  # Zeile 3
    [1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1],  # Zeile 4
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],  # Zeile 5
    [1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1],  # Zeile 6
    [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],  # Zeile 7
    [1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1],  # Zeile 8
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1],  # Zeile 9
    [1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1],  # Zeile 10
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],  # Zeile 11
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1],  # Zeile 12
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],  # Zeile 13
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1]   # Zeile 14 - Eingang bei (14,13)
]

# Start- und Zielpunkte
start = (14, 13)  # Eingang rechts unten
goal = (1, 0)     # Ausgang links oben

def manhattan_distance(pos1, pos2):
    """
    Berechnet die Manhattan-Distanz zwischen zwei Punkten.
    Dies ist unsere Heuristik h(n) - eine Schätzung der verbleibenden Kosten.
    
    Manhattan-Distanz = |x1-x2| + |y1-y2|
    """
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

def get_neighbors(position, maze):
    """
    Gibt alle gültigen Nachbarpositionen zurück.
    Gültig = innerhalb der Grenzen und begehbar (Wert 0).
    """
    row, col = position
    neighbors = []
    
    # Vier mögliche Bewegungsrichtungen: rechts, unten, links, oben
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    for dr, dc in directions:
        new_row, new_col = row + dr, col + dc
        
        # Prüfe, ob Position gültig ist
        if (0 <= new_row < len(maze) and 
            0 <= new_col < len(maze[0]) and 
            maze[new_row][new_col] == 0):  # 0 = begehbar
            
            neighbors.append((new_row, new_col))
    
    return neighbors

def reconstruct_path(came_from, current):
    """
    Rekonstruiert den Pfad vom Ziel zurück zum Start.
    came_from ist ein Dictionary: {position: vorherige_position}
    """
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.append(current)
    
    path.reverse()  # Umkehren, damit Pfad von Start zu Ziel geht
    return path

def a_star(maze, start, goal, verbose=False):
    """
    A*-Algorithmus zur Pfadfindung im Labyrinth.
    
    Der Algorithmus arbeitet mit drei wichtigen Werten:
    - g(n): Echte Kosten vom Start bis zur Position n
    - h(n): Geschätzte Kosten von Position n zum Ziel (Heuristik)
    - f(n) = g(n) + h(n): Gesamtschätzung für den besten Weg durch n
    
    Args:
        maze: 2D-Array des Labyrinths
        start: Startposition (row, col)
        goal: Zielposition (row, col)
        verbose: Wenn True, zeigt Schritt-für-Schritt Details
    
    Returns:
        Liste von Positionen, die den optimalen Pfad bilden
    """
    
    # SCHRITT 1: Initialisierung
    # ==========================
    
    # Open List: Priority Queue mit (f_score, g_score, position)
    # Wichtig: heapq sortiert nach dem ersten Element (f_score)
    open_list = [(0, 0, start)]
    
    # Closed Set: Bereits final bearbeitete Positionen
    closed_set = set()
    
    # g_scores: Beste bekannte Kosten vom Start zu jeder Position
    g_scores = {start: 0}
    
    # came_from: Speichert den besten Vorgänger für jede Position
    came_from = {}
    
    if verbose:
        print(f"A*-Suche von {start} nach {goal}")
        print(f"Heuristik (Manhattan-Distanz): {manhattan_distance(start, goal)}")
        print("-" * 50)
    
    step = 0
    
    # SCHRITT 2: Hauptschleife
    # =========================
    while open_list:
        step += 1
        
        # Nimm Position mit niedrigstem f-Score aus der Open List
        f_current, g_current, current = heapq.heappop(open_list)
        
        if verbose:
            h_current = manhattan_distance(current, goal)
            print(f"Schritt {step}: Untersuche {current}")
            print(f"  g={g_current}, h={h_current}, f={f_current}")
        
        # Bereits bearbeitet? Überspringe (kann durch Duplikate passieren)
        if current in closed_set:
            if verbose:
                print(f"  → Bereits bearbeitet, überspringe")
            continue
        
        # Markiere als bearbeitet
        closed_set.add(current)
        
        # SCHRITT 3: Ziel erreicht?
        # ==========================
        if current == goal:
            if verbose:
                print(f"🎉 ZIEL ERREICHT nach {step} Schritten!")
            return reconstruct_path(came_from, current)
        
        # SCHRITT 4: Untersuche alle Nachbarn
        # ====================================
        neighbors = get_neighbors(current, maze)
        
        for neighbor in neighbors:
            # Bereits final bearbeitet? Überspringe
            if neighbor in closed_set:
                continue
            
            # Berechne tentative g-Score (Kosten vom Start zum Nachbarn)
            tentative_g = g_current + 1  # +1 weil jeder Schritt Kosten 1 hat
            
            # Ist das ein besserer Weg zu diesem Nachbarn?
            if neighbor not in g_scores or tentative_g < g_scores[neighbor]:
                # Ja! Aktualisiere Werte
                came_from[neighbor] = current
                g_scores[neighbor] = tentative_g
                
                h_score = manhattan_distance(neighbor, goal)
                f_score = tentative_g + h_score
                
                # Füge zur Open List hinzu
                heapq.heappush(open_list, (f_score, tentative_g, neighbor))
                
                if verbose:
                    print(f"  → Nachbar {neighbor}: g={tentative_g}, h={h_score}, f={f_score}")
    
    # Kein Weg gefunden
    if verbose:
        print("❌ Kein Weg zum Ziel gefunden!")
    return None

def print_maze_with_path(maze, path=None):
    """
    Zeigt das Labyrinth mit dem gefundenen Pfad an.
    """
    print("\nLabyrinth mit A*-Lösung:")
    print("█ = Wand, S = Start, Z = Ziel, . = Pfad, ⎵ = freier Weg")
    print("-" * (len(maze[0]) + 2))
    
    for i, row in enumerate(maze):
        line = "|"
        for j, cell in enumerate(row):
            if path and (i, j) in path:
                if (i, j) == start:
                    line += "S"  # Start
                elif (i, j) == goal:
                    line += "Z"  # Ziel
                else:
                    line += "."  # Pfad
            elif cell == 1:
                line += "█"  # Wand
            else:
                line += " "  # Freier Weg
        line += "|"
        print(line)
    
    print("-" * (len(maze[0]) + 2))

# Hauptprogramm
if __name__ == "__main__":
    print("A*-ALGORITHMUS FÜR LABYRINTH-LÖSUNG")
    print("=" * 40)
    
    # Führe A*-Suche durch
    print("\n🔍 Führe A*-Suche durch...")
    path = a_star(maze, start, goal, verbose=True)
    
    if path:
        print(f"\n✅ Pfad gefunden!")
        print(f"Pfad-Länge: {len(path)} Schritte")
        print(f"Pfad: {' → '.join(map(str, path))}")
        
        # Zeige Labyrinth mit Lösung
        print_maze_with_path(maze, path)
        
        # Statistiken
        print(f"\n📊 STATISTIKEN:")
        print(f"• Start: {start}")
        print(f"• Ziel: {goal}")
        print(f"• Pfad-Länge: {len(path)} Schritte")
        print(f"• Manhattan-Distanz: {manhattan_distance(start, goal)} (Luftlinie)")
        print(f"• A*-Effizienz: {manhattan_distance(start, goal)/len(path)*100:.1f}% der Luftlinie")
        
    else:
        print("\n❌ Kein Pfad gefunden!")

    # Zusätzliche Erklärung
    print(f"\n🧠 WIE FUNKTIONIERT A*?")
    print("1. Beginne am Startpunkt")
    print("2. Wähle immer den Punkt mit niedrigstem f = g + h")
    print("3. g = echte Kosten vom Start")
    print("4. h = geschätzte Kosten zum Ziel (Manhattan-Distanz)")
    print("5. Wiederhole bis Ziel erreicht")
    print("\n💡 A* ist optimal, weil die Manhattan-Distanz nie überschätzt!")