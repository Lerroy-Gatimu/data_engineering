'''
Information can be passed into functions as arguments.
Arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want, just separate them with a comma.

Parameters vs Arguments
The terms parameter and argument can be used for the same thing: information that are passed into a function.
From a function's perspective:
A parameter is the variable listed inside the parentheses in the function definition.
An argument is the actual value that is sent to the function when it is called.
'''

def my_function (first_name): #first_name is an argument
  return print (f'My first name is {first_name}')

my_function ('Lerroy') #Lerroy is a parameter

'''
Number of Arguments
By default, a function must be called with the correct number of arguments.
If your function expects 2 arguments, you must call it with exactly 2 arguments.
'''

def full_name (first,second):
  print (f'My full name is {first} {second}')

full_name ("Lerroy","Gatimu")  


'''
Default Parameter Values
You can assign default values to parameters. If the function is called without an argument, it uses the default value
'''

def default_parameter (name = "Lerroy"):
  print (f"My name is {name}")

default_parameter ()
default_parameter ("Gatimu")

