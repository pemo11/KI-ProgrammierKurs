#! usr/bin/env python3
# file: StudentData_GiniGain.py

def gini_index(data):
    """
    Calculate the Gini Index for a dataset.
    Each row in `data` is a list where the last element is the class label.
    """
    total_samples = len(data)
    if total_samples == 0:
        return 0  # Edge case: no data
    
    # Count occurrences of each class
    label_counts = {}
    for row in data:
        label = row[-1]  # Assume the last column is the class label
        label_counts[label] = label_counts.get(label, 0) + 1

    # Calculate Gini Index
    gini = 1.0
    for label, count in label_counts.items():
        prob = count / total_samples
        gini -= prob ** 2

    return gini

def split_data(data, feature_index, threshold):
    """
    Split the dataset into two groups based on the given feature and threshold.
    """
    left = [row for row in data if row[feature_index] <= threshold]
    right = [row for row in data if row[feature_index] > threshold]
    return left, right

def measure_gini_gain(data, feature_index, threshold):
    """
    Measure the Gini Gain for splitting the data on a specific feature and threshold.
    """
    # Calculate parent Gini
    parent_gini = gini_index(data)

    # Split data
    left, right = split_data(data, feature_index, threshold)

    # Calculate weighted Gini for the split
    total_samples = len(data)
    left_weight = len(left) / total_samples
    right_weight = len(right) / total_samples
    split_gini = left_weight * gini_index(left) + right_weight * gini_index(right)

    # Gini Gain
    gini_gain = parent_gini - split_gini
    return gini_gain

# Example Dataset: [Hours_Studied, Class_Attendance, Exam_Preparation, Performance]
data = [
    [4, 40, 0, "Fail"],
    [6, 90, 1, "Pass"],
    [2, 70, 0, "Fail"],
    [7, 50, 0, "Fail"],
    [8, 80, 1, "Pass"],
]

# Test the influence of Class Attendance (index 1)
threshold = 50  # Example threshold for splitting
feature_index = 1  # Class Attendance

gini_gain = measure_gini_gain(data, feature_index, threshold)
print(f"Gini Gain for Class Attendance with threshold {threshold}: {gini_gain:.4f}")

def find_best_split(data):
    """
    Find the best feature and threshold for splitting the dataset
    based on the Gini Gain.
    """
    best_feature = None
    best_threshold = None
    best_gain = 0

    # Iterate through all features (except the last column, which is the label)
    for feature_index in range(len(data[0]) - 1):
        # Get all unique thresholds (feature values) for this feature
        thresholds = set(row[feature_index] for row in data)

        # Calculate Gini Gain for each threshold
        for threshold in thresholds:
            gini_gain = measure_gini_gain(data, feature_index, threshold)
            if gini_gain > best_gain:
                best_gain = gini_gain
                best_feature = feature_index
                best_threshold = threshold

    return best_feature, best_threshold, best_gain

# Example Dataset: [Hours_Studied, Class_Attendance, Exam_Preparation, Performance]
data = [
    [4, 40, 0, "Fail"],
    [6, 90, 1, "Pass"],
    [2, 70, 0, "Fail"],
    [7, 50, 0, "Fail"],
    [8, 80, 1, "Pass"],
]

# Find the best feature and threshold for splitting
best_feature, best_threshold, best_gain = find_best_split(data)

# Map feature index to feature name
feature_names = ["Hours_Studied", "Class_Attendance", "Exam_Preparation"]

# Output results
print(f"Best Feature: {feature_names[best_feature]}")
print(f"Best Threshold: {best_threshold}")
print(f"Gini Gain: {best_gain:.4f}")
