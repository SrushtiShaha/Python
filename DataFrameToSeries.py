import pandas as pd

# DataFrame
data = {
    'Name': ['A', 'B', 'C', 'D'],
    'Age': [21, 25, 30, 28]
}

df = pd.DataFrame(data)

# Convert the first column to a Series
first_column_series = df.iloc[:, 0]

print("Original DataFrame:\n", df)
print("\nFirst Column as Series:\n", first_column_series)
