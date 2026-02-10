# Install NumPy using the below command:-
# pip install numpy (provided python and pip is already installed in your system)

# The array object in NumPy is called ndarray.

# check numpy version:-
import numpy as np
# print(np.__version__)

# create a numpy array:-
# arr = np.array([1,2,3,4,5])
# print(arr)  # [1 2 3 4 5]
# print(type(arr))  # <class 'numpy.ndarray'>
# arr2 = np.array((1,2,3,4,5))
# print(arr2)  # [1 2 3 4 5]

# Dimension of array:-
# arr_0D = np.array(21)
# print(arr_0D)  # 0-D array
# print(arr_0D.ndim) # 0
# arr_1D = np.array([1,2,3,4,5])
# print(arr_1D) # 1-D array
# print(arr_1D.ndim) # 1
# arr_2D = np.array([[1,2,3], [4,5,6]])
# print(arr_2D) # 2-D array
# print(arr_2D.ndim) # 2
# arr_3D = np.array([[[1,2,3], [4,5,6]], [[1,2,3], [4,5,6]]])
# print(arr_3D) # 2-D array
# print(arr_3D.ndim) # 3
# arr = np.array([1,2,3,4], ndmin=5)
# print(arr) # [[[[[1 2 3 4]]]]]
# print(arr.ndim) # 5

# Array Indexing:-
# arr = np.array([1, 2, 3, 4])
# print(arr[1])
# arr2 = np.array([[1,2,3,4,5], [6,7,8,9,10]]) 
# print(arr2[1, 3])  #  9
# arr3 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
# print(arr3[0, 1, 2]) # 6
# arr4 = np.array([[1,2,3,4,5], [6,7,8,9,10]])
# print(arr4[1, -1]) # 10
