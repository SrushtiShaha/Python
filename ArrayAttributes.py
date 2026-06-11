import numpy as np

#Array 
arr = np.array([[1,2,3], [4,5,6]])
print("Array -> \n", arr)

#ndim
print("Number of dimensions -> ",arr.ndim)

#shape
print("Shape of array -> ",arr.shape)

#size
print("Total number of elements -> ",arr.size)

#dtype
print("Data type of elements -> ",arr.dtype)

#itemsize
print("Size of each element -> ",arr.itemsize)

#nbytes
print("Total memory used by array -> ",arr.nbytes)