from numpy import random
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# x = random.randint(100) #  a random integer from 0 to 100, pseudo random numbers
# print(x) # 15
# x = random.rand() # a random float from 0 to 1
# print(x) # 0.883400024177884
# x = random.randint(100, size=(5))
# print(x) # [14 12 90 73 65]
# x = random.randint(100, size=(5, 3))
# print(x) # [[ 9  9 85] [35 19 68] [71 63 43] [80 87 79] [10 45 62]]
# x = random.rand(5) # 1-D array containing 5 random floats
# print(x) # [0.97279646 0.26912691 0.06048659 0.97125199 0.6323029 ]
# x = random.rand(3,5) #2-D array with 3 rows, each row containing 5 random numbers
# print(x) # [[0.49517135 0.39301166 0.89220681 0.25620341 0.80600669]  [0.93902835 0.56204632 0.9759248  0.09300322 0.35129102]  [0.84297517 0.00612994 0.34873047 0.05312464 0.47618796]]
# x = random.choice([1,2,3,4,5]) # The choice() method takes an array as a parameter and randomly returns one of the values
# print(x) # 5
# x = random.choice([5,6,7,8], size=(2,3))
# print(x) # [[6 8 6]  [6 6 8]]
# x = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(100)) # p is probability of each value of array
# print(x) # [7 7 7 7 7 7 3 7 5 7 7 7 7 5 5 3 7 3 3 7 7 7 5 5 7 7 7 7 7 7 7 7 5 7 7 5 5 7 7 7 7 3 7 3 5 7 7 7 7 5 7 5 7 5 7 5 5 5 7 7 7 7 5 3 7 3 7 7 5 7 7 5 7 3 3 7 7 7 5 5 7 5 7 7 7 7 7 7 7 7 7 7 7 7 7 5 7 3 5 5]
# The sum of all probability numbers should be 1
# Even if you run the example above 100 times, the value 9 will never occur
# x = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(3, 5))
# print(x) # [[7 7 7 7 7]  [7 3 7 3 5]  [3 5 7 7 5]]

# Random Permutations:-
# A permutation refers to an arrangement of elements. e.g. [3, 2, 1] is a permutation of [1, 2, 3] and vice-versa.
# arr = np.array([1, 2, 3, 4, 5])
# random.shuffle(arr)
# print(arr) # [4 2 3 1 5]
# The shuffle() method makes changes to the original array.
# arr = np.array([1, 2, 3, 4, 5])
# print(random.permutation(arr)) # [4 5 2 3 1]
# The permutation() method returns a re-arranged array (and leaves the original array un-changed).

# Seaborn Module:-
# Seaborn is a library that uses Matplotlib underneath to plot graphs. It will be used to visualize random distributions.
# sns.displot([0, 1, 2, 3, 4, 5])
# plt.show()
# sns.displot([0, 1, 2, 3, 4, 5], kind="kde") #  Displot Without the Histogram
# plt.show()

# Normal (Gaussian) Distribution
# x = random.normal(size=(2, 3))
# print(x)  # [[-0.36019464  1.66271967 -0.02607124] [ 1.34615064  1.55078982  1.2342744 ]]
# x = random.normal(loc=1, scale=2, size=(2, 3)) # random normal distribution of size 2x3 with mean at 1 and standard deviation of 2
# print(x)  # [[-0.86634158 -1.54642457  3.40072253] [ 6.14453341  0.92269903  1.56052634]]
# sns.displot(random.normal(size=1000), kind="kde")
# plt.show()
# Note: The curve of a Normal Distribution is also known as the Bell Curve because of the bell-shaped curve.

# Binomial Distribution:-
# Binomial Distribution is a Discrete Distribution.
# x = random.binomial(n=10, p=0.5, size=10)
# print(x)  # [6 3 2 6 2 5 2 6 3 5]
# sns.displot(random.binomial(n=10, p=0.5, size=1000))
# plt.show()
# normal distribution is continous whereas binomial is discrete
# data = {
#   "normal": random.normal(loc=50, scale=5, size=1000),
#   "binomial": random.binomial(n=100, p=0.5, size=1000)
# }
# sns.displot(data, kind="kde")
# plt.show()

# Poisson Distribution:-
# Poisson Distribution is a Discrete Distribution.
# x = random.poisson(lam=2, size=10)
# print(x)  # [3 2 2 0 0 3 2 2 1 3]
# sns.displot(random.poisson(lam=2, size=1000))
# plt.show()
# data = {
#   "normal": random.normal(loc=50, scale=7, size=1000),
#   "poisson": random.poisson(lam=50, size=1000)
# }
# sns.displot(data, kind="kde")
# plt.show()
data = {
  "binomial": random.binomial(n=1000, p=0.01, size=1000),
  "poisson": random.poisson(lam=10, size=1000)
}
sns.displot(data, kind="kde")
plt.show()















