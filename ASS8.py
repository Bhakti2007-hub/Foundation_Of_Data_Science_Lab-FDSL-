
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load dataset
df = pd.read_csv("archive (1)/netflix_titles.csv")

print("Dataset Shape:", df.shape)
print("\nFirst 5 Records:")
print(df.head())

print("\nDataset Information:")
df.info()

# 2. Check missing values
print("\nMissing Values Before Cleaning:")
print(df.isnull().sum())

# Handle missing categorical values
df["director"] = df["director"].fillna("Unknown")
df["cast"] = df["cast"].fillna("Unknown")
df["country"] = df["country"].fillna("Unknown")
df["rating"] = df["rating"].fillna("Not Rated")

# Remove records without date_added
df.dropna(subset=["date_added"], inplace=True)

# Convert date_added to datetime
df["date_added"] = pd.to_datetime(
    df["date_added"].str.strip(),
    format="mixed",
    errors="coerce"
)
df.dropna(subset=["date_added"], inplace=True)

print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

# 3. Extract duration as a number
df["duration_int"] = pd.to_numeric(
    df["duration"].str.extract(r"(\d+)")[0],
    errors="coerce"
)

# Analyze movies and TV shows separately
movies = df[
    (df["type"] == "Movie") & df["duration_int"].notna()
].copy()

tv_shows = df[
    (df["type"] == "TV Show") & df["duration_int"].notna()
].copy()

# IQR outlier detection for movie duration
Q1 = movies["duration_int"].quantile(0.25)
Q3 = movies["duration_int"].quantile(0.75)
IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

movies_clean = movies[
    movies["duration_int"].between(lower, upper)
].copy()

print("\nMovies before outlier handling:", len(movies))
print("Movies after outlier handling:", len(movies_clean))
print("TV shows retained:", len(tv_shows))

# 4. Descriptive statistics
print("\nDescriptive Statistics:")
print(df.describe(include="all"))

print("\nContent Type Counts:")
print(df["type"].value_counts())

print("\nRating Counts:")
print(df["rating"].value_counts())

print("\nMovie Duration Statistics:")
print(movies_clean["duration_int"].describe())

print("\nTV Show Seasons Statistics:")
print(tv_shows["duration_int"].describe())

# 5. Visualizations

# Histogram of movie durations
plt.figure(figsize=(8, 5))
sns.histplot(
    data=movies_clean,
    x="duration_int",
    bins=20,
    kde=True
)
plt.title("Distribution of Movie Duration (Minutes)")
plt.xlabel("Duration in Minutes")
plt.tight_layout()
plt.show()

# Boxplot of movie durations
plt.figure(figsize=(7, 5))
sns.boxplot(y=movies_clean["duration_int"])
plt.title("Boxplot of Movie Duration")
plt.ylabel("Duration in Minutes")
plt.tight_layout()
plt.show()

# Top 10 countries by title count
# A title can list multiple countries.
top_countries = (
    df.assign(country=df["country"].str.split(", "))
      .explode("country")
)

top_countries = top_countries[
    top_countries["country"] != "Unknown"
]

plt.figure(figsize=(10, 5))
top_countries["country"].value_counts().head(10).plot(
    kind="bar"
)
plt.title("Top 10 Countries by Number of Titles")
plt.xlabel("Country")
plt.ylabel("Number of Titles")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()

# Content type comparison
plt.figure(figsize=(6, 4))
sns.countplot(data=df, x="type")
plt.title("Movies vs TV Shows")
plt.xlabel("Content Type")
plt.ylabel("Number of Titles")
plt.tight_layout()
plt.show()

# 6. Derive insights
print("\nKEY INSIGHTS")

print("Most common rating:", df["rating"].mode()[0])
print(
    "Most frequently listed country:",
    top_countries["country"].value_counts().idxmax()
)
print("Most common content type:", df["type"].mode()[0])

print(
    "Most common release year:",
    df["release_year"].mode()[0]
)

print("\nEDA completed successfully.")
