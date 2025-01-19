#! usr/bin/env python3
# file: DecisionTree_StudentData.py
# Beispiel für einen DecisionTreeClassifier mit Studentendaten

import pandas as pd
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Sample student performance data
data = {
    "Hours_Studied": [4, 6, 2, 7, 8, 3, 5, 10, 1, 9],
    "Class_Attendance": [40, 90, 70, 50, 80, 45, 65, 95, 30, 85],
    "Exam_Preparation": [0, 1, 0, 0, 1, 0, 1, 1, 0, 1],  # 0: No, 1: Yes
    "Performance": [0, 1, 0, 0, 1, 0, 1, 1, 0, 1],  # 0: Fail, 1: Pass
}

# Create a DataFrame
df = pd.DataFrame(data)

# Features and target
X = df[["Hours_Studied", "Class_Attendance", "Exam_Preparation"]]
y = df["Performance"]

#  Apply emphasis to Class_Attendance by scaling it
attendance_weight = 10  # Strengthen the weight of class attendance
df["Class_Attendance"] = df["Class_Attendance"] * attendance_weight

# Split data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Create and train the decision tree model
model = DecisionTreeClassifier(max_depth=3, random_state=42)
model.fit(X_train, y_train)

# Test the model
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2f}")

# Display the decision tree structure
tree_rules = export_text(model, feature_names=list(X.columns))
print("\nDecision Tree Rules:\n")
print(tree_rules)

# Predict the performance of a student with feature names

# New student data
new_students = pd.DataFrame({
    "Hours_Studied": [3, 6, 1, 9],
    "Class_Attendance": [60, 85, 40, 95],
    "Exam_Preparation": [0, 1, 0, 1],
})

# Predict performance for new students
predictions = model.predict(new_students)

# Display the predictions
print("\nPredicted Performance:")
for i, prediction in enumerate(predictions):
    print(f"Student {i + 1}: {'Pass' if prediction == 1 else 'Fail'}")
