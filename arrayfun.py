import numpy as np

#1D array
one_array = np.array([2, 3, 4, 5, 6])
print(one_array)

#find dimension
print(one_array.ndim)

#2D array
two_array = np.array([[2,3,4,5],[6,7,8,9]])
print(two_array)

#find dimension
print(two_array.ndim)

#3D array 
three_array = np.array([[[1,3,2,4],[2,4,5,6],[2,3,4,5]],[[1,2,3,7],[4,5,6,7],[6,7,8,4]]])
print(three_array)

#find dimemsion
print(three_array.ndim)