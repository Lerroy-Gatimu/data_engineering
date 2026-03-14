import pandas as pd
data = pd.read_csv ("data.csv")

print (data.head(30).duplicated())

'''Removing Duplicates
To remove duplicates, use the drop_duplicates() method.

Example
Remove all duplicates:'''

data.drop_duplicates(inplace = True)