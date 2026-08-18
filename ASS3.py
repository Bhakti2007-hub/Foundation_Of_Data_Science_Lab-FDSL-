import pandas as pd
import numpy as np
from scipy import stats


# 1. Load Dataset
df = pd.read_csv("C:/Users/BHAKTI/OneDrive/Desktop/SCOE/MLL/Loan_data.csv")

print("First 5 Rows:")
print(df.head())

print("\nDataset Description:")
print(df.describe())


# 2. Mean, Median and Mode using Pandas
mean_val = df["int.rate"].mean()
median_val = df["int.rate"].median()
mode_val = df["int.rate"].mode()[0]

print("\n--- Central Tendency using Pandas ---")
print("Mean:", mean_val)
print("Median:", median_val)
print("Mode:", mode_val)


# 3. Mean, Median and Mode using NumPy / SciPy
rate_array = df["int.rate"].to_numpy()

print("\n--- Central Tendency using NumPy / SciPy ---")
print("NumPy Mean:", np.mean(rate_array))
print("NumPy Median:", np.median(rate_array))
print("SciPy Mode:", stats.mode(rate_array, keepdims=True))


# 4. Central Tendency grouped by Purpose
group_summary = df.groupby("purpose")["int.rate"].agg(
    ["mean", "median", lambda x: x.mode()[0]]
)

group_summary.columns = ["Mean", "Median", "Mode"]

print("\n--- Central Tendency by Purpose ---")
print(group_summary)


# 5. Skewness
skewness = df["int.rate"].skew()

print("\n--- Distribution Analysis ---")
print("Skewness:", skewness)

if mean_val > median_val:
    print("Distribution is right (positively) skewed.")

elif mean_val < median_val:
    print("Distribution is left (negatively) skewed.")

else:
    print("Distribution is approximately symmetric.")