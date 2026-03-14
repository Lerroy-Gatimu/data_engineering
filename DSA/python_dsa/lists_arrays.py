'''
Python Lists and Arrays
In Python, lists are the built-in data structure that serves as a dynamic array.
Lists are ordered, mutable, and can contain elements of different types.
Lists are created using square brackets []

Python lists come with several built-in algorithms (called methods), to perform common operations like appending, sorting, and more.
'''
x = [9, 12, 7, 4, 11]
# Add element:
x.append(8)
# Sort list ascending:
x.sort()
print(x)

'''
Create Algorithms
Sometimes we want to perform actions that are not built into Python.

Then we can create our own algorithms.

For example, an algorithm can be used to find the lowest value in a list, like in the example below:

Example
Create an algorithm to find the lowest value in a list:
'''
my_array = [7, 12, 9, 4, 11, 8]
minVal = my_array[0]

for i in my_array:
  if i < minVal:
    minVal = i

print('Lowest value:', minVal)

'''
The algorithm above is very simple, and fast enough for small data sets, but if the data is big enough, any algorithm will take time to run.
This is where optimization comes in.
Optimization is an important part of algorithm development, and of course, an important part of DSA programming.

In the example above, the time the algorithm needs to run is proportional, or linear, to the size of the data set. This is because the algorithm must visit every array element one time to find the lowest value. The loop must run 5 times since there are 5 values in the array. And if the array had 1000 values, the loop would have to run 1000 times.
'''

