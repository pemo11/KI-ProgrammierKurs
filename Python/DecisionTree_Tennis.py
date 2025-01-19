#! usr/bin/env python3
# file: DecisionTree_Tennis.py
import pandas as pd
import numpy as np

# Creating the dataset from the image table
data = {
    "Outlook": ["Sunny", "Sunny", "Overcast", "Rain", "Rain", "Rain", "Overcast", "Sunny", "Sunny", "Rain", "Sunny", "Overcast", "Overcast", "Rain"],
    "Temperature": ["Hot", "Hot", "Hot", "Mild", "Cool", "Cool", "Cool", "Mild", "Cool", "Mild", "Mild", "Mild", "Hot", "Mild"],
    "Humidity": ["High", "High", "High", "High", "Normal", "Normal", "Normal", "High", "Normal", "Normal", "Normal", "High", "Normal", "High"],
    "Wind": ["Weak", "Strong", "Weak", "Weak", "Weak", "Strong", "Strong", "Weak", "Weak", "Weak", "Strong", "Strong", "Weak", "Strong"],
    "PlayTennis": ["No", "No", "Yes", "Yes", "Yes", "No", "Yes", "No", "Yes", "Yes", "Yes", "Yes", "Yes", "No"]
}

df = pd.DataFrame(data)

# Entropy calculation function
def entropy(target_col):
    elements, counts = np.unique(target_col, return_counts=True)
    probabilities = counts / len(target_col)
    return -np.sum(probabilities * np.log2(probabilities))

# Information gain calculation function
def info_gain(data, split_attribute_name, target_name="PlayTennis"):
    total_entropy = entropy(data[target_name])
    vals, counts = np.unique(data[split_attribute_name], return_counts=True)
    weighted_entropy = np.sum([
        (counts[i] / np.sum(counts)) * entropy(data.where(data[split_attribute_name] == vals[i]).dropna()[target_name])
        for i in range(len(vals))
    ])
    return total_entropy - weighted_entropy

# Determining the best attribute to split
def find_best_split(data, attributes, target_name="PlayTennis"):
    info_gains = {attribute: info_gain(data, attribute, target_name) for attribute in attributes}
    return max(info_gains, key=info_gains.get), info_gains

# Recursive function to build the tree
def build_tree(data, attributes, target_name="PlayTennis", tree=None):
    target_values = np.unique(data[target_name])
    
    # If the dataset is pure or empty, return the single class or None
    if len(target_values) == 1:
        return target_values[0]
    elif len(data) == 0:
        return None

    # If there are no attributes left to split, return the most common value
    elif len(attributes) == 0:
        return data[target_name].mode()[0]

    # Find the best attribute to split
    best_attribute, _ = find_best_split(data, attributes, target_name)
    tree = {best_attribute: {}}
    attributes = [attr for attr in attributes if attr != best_attribute]

    # Split the dataset and build subtrees
    for value in np.unique(data[best_attribute]):
        subset = data.where(data[best_attribute] == value).dropna()
        subtree = build_tree(subset, attributes, target_name)
        tree[best_attribute][value] = subtree

    return tree

# Building the decision tree
attributes = ["Outlook", "Temperature", "Humidity", "Wind"]
decision_tree = build_tree(df, attributes)

print(decision_tree)
