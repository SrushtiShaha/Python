import numpy as np
import pandas as pd

print("1. Convert NumPy array to Pandas Series")
# 1. NumPy array → Pandas Series
arr = np.array([10, 20, 30, 40, 50])
series_from_array = pd.Series(arr)
print(series_from_array)


print("\n 2. Convert first column of DataFrame to Series")
# 2. First column → Series
df1 = pd.DataFrame({
    'A': [1, 2, 3, 4],
    'B': ['x', 'y', 'z', 'w']
})
first_col_series = df1.iloc[:, 0]   # extract first column
print(first_col_series)


print("\n 3. Join two DataFrames along rows")
# 3. Join two DataFrames (row-wise)
df2 = pd.DataFrame({
    'A': [5, 6],
    'B': ['p', 'q']
})
joined_df = pd.concat([df1, df2], ignore_index=True)
print(joined_df)


print("\n 4. Split the DataFrame")
# 4. Split DataFrame into two parts
split1 = joined_df.iloc[:3]   # first 3 rows
split2 = joined_df.iloc[3:]   # remaining rows

print("\n Part 1")
print(split1)

print("\n Part 2")
print(split2)
