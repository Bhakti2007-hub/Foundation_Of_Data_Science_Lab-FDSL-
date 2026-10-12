
import pandas as pd
from ydata_profiling import ProfileReport

# 1. Load loan applicant dataset
df = pd.read_csv("c:/Users/BHAKTI/OneDrive/Desktop/SCOE/MLL/Loan_data.csv")

# 2. Display basic dataset information
print("Dataset Shape:", df.shape)

print("\nFirst 5 Records:")
print(df.head())

print("\nDataset Information:")
df.info()

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:", df.duplicated().sum())

print("\nDescriptive Statistics:")
print(df.describe(include="all"))

# 3. Generate automated EDA report
profile = ProfileReport(
    df,
    title="Loan Applicant Data - EDA Report",
    explorative=True
)

# 4. Save report as HTML
profile.to_file("eda_report.html")

print("\nEDA report generated successfully!")
print("Open eda_report.html in your web browser.")
