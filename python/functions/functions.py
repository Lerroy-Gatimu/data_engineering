'''
A function name must start with a letter or underscore
A function name can only contain letters, numbers, and underscores
Function names are case-sensitive (myFunction and myfunction are different)
'''

def farenheit_to_celsius (farenheit):
  return (farenheit - 32) * 5/9

print (farenheit_to_celsius (100))

# If a function doesn't have a return statement, it returns None by default.
def empty_function ():
  return
print (empty_function())  

'''
The pass Statement
Function definitions cannot be empty. If you need to create a function placeholder without any code, use the pass statement
The pass statement is often used when developing, allowing you to define the structure first and implement details later.
'''

def my_function():
  pass

