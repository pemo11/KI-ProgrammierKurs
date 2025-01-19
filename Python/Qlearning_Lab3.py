#! usr/bin/env python3
# file: Qlearning_Lab3.py

import numpy as np
import random

# Define the 2D grid (labyrinth)
grid = [
    [0, 0, 0, 1],  # 0: Free cell, 1: Goal
    [1, 1, 0, 1],  # 1: Wall
    [0, 0, 0, 0],
]

rows, cols = len(grid), len(grid[0])

# Define possible actions
actions = ["up", "down", "left", "right"]

# Rewards
goal_reward = 10
penalty = -1
wall_penalty = -5

# Q-table
q_table = np.zeros((rows, cols, len(actions)))

# Parameters
alpha = 0.1  # Learning rate
gamma = 0.9  # Discount factor
epsilon = 0.1  # Exploration rate
episodes = 1000

# Helper functions
def is_valid_move(x, y):
    return 0 <= x < rows and 0 <= y < cols and grid[x][y] != 1

def next_state(x, y, action):
    if action == "up":
        return (x - 1, y) if is_valid_move(x - 1, y) else (x, y)
    elif action == "down":
        return (x + 1, y) if is_valid_move(x + 1, y) else (x, y)
    elif action == "left":
        return (x, y - 1) if is_valid_move(x, y - 1) else (x, y)
    elif action == "right":
        return (x, y + 1) if is_valid_move(x, y + 1) else (x, y)
    return (x, y)

def get_reward(x, y):
    if grid[x][y] == 1:  # Goal state
        return goal_reward
    elif not is_valid_move(x, y):  # Wall
        return wall_penalty
    return penalty

def choose_action(x, y):
    if random.uniform(0, 1) < epsilon:
        return random.choice(range(len(actions)))  # Explore
    return np.argmax(q_table[x, y])  # Exploit

def print_labyrinth(grid, path=[]):
    """Print the labyrinth with the agent's path."""
    print("\nLabyrinth:")
    for i, row in enumerate(grid):
        row_str = ""
        for j, cell in enumerate(row):
            if (i, j) in path:  # Path taken by the agent
                row_str += "A "  # Agent
            elif cell == 1:
                row_str += "W "  # Wall
            elif cell == 0:
                row_str += ". "  # Free cell
            elif cell == 1:
                row_str += "G "  # Goal
        print(row_str)
    print()

# Training the agent
for episode in range(episodes):
    x, y = random.randint(0, rows - 1), random.randint(0, cols - 1)  # Start at a random position
    while grid[x][y] != 1:  # Until the agent reaches the goal
        action = choose_action(x, y)
        next_x, next_y = next_state(x, y, actions[action])
        reward = get_reward(next_x, next_y)

        # Q-Learning update
        best_next_action = np.max(q_table[next_x, next_y])
        q_table[x, y, action] += alpha * (
            reward + gamma * best_next_action - q_table[x, y, action]
        )

        x, y = next_x, next_y

# Test the agent
def find_path(start_x, start_y):
    path = []
    x, y = start_x, start_y
    while grid[x][y] != 1:  # Until the goal is reached
        path.append((x, y))
        action = np.argmax(q_table[x, y])
        x, y = next_state(x, y, actions[action])
    path.append((x, y))  # Append goal
    return path

# Display the optimal path
start_x, start_y = 2, 0  # Starting position
path = find_path(start_x, start_y)
print_labyrinth(grid, path)
print("Optimal path:", path)
print("Total reward:", sum(get_reward(x, y) for x, y in path))
