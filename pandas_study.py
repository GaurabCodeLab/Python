# check version of pandas:-
import pandas as pd
import matplotlib.pyplot as plt
# print(pd.__version__)

# pandas Series:-
a = [1, 7, 2]
# s = pd.Series(a)
# print(s)
# print(s[1]) # accessing a particular value from series
# myvar = pd.Series(a, index = ["x", "y", "z"])
# print(myvar)
# print(myvar["y"])
# calories = {"day1": 420, "day2": 380, "day3": 390}
# myvar = pd.Series(calories)
# print(myvar)
# print(myvar["day2"])
# calories = {"day1": 420, "day2": 380, "day3": 390}
# myvar = pd.Series(calories, index = ["day1", "day3"])
# print(myvar)

# pandas Dataframe:-
# data = {
#   "calories": [420, 380, 390],
#   "duration": [50, 40, 45]
# }
# df = pd.DataFrame(data, index = ["day1", "day2", "day3"]) # index argument, can name your own indexes
# print(df)
# print(df["duration"])  # used to select a column
# print(df.loc[2]) # return series
# print(df.loc[[0, 2]]) # return DataFrame
# print(df.loc["day1":"day3", "duration"])

# load csv files:-
# df = pd.read_csv('data.csv')
# print(df.to_string())  # use to_string() to print the entire DataFrame, having large DataFrame with many rows, Pandas will only return the first 5 rows, and the last 5 rows:
# print(pd.options.display.max_rows) # In my system the number is 60, which means that if the DataFrame contains more than 60 rows, the print(df) statement will return only the headers and the first and last 5 rows.
# change the maximum rows number with the same statement.
# pd.options.display.max_rows = 9999
# print(pd.options.display.max_rows) # 9999
# print(df.head()) # return first 5 rows of dataframe
# print(df.head(23))
# print(df.tail()) # return last 5 rows of dataframe
# print(df.tail(23))
# print(df.info())
# print(df.describe())

# load json files:-
# df = pd.read_json("data.json")
# # print(df)
# data = {
#   "Duration":{
#     "0":60,
#     "1":60,
#     "2":60,
#     "3":45,
#     "4":45,
#     "5":60
#   },
#   "Pulse":{
#     "0":110,
#     "1":117,
#     "2":103,
#     "3":109,
#     "4":117,
#     "5":102
#   },}
# print(pd.DataFrame(data))

# Cleaning Data

# 1. Empty Cells:-
df = pd.read_csv("data1.csv")
# new_df = df.dropna()
# print(new_df)
# By default, the dropna() method returns a new DataFrame, and will not change the original
# If you want to change the original DataFrame, use the inplace = True argument:
# df.dropna(inplace = True)
# Note: Now, the dropna(inplace = True) will NOT return a new DataFrame, but it will remove all rows containing NULL values from the original DataFrame.
# df.fillna(130, inplace = True) # replaces all empty cells in the whole Data Frame.
# df.fillna({"Calories": 130}, inplace=True) #This operation inserts 130 in empty cells in the "Calories" column
# x = df["Calories"].mean()
# df.fillna({"Calories": x}, inplace=True)
# x = df["Calories"].median()
# df.fillna({"Calories": x}, inplace=True)
# x = df["Calories"].mode()[0]
# df.fillna({"Calories": x}, inplace=True)

# 2. Wrong Format Data:-
# df['Date'] = pd.to_datetime(df['Date'], format='mixed')
# print(df.to_string())
# df["Calories"] = pd.to_numeric(df["Calories"], errors="raise")  # convert to numeric value
# errors : {'ignore', 'raise', 'coerce'}, default 'raise'
# If 'raise', then invalid parsing will raise an exception.
# If 'coerce', then invalid parsing will be set as NaN.
# If 'ignore', then invalid parsing will return the input.

# Wrong Data:-
# df.loc[7,'Duration'] = 45
# print(df.to_string())
# for x in df.index:
#   if df.loc[x, "Duration"] > 120:
#     df.loc[x, "Duration"] = 120
# for x in df.index:
#   if df.loc[x, "Duration"] > 120:
#     df.drop(x, inplace = True)

# Removing Duplicates:-
# print(df.duplicated())  # Returns True for every row that is a duplicate, otherwise False:
# df.drop_duplicates(inplace = True)

# Pandas Correlations:-
# df = pd.read_csv('data.csv')
# print(df.corr())

# Pandas Plotting:-
df = pd.read_csv('data.csv')
# df.plot()
# plt.show()
# df.plot(kind = 'scatter', x = 'Duration', y = 'Calories')
# plt.show()
# df.plot(kind = 'scatter', x = 'Duration', y = 'Maxpulse')
# plt.show()
df["Duration"].plot(kind = 'hist')
plt.show()

