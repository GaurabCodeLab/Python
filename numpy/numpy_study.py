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
# arr = np.array([1, 2, 3, 4, 5])
# x = arr.copy()
# y = arr.view()
# print(x.base)  # None
# print(y.base)  # [1 2 3 4 5]

# NumPy Array Shape:-
# arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
# print(arr.shape)  # (2, 4)
# arr = np.array([1, 2, 3, 4], ndmin=5)
# print(arr)  # [[[[[1 2 3 4]]]]]
# print(arr.shape)  # (1, 1, 1, 1, 4)
# Integers at every index tells about the number of elements the corresponding dimension has.
# In the example above at index-4 we have value 4, so we can say that 5th ( 4 + 1 th) dimension has 4 elements.

# NumPy Array Reshaping:-
# Reshaping means changing the shape of an array.
# Reshape From 1-D to 2-D:-
# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
# newarr = arr.reshape(4, 3)
# print(newarr)  # [[ 1  2  3], [ 4  5  6],  [ 7  8  9],  [10 11 12]]
# Reshape From 1-D to 3-D:-
# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
# newarr = arr.reshape(2, 3, 2)
# print(newarr)  #[[[ 1  2]   [ 3  4]   [ 5  6]]  [[ 7  8]   [ 9 10]   [11 12]]]
# We Reshape Into any Shape as long as the elements required for reshaping are equal in both shapes.
# We can reshape an 8 elements 1D array into 4 elements in 2 rows 2D array but we cannot reshape it into a 3 elements 3 rows 2D array as that would require 3x3 = 9 elements.
# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
# reshaped_arr = arr.reshape(2, 4)
# print(reshaped_arr)  # [[1 2 3 4]  [5 6 7 8]]
# print(reshaped_arr.base)  # [1 2 3 4 5 6 7 8]
# array reshape returns view
# You are allowed to have one "unknown" dimension.
# Meaning that you do not have to specify an exact number for one of the dimensions in the reshape method.
# Pass -1 as the value, and NumPy will calculate this number for you.
# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
# newarr = arr.reshape(2, 2, -1)
# print(newarr)  # [[[1 2]   [3 4]]  [[5 6]   [7 8]]]
# We can not pass -1 to more than one dimension.
# Flattening array means converting a multidimensional array into a 1D array.
# We can use reshape(-1) to do this.
# arr = np.array([[1, 2, 3], [4, 5, 6]])
# newarr = arr.reshape(-1)
# print(newarr)  # [1 2 3 4 5 6]

# NumPy Array Iterating:-
# arr = np.array([1, 2, 3])
# for x in arr:
#   print(x)
# output 
# 1
# 2
# 3
# arr = np.array([[1, 2, 3], [4, 5, 6]])
# for x in arr:
#   print(x)
# output
# [1 2 3]
# [4 5 6]
# If we iterate on a n-D array it will go through n-1th dimension one by one.
# arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
# for x in np.nditer(arr):
#   print(x)
# output
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
# for x in np.nditer(arr[:, ::2]):
#   print(x)
# output:-
# 1
# 3
# 5
# 7
# arr = np.array([1, 2, 3])
# for idx, x in np.ndenumerate(arr):
#   print(idx, x)
# output:-
# (0,) 1
# (1,) 2
# (2,) 3
# arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
# for raja, x in np.ndenumerate(arr):
#   print(raja, x)
# output:-
# (0, 0) 1
# (0, 1) 2
# (0, 2) 3
# (0, 3) 4
# (1, 0) 5
# (1, 1) 6
# (1, 2) 7
# (1, 3) 8

# NumPy Joining Array:-
# arr1 = np.array([1, 2, 3])
# arr2 = np.array([4, 5, 6])
# arr = np.concatenate((arr1, arr2))  #  If axis is not explicitly passed, it is taken as 0.
# print(arr)  # [1 2 3 4 5 6]
# arr1 = np.array([[1, 2], [3, 4]])
# arr2 = np.array([[5, 6], [7, 8]])
# arr = np.concatenate((arr1, arr2), axis=1) # axis =1 means along rows
# print(arr)  # [[1 2 5 6]  [3 4 7 8]]
# arr1 = np.array([1, 2, 3])
# arr2 = np.array([4, 5, 6])
# arr = np.stack((arr1, arr2), axis=1)  # If axis is not explicitly passed it is taken as 0.
# print(arr)  # [[1 4]  [2 5]  [3 6]]
# arr1 = np.array([1, 2, 3])
# arr2 = np.array([4, 5, 6])
# arr = np.hstack((arr1, arr2))  # Stacking Along Rows
# print(arr)  # [1 2 3 4 5 6]
# arr1 = np.array([1, 2, 3])
# arr2 = np.array([4, 5, 6])
# arr = np.vstack((arr1, arr2))  # Stacking Along Columns
# print(arr)  # [[1 2 3]  [4 5 6]]
# arr1 = np.array([1, 2, 3])
# arr2 = np.array([4, 5, 6])
# arr = np.dstack((arr1, arr2))  # Stacking Along Height (depth)
# print(arr)  # [[[1 4] [2 5] [3 6]]]

# NumPy Splitting Array:-
# Splitting is reverse operation of Joining.
# arr = np.array([1, 2, 3, 4, 5, 6])
# newarr = np.array_split(arr, 10)
# print(newarr)  # [array([1, 2]), array([3, 4]), array([5, 6])]
# If the array has less elements than required, it will adjust from the end accordingly.
# arr = np.array([1, 2, 3, 4, 5, 6])
# newarr = np.array_split(arr, 4)
# print(newarr)  # [array([1, 2]), array([3, 4]), array([5]), array([6])]
# arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
# newarr = np.array_split(arr, 3)
# print(newarr)  # [array([[1, 2], [3, 4]]), array([[5, 6], [7, 8]]), array([[ 9, 10], [11, 12]])]
# arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
# newarr = np.array_split(arr, 3, axis=1)  # axis = 1 means along columns
# print(newarr)  # [array([[ 1], [ 4], [ 7], [10], [13], [16]]), array([[ 2], [ 5], [ 8], [11], [14], [17]]), array([[ 3], [ 6], [ 9], [12], [15], [18]])]
# An alternate solution is using hsplit() opposite of hstack()
# arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
# newarr = np.hsplit(arr, 3)
# print(newarr) # same as previous
# Note: Similar alternates to vstack() and dstack() are available as vsplit() and dsplit()

# NumPy Searching Arrays:-
# arr = np.array([1, 2, 3, 4, 5, 4, 4])
# x = np.where(arr == 4)
# print(x)  # (array([3, 5, 6]),)
# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
# x = np.where(arr%2 == 0)
# print(x)  # (array([1, 3, 5, 7]),)

# NumPy Sorting Arrays:-
# arr = np.array([3, 2, 0, 1])
# print(np.sort(arr))  # [0 1 2 3]
# # Note: This method returns a copy of the array, leaving the original array unchanged.
# arr = np.array(['banana', 'cherry', 'apple'])
# print(np.sort(arr))  # ['apple' 'banana' 'cherry']
# arr = np.array([True, False, True])
# print(np.sort(arr))  # [False  True  True]
# arr = np.array([[3, 2, 4], [5, 0, 1]])
# print(np.sort(arr))  # [[2 3 4]  [0 1 5]]
# arr = np.array([[3, 2, 4], ["ram", "sita", "aanar"]])
# print(np.sort(arr))  # [['2' '3' '4']  ['aanar' 'ram' 'sita']]

# NumPy Filter Array:-
# Getting some elements out of an existing array and creating a new array out of them is called filtering.
# In NumPy, you filter an array using a boolean index list.
# A boolean index list is a list of booleans corresponding to indexes in the array.
# If the value at an index is True that element is contained in the filtered array, if the value at that index is False that element is excluded from the filtered array.
# arr = np.array([41, 42, 43, 44])
# x = [True, False, True, False]
# newarr = arr[x]
# print(newarr)  # [41 43]
# arr = np.array([41, 42, 43, 44])
# filter_arr = arr > 42
# newarr = arr[filter_arr]
# print(filter_arr)  # [False False  True  True]
# print(newarr)  # [43 44]
# arr = np.array([1, 2, 3, 4, 5, 6, 7])
# filter_arr = arr % 2 == 0
# newarr = arr[filter_arr]
# print(filter_arr)  # [False  True False  True False  True False]
# print(newarr)  # [2 4 6]



  




 

 

 
      




















