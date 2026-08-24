import numpy as np
arr = np.array(['Welcome To Python Programming', 'NumPy Library powerfull', 'Data Science'])
result = np.char.split(arr)
print("Original Array -> \n",arr)
print("Array elements after splitting by space -> \n", result)