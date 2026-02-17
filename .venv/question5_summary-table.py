import pandas as pd
import numpy as np

# load dataset
df = pd.read_csv("student.csv")

# create grade_band column
def assign_band(grade):
    if grade <= 9:
        return "Low"
    elif 10 <= grade <= 14:
        return "Medium"
    else:
        return "High"

df["grade_band"] = df["grade"].apply(assign_band)

# grouped summary table
summary = df.groupby("grade_band").agg(
    number_of_students=("grade", "count"),
    average_absences=("absences", "mean"),
    percent_internet=("internet", lambda x: x.mean() * 100)
)

# save table
summary.to_csv("student_bands.csv")

# print summary
print(summary)
