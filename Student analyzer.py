import pandas as pd
import numpy as np

# Step 1: Load Dataset
data = pd.read_csv(r"C:\Users\Himan\OneDrive\Documents\Mini projects\student_marks.csv")
print("Dataset:\n", data)

# Step 2: Average marks of each student
data['Average'] = data[['Math','Science','English','History','Computer']].mean(axis=1)
print("\nAverage Marks:\n", data[['Name','Average']])

# Step 3: Find topper
topper = data.loc[data['Average'].idxmax()]
print("\nTopper:", topper['Name'], "with Average =", topper['Average'])

# Step 4: Subject-wise highest scorer
for subject in ['Math','Science','English','History','Computer']:
    top_student = data.loc[data[subject].idxmax()]
    print(f"Highest in {subject}: {top_student['Name']} ({top_student[subject]})")

# Step 5: Class average in each subject
print("\nClass Average per Subject:\n", data[['Math','Science','English','History','Computer']].mean())
