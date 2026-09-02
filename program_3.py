import pandas as pd

# Read CSV file
df = pd.read_csv("data.csv")

# Display data
print("Data:")
print(df)

# Check rows and columns
print("\nRows and Columns:")
print(df.shape)

# Check data types
print("\nData Types:")
print(df.dtypes)

# Summary of numerical data
print("\nSummary:")
print(df.describe())

# Filter data
filtered = df[df["Marks"] >= 50]

print("\nFiltered Data:")
print(filtered)

# Remove missing values
cleaned = filtered.dropna()

# Save cleaned data
cleaned.to_csv("cleaned_data.csv", index=False)

print("\nCleaned data saved successfully!")
