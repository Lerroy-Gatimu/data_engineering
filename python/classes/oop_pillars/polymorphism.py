'''
The word "polymorphism" means "many forms", and in programming it refers to methods/functions/operators with the same name that can be executed on many objects or classes.

Function Polymorphism
An example of a Python function that can be used on different objects is the len() function.
'''

'''
Class Polymorphism
Polymorphism is often used in Class methods, where we can have multiple classes with the same method name.

For example, say we have three classes: Car, Boat, and Plane, and they all have a method called move():

Example
Different classes with the same method:'''

class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Drive!")

class Boat:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Sail!")

class Plane:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang")       #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747")     #Create a Plane object

for x in (car1, boat1, plane1):
  x.move()
  
  
'''Inheritance Class Polymorphism
What about classes with child classes with the same name? Can we use polymorphism there?

Yes. If we use the example above and make a parent class called Vehicle, and make Car, Boat, Plane child classes of Vehicle, the child classes inherits the Vehicle methods, but can override them:

Example
Create a class called Vehicle and make Car, Boat, Plane child classes of Vehicle:
'''
class Vehicle:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Move!")

class Car(Vehicle):
  pass

class Boat(Vehicle):
  def move(self):
    print("Sail!")

class Plane(Vehicle):
  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang")       #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747")     #Create a Plane object

for x in (car1, boat1, plane1):
  print(x.brand)
  print(x.model)
  x.move()
  
  
'''
Challenge: Polymorphism
Test your understanding of Python polymorphism by completing a small coding challenge.

Instructions
Inside the editor, complete the following steps:
Create a class Cat with a method sound that prints "Meow"
Create a class Fox with a method sound that prints "Wa-pa-pa-pa-pa-pow!"
Create objects c1 = Cat() and f1 = Fox()
Call sound() on both objects
'''  

class Cat:
  def __init__ (self, sound):
    self.sound = sound
  def make_sound (self):
    print (f"{self.sound}")

class Fox:
  def __init__ (self, sound):
    self.sound = sound
  def make_sound (self):
    print (f"{self.sound}")
            
c1 = Cat("Meow") 
f1 = Fox("Wapaaa")           

for animal in (c1, f1):
  animal.make_sound()