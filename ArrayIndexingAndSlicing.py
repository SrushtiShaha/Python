import numpy as np

#1D Array
arr1 = np.array([10,20,30,40,50])

#2D Array
arr2 = np.array([[1,2,3], [4,5,6]])

#Accessing Element
print("1D Array -> \n", arr1)
print("2D Array -> \n", arr2)
print("Accessing array element -> ")
print(arr1[0])
print(arr1[-1])
print(arr2[0,0])
print(arr2[1,0])

#Slicing
print("Slicing -> ")
print(arr1[1:2])
print(arr1[:2])
print(arr1[1:])
print(arr1[::2])

print(arr2[0:1, 1:3])
print(arr2[:, 0])
print(arr2[1, :])

#Reversing
rev = arr1[::-1]
print(rev)
print(arr2[::-1])
print(arr2[:, ::-1])
print(arr2[::-1, ::-1])

#Specific row and column
row = arr2[[0,1], :]
print(row)