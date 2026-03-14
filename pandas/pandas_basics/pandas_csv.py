import pandas as pd
data = pd.read_csv ('retention_sheet_1.csv')
print(data)

'''
Tip: use to_string() to print the entire DataFrame.

If you have a large DataFrame with many rows, Pandas will only return the first 5 rows, and the last 5 rows:

Example
Print the DataFrame without the to_string() method:

import pandas as pd

df = pd.read_csv('data.csv')

print(df) 
'''

'''max_rows
The number of rows returned is defined in Pandas option settings.

You can check your system's maximum rows with the pd.options.display.max_rows statement.

Example
Check the number of maximum returned rows:'''

print (pd.options.display.max_rows)

'''n my system the number is 60, which means that if the DataFrame contains more than 60 rows, the print(df) statement will return only the headers and the first and last 5 rows.

You can change the maximum rows number with the same statement.

Example
Increase the maximum number of rows to display the entire DataFrame:'''

import pandas as pd

pd.options.display.max_rows = 9999

df = pd.read_csv('data.csv')

print(df) 