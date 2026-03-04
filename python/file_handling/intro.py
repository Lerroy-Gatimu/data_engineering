'''
File Handling
The key function for working with files in Python is the open() function.

The open() function takes two parameters; filename, and mode.

There are four different methods (modes) for opening a file:

"r" - Read - Default value. Opens a file for reading, error if the file does not exist

"a" - Append - Opens a file for appending, creates the file if it does not exist

"w" - Write - Opens a file for writing, creates the file if it does not exist

"x" - Create - Creates the specified file, returns an error if the file exists

In addition you can specify if the file should be handled as binary or text mode

"t" - Text - Default value. Text mode

"b" - Binary - Binary mode (e.g. images)
'''

'''
Using the with statement
You can also use the with statement when opening a file:
Example
Using the with keyword:
'''
with open("demofile.txt") as f:
  print(f.read())

'''
Close Files
It is a good practice to always close the file when you are done with it.

If you are not using the with statement, you must write a close statement in order to close the file:

Example
Close the file when you are finished with it:
'''
f = open("demofile.txt")
print(f.readline())
f.close()  

'''
Read Only Parts of the File
By default the read() method returns the whole text, but you can also specify how many characters you want to return:

Example
Return the 5 first characters of the file:
'''
with open("demofile.txt") as f:
  print(f.read(5))
  
'''By calling readline() two times, you can read the two first lines:

Example
Read two lines of the file:'''

with open("demofile.txt") as f:
  print(f.readline())
  print(f.readline())  
  
  
'''By looping through the lines of the file, you can read the whole file, line by line:

Example
Loop through the file line by line:
'''
with open("demofile.txt") as f:
  for x in f:
    print(x)  
    
    