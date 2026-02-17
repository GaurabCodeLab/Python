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
# print(arr_3D) # 3-D array
# print(arr_3D.ndim) # 3
# arr = np.array([1,2,3,4], ndmin=5)
# print(arr) # [[[[[1 2 3 4]]]]]
# print(arr.ndim) # 5

# Array Indexing:-
# arr = np.array([1, 2, 3, 4])
# print(arr[1]) # 2
# arr2 = np.array([[1,2,3,4,5], [6,7,8,9,10]]) 
# print(arr2[1, 3])  #  9
# arr3 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
# print(arr3[0, 1, 2]) # 6
# arr4 = np.array([[1,2,3,4,5], [6,7,8,9,10]])
# print(arr4[1, -1]) # 10

# Array Slicing:-
# arr = np.array([1, 2, 3, 4, 5, 6, 7])
# print(arr[1:5])  # [2 3 4 5]
# print(arr[4:])   # [5 6 7]
# print(arr[:4])   # [1 2 3 4]
# print(arr[-3:-1]) # [5 6]
# print(arr[1:5:2])  # [2 4]
# print(arr[::2])   # [1 3 5 7]
# arr2 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
# print(arr2[1, 1:4])  # [7 8 9]
# print(arr2[0:2, 2])  # [3 8]
# print(arr2[0:2, 2:4]) # [[3,4], [8,9]]
# print(arr2[1, 2]) # 8

# Data Types:-
# arr = np.array([1, 2, 3, 4])
# print(arr.dtype)  # int64
# arr2 = np.array(['apple', 'banana', 'cherry'])
# print(arr2.dtype) # <U6
# arr = np.array([1, 2, 3, 4], dtype='S')
# print(arr) # [b'1' b'2' b'3' b'4']
# print(arr.dtype) # |S1
# arr = np.array([1.1, 2.9, 3.1])
# newarr = arr.astype('i')
# print(newarr)  # [1 2 3]
# print(newarr.dtype)  # int32
# newarr2 = arr.astype(int)
# print(newarr2)  # [1 2 3]
# print(newarr2.dtype)  # int64
# arr = np.array([1, 0, 3])
# newarr = arr.astype(bool)
# print(newarr)  # [ True False  True]
# print(newarr.dtype)  # bool

# NumPy Array Copy vs View:-
# arr = np.array([1, 2, 3, 4, 5])
# x = arr.copy()
# arr[0] = 42
# print(arr)  # [42  2  3  4  5]
# print(x)  # [1 2 3 4 5]
# arr = np.array([1, 2, 3, 4, 5])
# x = arr.view()
# arr[0] = 42
# print(arr)  # [42  2  3  4  5]
# print(x)  # [42  2  3  4  5]
# arr = np.array([1, 2, 3, 4, 5])
# x = arr.view()
# x[0] = 31
# print(arr)  # [31  2  3  4  5]
# print(x)  # [31  2  3  4  5]
arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
y = arr.view()
print(x.base)  # None
print(y.base)  # [1 2 3 4 5]
