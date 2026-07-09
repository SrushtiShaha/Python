import numpy as np
arr = np.array([11,33,22,11,11,33,3,2,5,3])
values, count = np.unique(arr, return_counts=True)
most_frequent = values[np.argmax(count)]
print("Array : ",arr)
print("Most Frequent Values : ", most_frequent)