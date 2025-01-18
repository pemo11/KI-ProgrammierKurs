#! usr/bin/env python3
# file: StudentData_CorrelationCheck.py

# Berechnung der Korrelation zwischen den Merkmalen

import pandas as pd

# Sample Data
data = {
    "Hours_Studied": [4, 6, 2, 7, 8, 3, 5, 10, 1, 9],
    "Class_Attendance": [40, 90, 70, 50, 80, 45, 65, 95, 30, 85],
    "Exam_Preparation": [0, 1, 0, 0, 1, 0, 1, 1, 0, 1],  # 0: No, 1: Yes
    "Performance": [0, 1, 0, 0, 1, 0, 1, 1, 0, 1],  # 0: Fail, 1: Pass
}

df = pd.DataFrame(data)
print(df.corr())
