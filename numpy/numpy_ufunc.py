# ufuncs stands for "Universal Functions" and they are NumPy functions that operate on the ndarray object.
# ufuncs (Universal Functions) are used to implement vectorization in NumPy which is way faster than iterating over elements.

import numpy as np

# Check if a Function is a ufunc:-
# print(type(np.add))  # <class 'numpy.ufunc'>
# print(type(np.concatenate))  # <class 'numpy._ArrayFunctionDispatcher'>
# print(type(np.gaurab))  # AttributeError: module 'numpy' has no attribute 'gaurab'
# print(np.ufunc)  # <class 'numpy.ufunc'>
# print(type(np.add)==np.ufunc)  # True
# print(type(np.concatenate)==np.ufunc)  # False

# Simple Arithmetic:-
# arr1 = np.array([10, 11, 12, 13, 14, 15])
# arr2 = np.array([20, 21, 22, 23, 24, 25])
# newarr = np.add(arr1, arr2)
# print(newarr)  # [30 32 34 36 38 40]
# arr1 = np.array([10, 20, 30, 40, 50, 60])
# arr2 = np.array([20, 21, 22, 23, 24, 25])
# newarr = np.subtract(arr1, arr2)
# print(newarr)  # [-10  -1   8  17  26  35]
# arr1 = np.array([10, 20, 30, 40, 50, 60])
# arr2 = np.array([20, 21, 22, 23, 24, 25])
# newarr = np.multiply(arr1, arr2)
# print(newarr)  # [ 200  420  660  920 1200 1500]
# arr1 = np.array([10, 20, 30, 40, 50, 60])
# arr2 = np.array([3, 5, 10, 8, 2, 33])
# newarr = np.divide(arr1, arr2)
# print(newarr)  # [ 3.33333333  4. 3. 5. 25. 1.81818182]
# arr1 = np.array([10, 20, 30, 40, 50, 60])
# arr2 = np.array([3, 5, 6, 8, 2, 33])
# newarr = np.power(arr1, arr2)
# print(newarr)  # [1000 3200000 729000000 6553600000000 2500 0]
# arr1 = np.array([10, 20, 30, 40, 50, 60])
# arr2 = np.array([3, 7, 9, 8, 2, 33])
# newarr = np.mod(arr1, arr2)
# print(newarr)  # [ 1  6  3  0  0 27]
# # You get the same result when using the remainder() function
# newarr = np.remainder(arr1, arr2)
# print(newarr)  # [ 1  6  3  0  0 27]
# arr1 = np.array([10, 20, 30, 40, 50, 60])
# arr2 = np.array([3, 7, 9, 8, 2, 33])
# newarr = np.divmod(arr1, arr2)
# print(newarr)  # (array([ 3,  2,  3,  5, 25,  1]), array([ 1,  6,  3,  0,  0, 27]))
# arr = np.array([-1, -2, 1, 2, 3, -4])
# newarr = np.absolute(arr)
# print(newarr)  # [1 2 1 2 3 4]

# Rounding Decimals:-
# arr = np.trunc([-3.1666, 3.6667])
# print(arr)  # [-3.  3.]
# print(np.trunc(4.99))  # 4.0
# arr = np.fix([-3.1666, 3.6667])
# print(np.fix(4.99))  # 4.0
# print(arr)  # [-3.  3.]
# arr = np.around(3.1666, 2)  # The around() function increments preceding digit or decimal by 1 if >=5 else do nothing
# print(arr)  # 3.17
# if we don't pass the second argument, it takes default value as 0
# print(np.around(np.array([4.6789, -4.6789]), 2))  # [ 4.68 -4.68]
# arr = np.floor([-3.1666, 3.6667])
# print(arr)  # [-4.  3.]
# print(np.floor(4.99))  # 4.0
# arr = np.ceil([-3.1666, 3.6667])
# print(arr)  # [-3.  4.]
# print(np.ceil(4.999))  # 5.0

# NumPy Logs:-
# arr = np.arange(1, 10)
# print(np.log2(arr))  # [0. 1. 1.5849625  2. 2.32192809 2.5849625 2.80735492 3. 3.169925  ]
# Note: The arange(1, 10) function returns an array with integers starting from 1 (included) to 10 (not included).
# print(np.log2(2))  # 1.0
# print(np.log10(arr))  # [0. 0.30103 0.47712125 0.60205999 0.69897 0.77815125 0.84509804 0.90308999 0.95424251]
# print(np.log10(2))  # 0.3010299956639812
# print(np.log(arr))  # find Natural Log, or Log at Base e, [0.  0.69314718 1.09861229 1.38629436 1.60943791 1.79175947 1.94591015 2.07944154 2.19722458]
# print(np.log(2))  # 0.6931471805599453
# print(np.log(0))  # -inf

# NumPy Summations:-
# Addition is done between two arguments whereas summation happens over n elements.
# arr1 = np.array([1, 2, 3])
# arr2 = np.array([1, 2, 3])
# newarr = np.sum([arr1, arr2])
# print(newarr)  # 12
# newarr = np.sum([arr1, arr2], axis=1)
# print(newarr)  # [6 6]
# arr = np.array([1, 2, 3])
# newarr = np.cumsum(arr)
# print(newarr)  # [1 3 6]

# NumPy Products:-
# arr = np.array([1, 2, 3, 4])
# x = np.prod(arr)
# print(x)  # 24
# arr1 = np.array([1, 2, 3, 4])
# arr2 = np.array([5, 6, 7, 8])
# x = np.prod([arr1, arr2])
# print(x)  # 40320, because 1*2*3*4*5*6*7*8 = 40320
# newarr = np.prod([arr1, arr2], axis=1)
# print(newarr)  # [  24 1680]
# arr = np.array([5, 6, 7, 8])
# newarr = np.cumprod(arr)
# print(newarr)  # [   5   30  210 1680]

# NumPy Differences:-
# arr = np.array([10, 15, 25, 5])
# newarr = np.diff(arr) # Compute discrete difference (A discrete difference means subtracting two successive elements)
# print(newarr)  # [  5  10 -20]
# arr = np.array([10, 15, 25, 5])
# newarr = np.diff(arr, n=2)
# print(newarr)  # [  5 -30]

# NumPy LCM Lowest Common Multiple:-
# num1 = 4
# num2 = 6
# x = np.lcm(num1, num2)
# print(x)  # 12
# arr = np.array([3, 6, 9])
# x = np.lcm.reduce(arr)
# print(x)  # 18

# NumPy GCD Greatest Common Divisor:-
# num1 = 6
# num2 = 9
# x = np.gcd(num1, num2, 12)
# print(x)  # 3
# arr = np.array([20, 8, 32, 36, 16])
# x = np.gcd.reduce(arr)
# print(x)  # 4

# NumPy Trigonometric Functions:-
# x = np.sin(np.pi/2)
# print(x)  # 1.0
# arr = np.array([np.pi/2, np.pi/3, np.pi/4, np.pi/5])
# x = np.sin(arr)
# print(x)  # [1. 0.8660254 0.70710678 0.58778525]
# y = np.deg2rad(22)
# print(y)  # 0.3839724354387525
# arr = np.array([90, 180, 270, 360])
# x = np.deg2rad(arr)
# print(x)  # [1.57079633 3.14159265 4.71238898 6.28318531]
# y = np.rad2deg(12)
# print(y)  # 687.5493541569879
# arr = np.array([np.pi/2, np.pi, 1.5*np.pi, 2*np.pi])
# x = np.rad2deg(arr)
# print(x)  # [ 90. 180. 270. 360.]
# x = np.arcsin(1.0)
# print(x)  # 1.5707963267948966
# arr = np.array([1, -1, 0.1])
# x = np.arcsin(arr)
# print(x)  # [ 1.57079633 -1.57079633  0.10016742]
# base = 3
# perp = 4
# x = np.hypot(base, perp)
# print(x)  # 5.0

# NumPy Hyperbolic Functions:-
# x = np.sinh(np.pi/2)
# print(x)  # 2.3012989023072947
# arr = np.array([np.pi/2, np.pi/3, np.pi/4, np.pi/5])
# x = np.cosh(arr)
# print(x)  # [2.50917848 1.60028686 1.32460909 1.20397209]
# x = np.arcsinh(1.0)
# print(x)  # 0.881373587019543
# arr = np.array([0.1, 0.2, 0.5])
# x = np.arctanh(arr)
# print(x)  # [0.10033535 0.20273255 0.54930614]

# NumPy Set Operations:-
# A set in mathematics is a collection of unique elements.
# arr = np.array([1, 1, 1, 2, 3, 4, 5, 5, 6, 7])
# x = np.unique(arr)
# print(x)  # [1 2 3 4 5 6 7]
# arr1 = np.array([1, 2, 3, 4])
# arr2 = np.array([3, 4, 5, 6])
# newarr = np.union1d(arr1, arr2)
# print(newarr)  # [1 2 3 4 5 6]
# arr1 = np.array([1, 2, 3, 4])
# arr2 = np.array([3, 4, 5, 6])
# newarr = np.intersect1d(arr1, arr2, assume_unique=True)
# print(newarr)  # [3 4]
# Note: the intersect1d() method takes an optional argument assume_unique, which if set to True can speed up computation. It should always be set to True when dealing with sets.
# set1 = np.array([1, 2, 3, 4])
# set2 = np.array([3, 4, 5, 6])
# newarr = np.setdiff1d(set1, set2, assume_unique=True)
# print(newarr)  # [1 2]
# set1 = np.array([1, 2, 3, 4])
# set2 = np.array([3, 4, 5, 6])
# newarr = np.setxor1d(set1, set2, assume_unique=True)  # To find only the values that are NOT present in BOTH sets (Symmetric Difference)
# print(newarr)  # [1 2 5 6]