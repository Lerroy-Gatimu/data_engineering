'''
Mixing Positional and Keyword Arguments
You can mix positional and keyword arguments in a function call.
However, positional arguments must come before keyword arguments.
'''

def car_details (make, model, age):
  print (f"I have a {make} {model}, {age} series")

car_details ("BMW", model="ZL8", age=2025)  

'''
Passing Different Data Types
You can send any data type as an argument to a function (string, number, list, dictionary, etc.)
The data type will be preserved inside the function:
'''

car_list = ["Ferrari", "Lambo", "Rover"]

def car_List (cars):
  for car in cars:
    print (car)
    
car_List (car_list)    


#Sending a dictionary as an argument:

user_details = {"Name":"Lerroy", "Age":25}

def user_Details (user):
  print ("Name:", user["Name"])
  print ("Age:", user["Age"])

user_Details (user_details)