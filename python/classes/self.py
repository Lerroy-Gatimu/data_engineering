'''
The self Parameter
The self parameter is a reference to the current instance of the class.
It is used to access properties and methods that belong to the class.
'''

class person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
    
  def greet (self):
    print (f'Hello {self.name}')
    
p1 = person ("Lee", 22)
p1.greet()      

'''
self Does Not Have to Be Named "self"
It does not have to be named self, you can call it whatever you like, but it has to be the first parameter of any method in the class
'''
class Person:
  def __init__ (pp, name, age):
    pp.name = name
    pp.age = age
  
  def greet (abc):
    print (f"Hello, my name is {abc.name}")      
    
p1 = Person ("Lerroyyy", 23)    
p1.greet()

'''
Instructions
Inside the editor, complete the following steps:
Create a class called Car
Add an __init__ method with a brand parameter, and store it as a property
Add a method called show that prints the brand
Create an object c1 of the Car class with brand "Ford"
Call the show method on c1
'''

class Car:
  def __init__(self, brand, year):
    self.brand = brand
    self.year = year
  
  def show (self):
    print (f'This car is a {self.brand}')  
    
c1 = Car ('Ford', 2025)    
c1.show()

# You can modify the value of properties on objects:
c1.year = 2028
print (c1.year)

#You can delete properties from objects using the del keyword:
del c1.year
print (c1.year)