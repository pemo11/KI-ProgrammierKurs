#! usr/bin/env python3
# file: QLearning_Lab2.py

# Extended Q-Learning example
import numpy as np
import random

states = ["A", "B", "C", "D", "E", "F"]
actions = ["left", "right"]
rewards = {
    ("A", "right"): 0,
    ("B", "right"): 1,
    ("C", "right"): 2,
    ("D", "right"): 3,
    ("E", "right"): 5,
    ("F", "right"): 10,
    ("A", "left"): -5,
    ("B", "left"): -5,
    ("C", "left"): -5,
    ("D", "left"): -5,
    ("E", "left"): -5,
    ("F", "left"): -5,
}

def next_state(current_state, action):
    if action == "right":
        return chr(min(ord(current_state) + 1, ord("F")))
    elif action == "left":
        return chr(max(ord(current_state) - 1, ord("A")))
    return current_state

def get_reward(state, action):
    return rewards.get((state, action), -1)

# Initialize Q-table
q_table = {state: {action: 0 for action in actions} for state in states}
alpha = 0.1  # Learning rate
gamma = 0.9  # Discount factor
epsilon = 0.1  # Exploration rate

def choose_action(state):
    if random.uniform(0, 1) < epsilon:
        return random.choice(actions)  # Explore
    return max(q_table[state], key=q_table[state].get)  # Exploit

# Training
for episode in range(2000):
    state = random.choice(states)  # Start at a random state
    while state != "F":  # Goal state
        action = choose_action(state)
        next_s = next_state(state, action)
        reward = get_reward(state, action)
        q_table[state][action] += alpha * (
            reward + gamma * max(q_table[next_s].values()) - q_table[state][action]
        )
        state = next_s

# Display trained Q-table
print("Q-Table after training:")
for state in q_table:
    print(f"{state}: {q_table[state]}")

# Test the policy
state = "A"
print("\nOptimal Path from 'A':")
while state != "F":
    action = max(q_table[state], key=q_table[state].get)
    print(f"State: {state}, Action: {action}")
    state = next_state(state, action)
