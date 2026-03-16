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
# data = {
#   "binomial": random.binomial(n=1000, p=0.01, size=1000),
#   "poisson": random.poisson(lam=10, size=1000)
# }
# sns.displot(data, kind="kde")
# plt.show()

# Uniform Distribution:-
# Used to describe probability where every event has equal chances of occuring.
# x = random.uniform(size=(2, 3))
# print(x) # [[0.01359661 0.58884887 0.93528197] [0.6438507  0.58748739 0.31764499]]
# sns.displot(random.uniform(size=1000), kind="kde")
# plt.show()

# Logistic Distribution:-
# x = random.logistic(loc=1, scale=2, size=(2, 3)) # Draw 2x3 samples from a logistic distribution with mean at 1 and stddev 2.0
# print(x)  # [[2.34841462 1.09674752 0.82624434] [0.70507402 1.51467193 0.10942292]]
# sns.displot(random.logistic(size=1000), kind="kde")
# plt.show()
# data = {
#   "normal": random.normal(scale=2, size=1000),
#   "logistic": random.logistic(size=1000)
# }
# sns.displot(data, kind="kde")
# plt.show()

# Multinomial Distribution:-
# Multinomial distribution is a generalization of binomial distribution.
# x = random.multinomial(n=6, pvals=[1/6, 1/6, 1/6, 1/6, 1/6, 1/6])
# print(x) # [3 0 3 0 0 0]
# Note: Multinomial samples will NOT produce a single value! They will produce one value for each pval

# Exponential Distribution:-
# x = random.exponential(scale=2, size=(2, 3))
# print(x)  # [[3.89766686 0.47145764 2.00666189] [0.0439367  0.5086273  1.09567157]]
# sns.displot(random.exponential(size=1000), kind="kde")
# plt.show()
# Poisson distribution deals with number of occurences of an event in a time period whereas exponential distribution deals with the time between these events.

# Chi Square Distribution:-
# x = random.chisquare(df=2, size=(2, 3)) # chi squared distribution with degree of freedom 2 with size 2x3:
# print(x)  # [[1.45078524 5.09094235 3.34107459] [1.6718828  1.35365044 0.23864214]]
# sns.displot(random.chisquare(df=1, size=1000), kind="kde")
# plt.show()

# Rayleigh Distribution:-
# x = random.rayleigh(scale=2, size=(2, 3))  # rayleigh distribution with scale of 2 with size 2x3
# print(x)  # [[3.40264931 5.6877841  2.19810089] [3.89322192 0.98014182 0.74223543]]
# sns.displot(random.rayleigh(size=1000), kind="kde")
# plt.show()
# At unit stddev and 2 degrees of freedom rayleigh and chi square represent the same distributions.














