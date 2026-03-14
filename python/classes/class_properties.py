'''
Class Properties vs Object Properties
Properties defined inside __init__() belong to each object (instance properties).
Properties defined outside methods belong to the class itself (class properties) and are shared by all objects:
'''

class Person:
  species = "Human" # Class property

  def __init__(self, name):
    self.name = name # Instance property

p1 = Person("Emil")
p2 = Person("Tobias")

print(p1.name)
print(p2.name)
print(p1.species)
print(p2.species)

'''
Add New Properties
You can add new properties to existing objects:
'''

class Car:
  vehicle = "car"
  
  def __init__(self, brand):
    self.brand = brand 
    
  def show (self):
    print (f'{self.brand}')

c1 = Car ("BMW")
c1.show()

c1.year = 2025
c1.mileage = 300  

print (c1.year, c1.mileage)