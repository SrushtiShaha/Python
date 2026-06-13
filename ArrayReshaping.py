#ArrayReshaping
import numpy as np
arr = np.array([1,2,3,4,5,6])
print("Array -> \n", arr)
reshaped2d = arr.reshape(2,3)
print("1D to 2D -> \n",reshaped2d)
reshaped3d = arr.reshape(2,3,1)
print("1D to 3D -> \n",reshaped3d)

#Flatten multidimentional array using - revel() & flatten()
flat1 = reshaped2d.ravel()
print("Ravel array -> \n",flat1)
flat2 = reshaped2d.flatten()
print("Flatten array -> \n",flat2)

auto = arr.reshape(3, -1)
print("Automatic dimension -> \n",auto)