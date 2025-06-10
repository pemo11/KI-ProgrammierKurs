# SCHRITT-FÜR-SCHRITT ERKLÄRUNG: LABYRINTH-LÖSUNG
# ================================================

# 1. DATENSTRUKTUR: Das Labyrinth als 2D-Array
# ---------------------------------------------
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

# Erklärung: 
# - 1 = Wand (nicht begehbar)
# - 0 = Weg (begehbar)
# - Position (zeile, spalte): maze[zeile][spalte]

start = (14, 13)  # Start: Zeile 14, Spalte 13
goal = (1, 0)     # Ziel: Zeile 1, Spalte 0

print("=== LABYRINTH SETUP ===")
print(f"Start: {start}")
print(f"Ziel: {goal}")
print(f"Labyrinth-Größe: {len(maze)} x {len(maze[0])}")

# 2. EINFACHER ALGORITHMUS: BREADTH-FIRST SEARCH (BFS)
# ====================================================
def bfs_pathfinding(maze, start, goal):
    """
    BFS sucht den KÜRZESTEN Weg (garantiert!), ist aber nicht so effizient wie A*
    
    Wie BFS funktioniert:
    1. Beginne am Startpunkt
    2. Schaue alle Nachbarn an
    3. Dann alle Nachbarn der Nachbarn
    4. Immer weiter, bis Ziel gefunden
    """
    print("\n=== BFS ALGORITHMUS ===")
    
    from collections import deque
    
    # Queue: Speichert Positionen zum Besuchen
    # Jedes Element: ((zeile, spalte), [pfad_bis_hierher])
    queue = deque([(start, [start])])
    
    # Visited: Welche Positionen wurden bereits besucht?
    visited = {start}
    
    # Bewegungsrichtungen: rechts, unten, links, oben
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    step = 0
    while queue:
        step += 1
        # Nimm erste Position aus der Queue
        (row, col), path = queue.popleft()
        
        print(f"Schritt {step}: Prüfe Position ({row}, {col})")
        
        # Ziel erreicht?
        if (row, col) == goal:
            print(f"🎉 ZIEL ERREICHT nach {step} Schritten!")
            return path
        
        # Schaue alle 4 Nachbarn an
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            
            # Ist die neue Position gültig?
            if (0 <= new_row < len(maze) and 
                0 <= new_col < len(maze[0]) and 
                maze[new_row][new_col] == 0 and  # Ist es ein Weg?
                (new_row, new_col) not in visited):  # Noch nicht besucht?
                
                # Markiere als besucht
                visited.add((new_row, new_col))
                # Füge zur Queue hinzu mit erweitertem Pfad
                queue.append(((new_row, new_col), path + [(new_row, new_col)]))
                print(f"  → Füge Nachbar ({new_row}, {new_col}) zur Queue hinzu")
    
    return None  # Kein Weg gefunden

# 3. INTELLIGENTER ALGORITHMUS: A* (A-STERN)
# ==========================================
def manhattan_distance(pos1, pos2):
    """
    Manhattan-Distanz: |x1-x2| + |y1-y2|
    Das ist unsere "Heuristik" - eine Schätzung, wie weit das Ziel noch ist
    """
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

def a_star_pathfinding(maze, start, goal):
    """
    A* ist INTELLIGENTER als BFS:
    - BFS schaut "blind" in alle Richtungen
    - A* bevorzugt Richtungen, die zum Ziel führen
    
    A* verwendet drei Werte:
    - g(n): Echte Kosten vom Start bis zur Position n
    - h(n): Geschätzte Kosten von Position n zum Ziel (Heuristik)
    - f(n) = g(n) + h(n): Gesamtschätzung
    """
    print("\n=== A* ALGORITHMUS ===")
    
    import heapq
    
    # Priority Queue: Sortiert automatisch nach f-Wert (niedrigste zuerst)
    # Jedes Element: (f_wert, g_wert, (zeile, spalte), [pfad])
    open_list = [(0, 0, start, [start])]
    
    # Welche Positionen wurden bereits final bearbeitet?
    closed_set = set()
    
    # Beste bekannte g-Werte für jede Position
    g_scores = {start: 0}
    
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    step = 0
    while open_list:
        step += 1
        
        # Nimm Position mit niedrigstem f-Wert
        f_current, g_current, current, path = heapq.heappop(open_list)
        
        print(f"Schritt {step}: Prüfe {current}")
        print(f"  g={g_current}, h={manhattan_distance(current, goal)}, f={f_current}")
        
        # Schon bearbeitet? Überspringe
        if current in closed_set:
            continue
            
        # Als bearbeitet markieren
        closed_set.add(current)
        
        # Ziel erreicht?
        if current == goal:
            print(f"🎉 ZIEL ERREICHT nach {step} Schritten!")
            return path
        
        # Schaue alle Nachbarn an
        row, col = current
        for dr, dc in directions:
            neighbor = (row + dr, col + dc)
            new_row, new_col = neighbor
            
            # Ist Nachbar gültig und noch nicht final bearbeitet?
            if (0 <= new_row < len(maze) and 
                0 <= new_col < len(maze[0]) and 
                maze[new_row][new_col] == 0 and 
                neighbor not in closed_set):
                
                # Berechne neue Kosten
                tentative_g = g_current + 1  # 1 Schritt weiter
                
                # Ist das ein besserer Weg zu diesem Nachbarn?
                if neighbor not in g_scores or tentative_g < g_scores[neighbor]:
                    g_scores[neighbor] = tentative_g
                    h_score = manhattan_distance(neighbor, goal)
                    f_score = tentative_g + h_score
                    
                    new_path = path + [neighbor]
                    heapq.heappush(open_list, (f_score, tentative_g, neighbor, new_path))
                    
                    print(f"  → Nachbar {neighbor}: g={tentative_g}, h={h_score}, f={f_score}")
    
    return None

# 4. VISUALISIERUNG DES PFADS
# ============================
def print_maze_with_path(maze, path=None):
    """Zeigt das Labyrinth mit optionalem Pfad an"""
    print("\n=== LABYRINTH MIT LÖSUNG ===")
    
    for i, row in enumerate(maze):
        line = ""
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
        print(line)

# 5. VERGLEICH DER ALGORITHMEN
# =============================
if __name__ == "__main__":
    print("LABYRINTH-LÖSUNG: BFS vs A*")
    print("=" * 40)
    
    # BFS testen
    print("\n🔍 TESTE BFS...")
    bfs_path = bfs_pathfinding(maze, start, goal)
    if bfs_path:
        print(f"BFS fand Pfad mit {len(bfs_path)} Schritten")
        print_maze_with_path(maze, bfs_path)
    
    # A* testen
    print("\n🧠 TESTE A*...")
    astar_path = a_star_pathfinding(maze, start, goal)
    if astar_path:
        print(f"A* fand Pfad mit {len(astar_path)} Schritten")
        print_maze_with_path(maze, astar_path)
    
    # Vergleich
    print("\n📊 VERGLEICH:")
    print(f"BFS Pfad-Länge: {len(bfs_path) if bfs_path else 'Nicht gefunden'}")
    print(f"A* Pfad-Länge: {len(astar_path) if astar_path else 'Nicht gefunden'}")
    print("\nBeide finden den optimalen Pfad, aber A* ist meist schneller!")
    
    print("\n🎓 WAS HABEN WIR GELERNT?")
    print("• BFS garantiert den kürzesten Pfad, aber kann langsam sein")
    print("• A* ist intelligenter und meist schneller")
    print("• A* braucht eine gute Heuristik (hier: Manhattan-Distanz)")
    print("• Priority Queue sorgt dafür, dass A* zuerst vielversprechende Wege verfolgt")
    print("• g(n) = echte Kosten, h(n) = geschätzte Kosten, f(n) = g+h")

# 6. DETAILLIERTE A* ERKLÄRUNG
# =============================
print("\n" + "="*60)
print("🔬 DETAILLIERTE A* ERKLÄRUNG")
print("="*60)

print("""
A* KERNKONZEPTE:

1. OPEN LIST (Priority Queue):
   - Enthält alle Knoten, die noch untersucht werden müssen
   - Sortiert nach f(n) = g(n) + h(n)
   - Niedrigste f-Werte werden zuerst bearbeitet

2. CLOSED SET:
   - Enthält alle bereits final bearbeiteten Knoten
   - Verhindert unnötige Wiederholung

3. G-SCORE:
   - Echte Kosten vom Start bis zum aktuellen Knoten
   - In unserem Fall: Anzahl der Schritte

4. H-SCORE (Heuristik):
   - Geschätzte Kosten vom aktuellen Knoten zum Ziel
   - Manhattan-Distanz: |x1-x2| + |y1-y2|
   - Muss "zulässig" sein (nie überschätzen!)

5. F-SCORE:
   - f(n) = g(n) + h(n)
   - Gesamtschätzung der Kosten für den besten Weg durch n

WARUM IST A* BESSER ALS BFS?
- BFS: Schaut blind in alle Richtungen → O(b^d)
- A*: Bevorzugt vielversprechende Richtungen → oft viel schneller
- A* ist "optimal" wenn Heuristik zulässig ist
""")

# 7. SCHRITT-FÜR-SCHRITT BEISPIEL
# ================================
def a_star_detailed_example():
    """Zeigt die ersten paar Schritte von A* im Detail"""
    print("\n🔍 A* BEISPIEL - ERSTE 3 SCHRITTE:")
    print("-" * 50)
    
    # Simuliere die ersten Schritte manuell
    current = start  # (14, 13)
    
    print(f"START bei {current}")
    print(f"ZIEL bei {goal}")
    print()
    
    # Schritt 1: Von Start aus
    neighbors = [(13, 13)]  # Nur ein Nachbar verfügbar (nach oben)
    for neighbor in neighbors:
        g = 1  # 1 Schritt vom Start
        h = manhattan_distance(neighbor, goal)
        f = g + h
        print(f"Nachbar {neighbor}:")
        print(f"  g = {g} (Schritte vom Start)")
        print(f"  h = {h} (Manhattan-Distanz zum Ziel)")
        print(f"  f = {f} (Gesamtschätzung)")
        print()
    
    print("➡️ A* wählt immer den Knoten mit niedrigstem f-Wert!")
    print("➡️ Bei Gleichstand: Knoten mit niedrigstem h-Wert")
    print("➡️ Das führt A* 'intelligenter' zum Ziel als BFS")

# Führe detailliertes Beispiel aus
a_star_detailed_example()

# 8. KOMPLEXITÄTSVERGLEICH
# ========================
print("\n📈 KOMPLEXITÄTSVERGLEICH:")
print("-" * 30)
print("BFS:")
print("  Zeit: O(b^d) - exponentiell mit Verzweigungsfaktor b und Tiefe d")
print("  Speicher: O(b^d) - muss alle Knoten einer Ebene speichern")
print("  Garantie: Findet immer kürzesten Pfad")
print()
print("A*:")
print("  Zeit: O(b^d) im schlechtesten Fall, oft viel besser")
print("  Speicher: O(b^d) - kann mehr speichern als BFS")
print("  Garantie: Findet kürzesten Pfad (wenn Heuristik zulässig)")
print("  Vorteil: Intelligente Suche durch Heuristik")
print()
print("💡 WANN WELCHEN ALGORITHMUS VERWENDEN?")
print("  BFS: Einfach, garantiert optimal, gut für kleine Probleme")
print("  A*: Besser für große Probleme, braucht gute Heuristik")
print("  Dijkstra: Wenn alle Kanten unterschiedliche Kosten haben")
print("  DFS: Wenn nur irgendein Weg gefunden werden soll (nicht optimal)")

print("\n🎯 ZUSAMMENFASSUNG:")
print("Beide Algorithmen finden den optimalen Weg, aber A* ist")
print("meist effizienter, weil es 'weiß', in welche Richtung")
print("das Ziel liegt und diese Richtung bevorzugt!")