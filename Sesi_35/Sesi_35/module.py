import sys
##Add path to sys

from Path import Person 
from Path.Person import display, name

##With default import
print("\n\n> With default import")
print(Person.name)
print(Person.devices)
Person.display('Good Morning !')

##Alternate individual object
print("\n\n> Alternate individual object")
print(name)
display('Good Morning !')

##Import with alternative name
print("\n\n> Import with alternative name")
from Path2.Person2 import display2 as new_display, name as new_name
print(new_name)
new_display('Good Morning2 !')

##Dir function
print("\n\n> Dir Function")
print(dir(new_name))

##Executing a Module as a Script
## execute in cmd command inside directory "python Person.py"

##Reload module
print("\n\n> Reload Module")
import car
import importlib

print(car.brands)
importlib.reload(car)
print(car.brands)

##Python Packages
print("\n\n> Python Package")
import pkg.mod1, pkg.mod2
print(pkg.mod1.kitchen_sets)
print(pkg.mod2.artist_kits)

##Package using individual object
print("\n> Package using individual object")
from pkg.mod1 import kitchen_sets
print(kitchen_sets)
##Package using alt name
print("\n> Package using alt name")
from pkg.mod1 import kitchen_sets as ks
print(ks)