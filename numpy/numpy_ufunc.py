# ufuncs stands for "Universal Functions" and they are NumPy functions that operate on the ndarray object.
# ufuncs (Universal Functions) are used to implement vectorization in NumPy which is way faster than iterating over elements.

import numpy as np

# Check if a Function is a ufunc:-
# print(type(np.add))  # <class 'numpy.ufunc'>
# print(type(np.concatenate))  # <class 'numpy._ArrayFunctionDispatcher'>
# print(type(np.gaurab))  # AttributeError: module 'numpy' has no attribute 'gaurab'
print(np.ufunc)  # <class 'numpy.ufunc'>
print(type(np.add)==np.ufunc)  # True
print(type(np.concatenate)==np.ufunc)  # False


