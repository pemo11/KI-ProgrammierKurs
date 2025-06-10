#! usr/bin/env python3
# file: LabiPemo1.py
# Mein eigenes Labyrinth-Puzzle mit A*-Algorithmus

# Ein 10x10 Labyrinth - erstmal alles leer
maze = []
for i in range(10):
    row = []
    for j in range(10):
        # 0 = Weg, 1 = Wand
        row.append(0)  
    maze.append(row)

# Testen: Erstes Element ausgeben
# Sollte 0 ausgeben
print(maze[0][0])  
print(f"Labyrinth-Größe: {len(maze)} x {len(maze[0])}")

def print_maze(maze):
    for row in maze:
        line = ""
        for cell in row:
            if cell == 0:
                line += ". "  # Weg
            else:
                line += "# "  # Wand
        print(line)

# Labyrinth ausgeben
print("Labyrinth:")
print_maze(maze)

# Äußere Wände bauen (Rahmen)
for i in range(10):
    maze[0][i] = 1      # Obere Wand
    maze[9][i] = 1      # Untere Wand
    maze[i][0] = 1      # Linke Wand  
    maze[i][9] = 1      # Rechte Wand

# Schauen wir uns das Ergebnis an
print("Labyrinth mit Rahmen:")
print_maze(maze)

# Eingang links oben schaffen
maze[1][0] = 0  # Loch in der linken Wand

# Ausgang rechts unten schaffen  
maze[8][9] = 0  # Loch in der rechten Wand

print("Labyrinth mit Eingang und Ausgang:")
print_maze(maze)

maze[2][6] = 1
maze[2][7] = 1
maze[4][1] = 1
maze[4][2] = 1
maze[5][5] = 1
maze[5][6] = 1
maze[5][7] = 1

print("Labyrinth mit inneren Wänden:")
print_maze(maze)

# Start- und Zielpunkte festlegen
start = (1, 0)  # Beim Eingang (Zeile 1, Spalte 0)
goal = (8, 9)   # Beim Ausgang (Zeile 8, Spalte 9)

print(f"Start: {start}")
print(f"Ziel: {goal}")

def manhattan_distance(pos1, pos2):
    """Berechnet die Manhattan-Distanz zwischen zwei Punkten"""
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

# Teste die Funktion
distance = manhattan_distance(start, goal)
print(f"Manhattan-Distanz von Start zu Ziel: {distance}")

def get_neighbors(position, maze):
    """Findet alle begehbaren Nachbarn einer Position"""
    row, col = position
    neighbors = []
    
    # Die 4 Richtungen: rechts, runter, links, hoch
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    for dr, dc in directions:
        new_row, new_col = row + dr, col + dc
        
        # Ist der Nachbar im Labyrinth und begehbar?
        if (0 <= new_row < 10 and 0 <= new_col < 10 and 
            maze[new_row][new_col] == 0):
            neighbors.append((new_row, new_col))
    
    return neighbors

# Teste mit dem Startpunkt
start_neighbors = get_neighbors(start, maze)
print(f"Nachbarn vom Start {start}: {start_neighbors}")

import heapq

# A*-Algorithmus Schritt für Schritt (es werden nur die ersten drei Schritte gezeigt)
def a_star_step_by_step(maze, start, goal):
    """Nur die ersten drei Schritte - vereinfacht"""
    
    open_list = []
    closed_set = set()
    
    # Schritt 1: Start bearbeiten
    print("=== SCHRITT 1 ===")
    heapq.heappush(open_list, (16, 0, (1, 0)))
    f, g, current = heapq.heappop(open_list)
    closed_set.add(current)
    print(f"Bearbeite: {current}")
    
    # Nachbar (1,1) hinzufügen
    heapq.heappush(open_list, (16, 1, (1, 1)))
    print(f"Open list: {len(open_list)} Elemente")
    
    # Schritt 2: (1,1) bearbeiten  
    print("\n=== SCHRITT 2 ===")
    f, g, current = heapq.heappop(open_list)
    closed_set.add(current)
    print(f"Bearbeite: {current}")
    
    # Nachbarn von (1,1) hinzufügen
    heapq.heappush(open_list, (15, 2, (1, 2)))  # g=2, h=13, f=15
    heapq.heappush(open_list, (16, 2, (2, 1)))  # g=2, h=14, f=16
    
    print(f"Open list: {len(open_list)} Elemente")
    
    # Schritt 3: ???
    print("\n=== SCHRITT 3 ===")
    f, g, current = heapq.heappop(open_list)
    print(f"Bearbeite: {current} mit f={f}, g={g}")
    
    # Position (1,2) komplett bearbeiten
    closed_set.add(current)
    
    # Nachbarn von (1,2) finden
    neighbors = get_neighbors(current, maze)
    print(f"Nachbarn von {current}: {neighbors}")
    
    # Jeden Nachbarn untersuchen - mit Debug
    for neighbor in neighbors:
        print(f"DEBUG: Untersuche {neighbor}")
        if neighbor in closed_set:
            print(f"  {neighbor}: Bereits bearbeitet, überspringe")
        else:
            new_g = g + 1
            h_val = manhattan_distance(neighbor, goal)
            f_val = new_g + h_val
            print(f"  {neighbor}: g={new_g}, h={h_val}, f={f_val} → zur open_list")
            heapq.heappush(open_list, (f_val, new_g, neighbor))

    print(f"\nNach Schritt 3:")
    print(f"Closed set: {closed_set}")
    print(f"Open list: {len(open_list)} Elemente")
    
    return open_list, closed_set

# Teste
open, close = a_star_step_by_step(maze, start, goal)

# Die vollständige A*-Suche in einer Schleife
def a_star(maze, start, goal):
    """Kompletter A*-Algorithmus in einer Schleife"""
    
    # Initialisierung
    open_list = []
    closed_set = set()
    g_scores = {start: 0}
    came_from = {}
    
    # Start zur open_list hinzufügen
    h_start = manhattan_distance(start, goal)
    f_start = 0 + h_start
    heapq.heappush(open_list, (f_start, 0, start))
    
    print(f"A* Suche von {start} nach {goal}")
    print(f"Ziel-Distanz: {h_start}")
    print("-" * 40)
    
    step = 0
    
    # HAUPTSCHLEIFE
    while open_list:
        step += 1
        
        # Besten Knoten aus open_list nehmen
        f_current, g_current, current = heapq.heappop(open_list)
        
        print(f"\nSchritt {step}: Bearbeite {current}")
        print(f"  f={f_current}, g={g_current}")
        
        # Bereits bearbeitet? (kann durch Duplikate passieren)
        if current in closed_set:
            print(f"  → Bereits bearbeitet, überspringe")
            continue
        
        # Als bearbeitet markieren
        closed_set.add(current)
        
        # ZIEL ERREICHT?
        if current == goal:
            print(f"\n🎉 ZIEL ERREICHT nach {step} Schritten!")
            
            # Pfad rekonstruieren
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            
            print(f"Pfad: {' → '.join(map(str, path))}")
            print(f"Pfad-Länge: {len(path)} Schritte")
            return path
        
        # Nachbarn untersuchen
        neighbors = get_neighbors(current, maze)
        print(f"  Nachbarn: {neighbors}")
        
        for neighbor in neighbors:
            # Bereits bearbeitet?
            if neighbor in closed_set:
                print(f"    {neighbor}: Bereits bearbeitet")
                continue
            
            # Neue g-Kosten berechnen
            tentative_g = g_current + 1
            
            # Ist das ein besserer Weg?
            if neighbor not in g_scores or tentative_g < g_scores[neighbor]:
                # Ja! Aktualisiere Werte
                came_from[neighbor] = current
                g_scores[neighbor] = tentative_g
                
                h_score = manhattan_distance(neighbor, goal)
                f_score = tentative_g + h_score
                
                heapq.heappush(open_list, (f_score, tentative_g, neighbor))
                
                print(f"    {neighbor}: g={tentative_g}, h={h_score}, f={f_score}")
            else:
                print(f"    {neighbor}: Schlechterer Weg, ignoriere")
        
        print(f"  Open list: {len(open_list)} Elemente")
        
        # Sicherheitsabbruch nach 50 Schritten
        if step > 50:
            print("Abbruch nach 50 Schritten!")
            break
    
    print("\n❌ Leoder kein Weg gefunden!")
    return None

# VOLLSTÄNDIGE A*-SUCHE STARTEN
print("VOLLSTÄNDIGER A*-ALGORITHMUS")
print("=" * 50)
path = a_star(maze, start, goal)

if path:
    print(f"\n✅ Erfolg! Weg gefunden mit {len(path)} Schritten")
else:
    print(f"\n❌ Kein Weg möglich")

