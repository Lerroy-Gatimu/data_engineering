'''
Keyword Arguments
You can send arguments with the key = value syntax.
with keyword arguments, the order of the arguments does not matter.
'''

def car_name (name, make):
  print (f"My car is a {name}, a {make} to be precise. I love {name}'s for their masculine look.")

car_name (name="BMW",make="ZL8")  

# When you call a function with arguments without using keywords, they are called positional arguments.
# Positional arguments must be in the correct order
def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function("Buddy", "dog")