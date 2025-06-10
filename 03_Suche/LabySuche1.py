# Korrektes Labyrinth als 2D-Array (basierend auf dem ursprünglichen Bitmap)
# 1 = Wand (schwarz), 0 = Weg (weiß)
# Eingang: rechts unten (14,13), Ausgang: links oben (1,0)

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

# Koordinaten für Start und Ziel
start = (14, 13)  # Eingang rechts unten
goal = (1, 0)     # Ausgang links oben

# Funktion zum Anzeigen des Labyrinths
def print_maze(maze_array, path=None):
    """
    Zeigt das Labyrinth an
    maze_array: 2D-Array mit 1 für Wände, 0 für Wege
    path: Optional - Liste von (row, col) Koordinaten für den Lösungsweg
    """
    for i, row in enumerate(maze_array):
        line = ""
        for j, cell in enumerate(row):
            if path and (i, j) in path:
                line += "."  # Pfad markieren
            elif cell == 1:
                line += "█"  # Wand
            else:
                line += " "  # Weg
        print(line)

# Einfacher A*-Pathfinding Algorithmus
def find_path(maze_array, start, goal):
    """
    Findet den kürzesten Weg durch das Labyrinth
    """
    from collections import deque
    
    rows, cols = len(maze_array), len(maze_array[0])
    queue = deque([(start, [start])])
    visited = {start}
    
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # rechts, unten, links, oben
    
    while queue:
        (row, col), path = queue.popleft()
        
        if (row, col) == goal:
            return path
        
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            
            if (0 <= new_row < rows and 0 <= new_col < cols and 
                maze_array[new_row][new_col] == 0 and 
                (new_row, new_col) not in visited):
                
                visited.add((new_row, new_col))
                queue.append(((new_row, new_col), path + [(new_row, new_col)]))
    
    return None  # Kein Weg gefunden

# Beispiel-Nutzung:
if __name__ == "__main__":
    print("Labyrinth:")
    print_maze(maze)
    
    print(f"\nStart: {start}")
    print(f"Ziel: {goal}")
    
    # Weg finden
    path = find_path(maze, start, goal)
    if path:
        print(f"\nLösungsweg gefunden! Länge: {len(path)} Schritte")
        print("\nLabyrinth mit Lösungsweg (. = Pfad):")
        print_maze(maze, path)
    else:
        print("\nKein Weg gefunden!")