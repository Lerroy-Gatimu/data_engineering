#To fix it, you have two options: remove the rows, or convert all cells in the columns into the same format

import pandas as pd
data = pd.read_csv ("data.csv")

data ["Date"] = pd.to_datetime (data ["Date"], format = "mixed")
print (data.to_string())

'''
Removing Rows
The result from the converting in the example above gave us a NaT value, which can be handled as a NULL value, and we can remove the row by using the dropna() method.

Example
Remove rows with a NULL value in the "Date" column:'''

data.dropna (subset=['Date'], inplace=True)