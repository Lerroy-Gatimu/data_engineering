'''
Python Inheritance
Inheritance allows us to define a class that inherits all the methods and properties from another class.
Parent class is the class being inherited from, also called base class.
Child class is the class that inherits from another class, also called derived class.

Create a Parent Class
Any class can be a parent class, so the syntax is the same as creating any other class:
'''
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
    
  def show (self):
    print (f"Name: {self.name},\nAge: {self.age}")  

p1 = Person ("Tony", 36)   
p1.show() 

'''
Create a Child Class
To create a class that inherits the functionality from another class, send the parent class as a parameter when creating the child class:
Example
Create a class named Student, which will inherit the properties and methods from the Person class:
'''

'''
When you add the __init__() function, the child class will no longer inherit the parent's __init__() function.

Note: The child's __init__() function overrides the inheritance of the parent's __init__() function.

To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function:
'''
class Student(Person):
  def __init__(self, grade, mark):
   Person.__init__(self, grade, mark) 
    

p2 = Student ("Sony", 70)
p2.show()

'''
Use the super() Function
Python also has a super() function that will make the child class inherit all the methods and properties from its parent:
'''
'''class Student(Person):
  def __init__(self, grade, mark, year):
    super().__init__(grade, mark)
    self.year = year
    self.grade = grade
    self.mark = mark
    
  def greeting(self):
    print (f"The class of {self.year} welcomes {self.name}. Steudent details:\nMark: {self.mark}\nGrade: {self.grade} ")  
    
x = Student("Mike", "Olsen", 2019,"A")
x.greeting()    '''

'''
Challenge: Inheritance
Test your understanding of Python inheritance by completing a small coding challenge.

Instructions
Inside the editor, complete the following steps:
Create a parent class Animal with an __init__ that takes name
Add a method speak that prints the name
Create a child class Dog that inherits from Animal
Create an object d1 = Dog("Rex")
Call d1.speak()
'''

class Animal:
  def __init__(self, name):
    self.dog_name = name
  
  def fname (self):
    print (f"My name is {self.dog_name}")
    
class Dog (Animal):
  pass    

d1 = Dog ("Rex")
d1.fname()      