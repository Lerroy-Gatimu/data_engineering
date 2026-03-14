'''
Naming Variables
If you operate with the same variable name inside and outside of a function, Python will treat them as two separate variables, one available in the global scope (outside the function) and one available in the local scope (inside the function)
'''

x = 300

def myfunc():
  x = 200
  print(x)

myfunc()

print(x)

'''
Global Keyword
If you need to create a global variable, but are stuck in the local scope, you can use the global keyword.
The global keyword makes the variable global.
'''
def myfunc():
  global x
  x = 3

myfunc()

print(x)

#Also, use the global keyword if you want to make a change to a global variable inside a function.
x = 50

def myfunc():
  global x
  x = 20
  print(x)
  
myfunc()  
  

'''
Nonlocal Keyword
The nonlocal keyword is used to work with variables inside nested functions.
The nonlocal keyword makes the variable belong to the outer function.
'''

def func1():
  x = 20
  
  def func2():
    nonlocal x
    x=30
  func2()  
  return x
  
print(func1())
    
'''    
The LEGB Rule
Python follows the LEGB rule when looking up variable names, and searches for them in this order:
Local - Inside the current function
Enclosing - Inside enclosing functions (from inner to outer)
Global - At the top level of the module
Built-in - In Python's built-in namespace
'''
x = "global"

def outer():
  x = "enclosing"
  def inner():
    x = "local"
    print("Inner:", x)
  inner()
  print("Outer:", x)

outer()
print("Global:", x)