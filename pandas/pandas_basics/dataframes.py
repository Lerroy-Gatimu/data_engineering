#Data sets in Pandas are usually multi-dimensional tables, called DataFrames.
#Series is like a column, a DataFrame is the whole table.

#Create a DataFrame from two Series:

import pandas as pd

x = {
  "Day 1" : ["Monday", 1],
  "Day 2" : ["Tuesday", 2]
}

y = pd.DataFrame (x)
print (y)

'''Locate Row
As you can see from the result above, the DataFrame is like a table with rows and columns.

Pandas use the loc attribute to return one or more specified row(s)

Example
Return row 0:'''

#refer to the row index:
print(y.loc[0])

#Return row 0 and 1:
#use a list of indexes:
print(y.loc[[0, 1]])

#Note: When using [], the result is a Pandas DataFrame, if it's one, it will be a series

'''
Named Indexes
With the index argument, you can name your own indexes.

Example
Add a list of names to give each row a name:'''

import pandas as pd
data = {
  "Batch A" : [1,2,3,4,5],
  "Batch B" : [6,7,8,9,10],
  "Batch C" : [11,12,13,14,15]
}

df = pd.DataFrame (data, index=["One", "Two", "Three", "Four", "Five"])

print (df)
print (df.loc["Two"])
print (df.loc[["Three", "Two"]])