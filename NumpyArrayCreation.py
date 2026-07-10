import numpy as np


#Array Using np.array()

arr1 = np.array([1,2,3,4,5])
print("1D Array : \n", arr1)
arr2 = np.array([[1,2,3], [4,5,6]])
print("2D Array : \n", arr2)
arr3 = np.array([[[1,2,3], [4,5,6], [7,8,9]]])
print("3D Array : \n", arr3)

#Array using np.zeros()

z = np.zeros((2,3))
print("Array using zeros() function : \n", z)

#Array using np.ones()

o = np.ones((3,2))
print("Array using ones() function : \n", o)

#Array using np.arrange()

a = np.arange(0, 10, 2)
print("Array using arange() function : \n", a)

#Array using np.linspace()

l = np.linspace(0, 1, 5)
print("Array using linspace() function : \n", l)

#Array using np.eye()

i = np.eye(3)
print("Array using eye() function : \n", i)