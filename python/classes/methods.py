'''
Class Methods
Methods are functions that belong to a class. They define the behavior of objects created from the class.
All methods must have "self" as the first parameter.
'''

class Calculator:
  def add(self, a, b):
    return a + b

  def multiply(self, a, b):
    return a * b

calc = Calculator()
print(calc.add(5, 3))
print(calc.multiply(4, 7))

'''The __str__() Method
The __str__() method is a special method that controls what is returned when the object is printed:

Example
Without the __str__() method:'''

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Emil", 36)
print(p1)

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name} ({self.age})"

p1 = Person("Tobias", 36)
print(p1)