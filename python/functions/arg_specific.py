'''
Positional-Only Arguments
You can specify that a function can have ONLY positional arguments.
To specify positional-only arguments, add , / after the arguments:
'''

def pos_only (car, year, /):
  print (f"My {car} is a {year} version.")

pos_only ("BMW", "2025")  

'''
Keyword-Only Arguments
To specify that a function can have only keyword arguments, add *, before the arguments:
'''

def key_only (*, car, year):
  print (f"My {car} is a {year} version")
  
key_only (car="BMW", year=2025)    