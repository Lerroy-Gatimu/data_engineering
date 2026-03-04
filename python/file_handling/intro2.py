'''
Write to an Existing File
To write to an existing file, you must add a parameter to the open() function:

"a" - Append - will append to the end of the file

"w" - Write - will overwrite any existing content

Open the file "demofile.txt" and append content to the file:
'''
with open("demofile.txt", "a") as f:
  f.write("Now the file has more content!")

#open and read the file after the appending:
with open("demofile.txt") as f:
  print(f.read())
  
  
'''
Overwrite Existing Content
To overwrite the existing content to the file, use the w parameter:

Example
Open the file "demofile.txt" and overwrite the content:
'''
with open("demofile.txt", "w") as f:
  f.write("Woops! I have deleted the content!")

#open and read the file after the overwriting:
with open("demofile.txt") as f:
  print(f.read())  
  
  
'''
Create a New File
To create a new file in Python, use the open() method, with one of the following parameters:

"x" - Create - will create a file, returns an error if the file exists

"a" - Append - will create a file if the specified file does not exists

"w" - Write - will create a file if the specified file does not exists

Example
Create a new file called "myfile.txt":
'''
f = open("myfile.txt", "x")  

'''
Delete a File
To delete a file, you must import the OS module, and run its os.remove() function:

ExampleGet your own Python Server
Remove the file "demofile.txt":
'''
import os
os.remove("demofile.txt")

'''
Check if File exist:
To avoid getting an error, you might want to check if the file exists before you try to delete it:

Example
Check if file exists, then delete it:
'''
import os
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")
  
'''
Delete Folder
To delete an entire folder, use the os.rmdir() method:
Note: You can only remove empty folders.
Example
Remove the folder "myfolder":
'''
import os
os.rmdir("myfolder")  