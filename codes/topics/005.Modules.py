#learning basic modules
#print(help("modules")) #prints all available modules
#print(help("math"))    #prints all the available functions in said module
#ways to import modules
#import math
#import math as m
from math import pi as p #or can use just pi
import creating_module_005_v0_5 as custom
print(p)
print(custom.pi)
print(custom.square(2))