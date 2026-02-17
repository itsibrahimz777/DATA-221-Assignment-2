import pandas as pd

# load the dataset
df = pd.read_csv("student.csv")

# filter students
filtered = df[
    (df["studytime"] >= 3) &
    (df["internet"] == 1) &
    (df["absences"] <= 5)
]

# save filtered data
filtered.to_csv("high_engagement.csv", index=False)

# print number of students saved
num_students = len(filtered)

# compute average grade
# (Assuming the grade column is named 'grade')
average_grade = filtered["grade"].mean()

print("Number of students saved:", num_students)
print("Average grade:", average_grade)
