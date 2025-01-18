#! usr/bin/env python3
# file: QLearning_Labi1.py

import numpy as np
import random

# Define the environment
states = ["A", "B", "C", "D"]  # Example states
actions = ["left", "right"]    # Example actions
rewards = {
    ("A", "right"): 0,
    ("B", "right"): 1,
    ("C", "right"): 2,
    ("D", "right"): 10,
}

# Initialize Q-table
q_table = {state: {action: 0 for action in actions} for state in states}

alpha = 0.1  # Learning rate
gamma = 0.9  # Discount factor
epsilon = 0.1  # Exploration rate

# Define a function to choose an action (epsilon-greedy strategy)
def choose_action(state):
    if random.uniform(0, 1) < epsilon:
        return random.choice(actions)  # Explore
    return max(q_table[state], key=q_table[state].get)  # Exploit

# Simulate the environment
for episode in range(1000):
    state = random.choice(states)  # Start at a random state
    while state != "D":  # Goal state
        action = choose_action(state)
        next_state = "D" if state == "C" else chr(ord(state) + 1)  # Simplified environment
        reward = rewards.get((state, action), -1)  # Get reward
        q_table[state][action] += alpha * (
            reward + gamma * max(q_table[next_state].values()) - q_table[state][action]
        )
        state = next_state

# Display the Q-table
print("Q-Table after training:")
for state in q_table:
    print(f"{state}: {q_table[state]}")
