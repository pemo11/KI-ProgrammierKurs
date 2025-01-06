import pandas as pd
import random
from os import path

# Generate 100 rows of training data
data = []
for _ in range(100):
    study_hours = round(random.uniform(1, 10), 1)  # Random study hours between 1 and 10
    sleep_hours = round(random.uniform(1, 8), 1)   # Random sleep hours between 1 and 8
    # Pass: 1 if study hours + sleep hours > 10, otherwise 0
    pass_status = 1 if (study_hours + sleep_hours > 10) else 0
    data.append({"StudyHours": study_hours, "SleepHours": sleep_hours, "Pass": pass_status})

# Convert to DataFrame
df = pd.DataFrame(data)

# Save to CSV
file_path = path.join(path.dirname(__file__), 'student_data2.csv')
df.to_csv(file_path, index=False)

file_path
