#! usr/bin/env python3
# file: DecisionTree_StudentData.py
# Beispiel für einen DecisionTreeClassifier mit Studentendaten ohne Scikit-learn

# Sample student performance data
data = [
    {"Hours_Studied": 4, "Class_Attendance": 40, "Exam_Preparation": False, "Performance": "Fail"},
    {"Hours_Studied": 6, "Class_Attendance": 90, "Exam_Preparation": True, "Performance": "Pass"},
    {"Hours_Studied": 2, "Class_Attendance": 70, "Exam_Preparation": False, "Performance": "Fail"},
    {"Hours_Studied": 7, "Class_Attendance": 50, "Exam_Preparation": False, "Performance": "Fail"},
    {"Hours_Studied": 8, "Class_Attendance": 80, "Exam_Preparation": True, "Performance": "Pass"},
]

# Decision tree function
def predict_performance(hours_studied, class_attendance, exam_preparation):
    if hours_studied < 5:
        if class_attendance < 50:
            return "Fail"
        else:
            return "Pass"
    else:
        if exam_preparation:
            return "Pass"
        else:
            return "Fail"

# Testing the decision tree
test_data = [
    {"Hours_Studied": 3, "Class_Attendance": 60, "Exam_Preparation": False},
    {"Hours_Studied": 6, "Class_Attendance": 85, "Exam_Preparation": True},
    {"Hours_Studied": 1, "Class_Attendance": 40, "Exam_Preparation": False},
    {"Hours_Studied": 9, "Class_Attendance": 95, "Exam_Preparation": True},
]

# Apply the tree on test data
for i, student in enumerate(test_data):
    prediction = predict_performance(
        student["Hours_Studied"],
        student["Class_Attendance"],
        student["Exam_Preparation"],
    )

    print(f"Student {i + 1}: Predicted Performance = {prediction}")
