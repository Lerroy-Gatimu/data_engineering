#A Pandas Series is like a column in a table.
#It is a one-dimensional array holding data of any type.

import pandas as pd

a = [1,2,3]
myvar = pd.Series (a)

print (myvar)

'''
Labels
If nothing else is specified, the values are labeled with their index number. First value has index 0, second value has index 1 etc.

This label can be used to access a specified value.

Example
Return the first value of the Series:
'''

print(myvar[0])

'''Create Labels
With the index argument, you can name your own labels.

Example
Create your own labels:'''

import pandas as pd
a = [1,2,3]
myvar = pd.Series (a, index = ["x","y","z"])

print(myvar)

'''Key/Value Objects as Series
You can also use a key/value object, like a dictionary, when creating a Series.

Example
Create a simple Pandas Series from a dictionary:'''

import pandas as pd

calories = {"day1": 420, "day2": 380, "day3": 390}

myvar = pd.Series(calories)

print(myvar)

#Note: The keys of the dictionary become the labels.

#Create a Series using only data from "day1" and "day2":

import pandas as pd

calories = {"day1": 420, "day2": 380, "day3": 390}

myvar = pd.Series(calories, index = ["day1", "day2"])

print(myvar)