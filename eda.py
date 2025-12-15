import pandas as pd

# Load dataset
df = pd.read_csv("quotes_dataset.csv")

# View first few rows
print("First 5 rows:")
print(df.head())

# Dataset structure
print("\nDataset Info:")
print(df.info())

# Statistical summary
print("\nSummary:")
print(df.describe())

# Missing values
print("\nMissing values:")
print(df.isnull().sum())

# Duplicate rows
print("\nDuplicate rows:", df.duplicated().sum())

import matplotlib.pyplot as plt

# Quote length
df["quote_length"] = df["Quote"].apply(len)

# Top authors
top_authors = df["Author"].value_counts().head(10)
print("\nTop Authors:")
print(top_authors)

# Plot
top_authors.plot(kind="bar")
plt.title("Top 10 Authors by Number of Quotes")
plt.xlabel("Author")
plt.ylabel("Count")
plt.show()

# Average quote length per author
avg_length = df.groupby("Author")["quote_length"].mean()

print("\nAverage quote length per author:")
print(avg_length.sort_values(ascending=False).head())

# Very short quotes
print("\nVery short quotes:")
print(df[df["quote_length"] < 15])

# Remove duplicates
df_cleaned = df.drop_duplicates()
print("Rows after removing duplicates:", len(df_cleaned))