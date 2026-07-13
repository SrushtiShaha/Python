import numpy as np
import pandas as pd

# Create a NumPy array
arr = np.array([10, 20, 30, 40, 50])

# Convert NumPy array to Pandas Series
series = pd.Series(arr)

print("NumPy Array:", arr)
print("\nPandas Series:\n", series)
