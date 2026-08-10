import numpy as np
arr = np.array([15,3,29,20,37,1,11,5])
print("Original Array : ", arr)
n = int(input("Enter the number of element to sort from beginning : "))
sorted_part = np.sort(arr[:n])
remaining_part = arr[:n]
result = np.concatenate((sorted_part, remaining_part))
print("Array after sorting first : ", n, "element", result)