# to check version:-
# import matplotlib
# print(matplotlib.__version__)

import matplotlib.pyplot as plt
import numpy as np

# line graph:-
x1 = np.array([2,4,6,8])
y1 = np.array([3,6,9,12])
x2 = np.array([10,15,19,32])
y2 = np.array([81,23,56,22])
# xpoints is optional, if not specified it will take as [0,1,2,3]
plt.plot(x1, y1,x2, y2, color="red", marker="*", markersize=10, markeredgecolor="green", markerfacecolor="yellow", linestyle="dashed", linewidth=10)
# plt.plot(x2, y2)
font = {'family':'serif','color':'blue','size':10}
plt.xlabel("raja", color="cyan", fontdict=font)
plt.ylabel("dolly", color="pink", fontdict=font)
plt.title("my matplotlib learning", color="red", fontdict=font, loc="left")
plt.grid(axis="both", color="green", linestyle="dotted", linewidth=2) # possible values are axis="x", axis="y", axis="both"
plt.show()

#  Scatter diagram:-
# xpoints = np.array([1,2,3,4,5])
# ypoints = np.array([12,20,33,44,22,])
# plt.scatter(xpoints, ypoints, color="green")
# xpoints = np.array([12,23,344,43,51])
# ypoints = np.array([23,24,3,34,2,])
# plt.scatter(xpoints, ypoints, color="yellow")
# plt.show()

# Bar Chart:-
# x = np.array(["A", "B", "C"])
# y = np.array([12, 34, 22])
# # plt.bar(x,y, color="red", width=0.1)
# plt.barh(x,y, color="green", height=0.1)
# plt.xlabel("rama jee", color="tomato")
# plt.ylabel("krishna jee")
# plt.show()

# histogram chart:-
# x = np.random.normal(150, 15, 200)
# plt.hist(x, color="red")
# plt.show()

# Pie chart:-
# y = np.array([15, 25, 40, 20])
# plt.pie(y, labels=["ram", "lakshman", "bharat", "satrudhan"], colors=["red", "green", "orange", "black"], explode=[0.1, 0.2, 0, 0], shadow=False, startangle=90)
# plt.legend(title="dasrath ke bete")
# plt.show()
