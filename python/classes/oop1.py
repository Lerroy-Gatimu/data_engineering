'''
Classes are like blueprints. The objects follow the blueprint.
For instance, a car is the class, a Toyota is the object.
'''

'''
All classes have a built-in method called __init__(), which is always executed when the class is being initiated.
The __init__() method is used to assign values to object properties, or to perform operations that are necessary when the object is being created.
Without the __init__() method, you would need to set properties manually for each object:
'''
class person:
  def __init__ (self, name, age):
    self.name = name
    self.age = age
    
p1 = person ("Lerroy", 25)    
p2 = person ("Satoshi", 100)

print (p1.name, p2.age)

'''
Instructions
Inside the editor, complete the following steps:
Create a class called Dog
Add an __init__ method with parameters name and age, and store them as properties using self
Add a method called bark that prints the dog's name followed by " says Woof!"
Create an object d1 of the Dog class with name "Buddy" and age 3
Call the bark method on d1
'''
class Dog:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def bark (self):
    print (f"{self.name} says WOOF!")

d1 = Dog ("Bosco",3)    
d1.bark()