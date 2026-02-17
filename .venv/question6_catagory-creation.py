import pandas as pd

# load dataset
df = pd.read_csv("crime.csv")

# create risk category
df["risk"] = df["ViolentCrimesPerPop"].apply(
    lambda x: "HighCrime" if x >= 0.50 else "LowCrime"
)

# group by risk and calculate average unemployment
grouped = df.groupby("risk")["PctUnemployed"].mean()

# print results clearly
for group, avg_unemp in grouped.items():
    print(f"{group} Average Unemployment Rate: {avg_unemp:.4f}")
