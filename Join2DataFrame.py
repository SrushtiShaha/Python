import pandas as pd

# Create first DataFrame
df1 = pd.DataFrame({
    'ID': [1, 2, 3],
    'Name': ['A', 'B', 'C']
})

# Create second DataFrame
df2 = pd.DataFrame({
    'ID': [4, 5],
    'Name': ['D', 'E']
})

# Join along rows
result = pd.concat([df1, df2], ignore_index=True)

print("DataFrame 1:\n", df1)
print("\nDataFrame 2:\n", df2)
print("\nJoined DataFrame:\n", result)
