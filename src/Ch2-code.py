

# 2.2 IPython Basics ---------------------------------------------------

import numpy as np

data = [np.random.standard_normal() for i in range(7)]

data




 b = [1, 2, 3]
 b?
 print?
 
 #  object introspection 
    
 
 
 def add_numbers(a, b):
     

    """
    Add two numbers together

    Returns
    -------
    the_sum : type of arguments
    """
    return a + b        
 

# Python Language Basics  
----------------------------------------------------------


# use of colons and indentation (use 4 spaces, not tabs)

for x in array:
    if x < pivot:
        less.append(x)
    else:
        greater.append(x)   
    

# Using comments to block out some code

results = []
for line in file_handle:
    # keep the empty lines for now
    # if len(line) == 0:
    #   continue
    results.append(line.replace("foo", "bar"))
    
    
# Combining comments with code

    
   print("Reached this line")  # Simple status report 
    

# function calls with zero or more arguments

result = f(x, y, z)
g()


# syntax for an object calling a method

obj.some_method(x, y, z)

# positional and keyword arguments

result = f(a, b, c, d=5, e="foo")


    
# variable assignment is by reference


a = [1, 2, 3]

b = a

# b now references [1, 2, 3]
# a new copy is NOT created 

# Variables are names for objects within a particular namespace
# the type information is stored in the object itself
# So variables don't have inherent types

a = 5

type(a) # here its int

a = "foo"

type(a) # here its str


# In Python, implicit casts are not allowed

"5" + 5 # throws a type error

# every object has a specific type (or class), and implicit 
# conversions will occur only in certain permitted circumstances
# such as:
    
a = 4.5

b = 2

a / b # yields the float 2.25


# checking that an object is an instance of a particular type

 a = 5
 
 isinstance(a, int) # yields True


# isinstance can accept a tuple of types

a = 5; b = 4.5

isinstance(a, (int, float)) # True

isinstance(b, (int, float)) # True


# objects have attributes and methods

a = "foo"

a.<Press Tab>

# attributes and methods via the getattr function:

getattr(a, "split")


# duck typing 










def append_element(some_list, element):
  some_list.append(element)  
    
    
 data = [1, 2, 3]
 
 append_element(data, 4)

data


# dynamic references, strong types ------------------------

a = 5

type(a)


a = "foo"

type(a)

# strong types

a = 4.5

b = 2

print(f"a is {type(a)}, b is {type(b)}")

a/b   #<<<<<<<<< implicit conversion to float


# importing modules ------------------------

# some_module.py
PI = 3.14159

def f(x):
    return x + 2

def g(a, b):
    return a + b
    
import some_module
result = some_module.f(5)
pi = some_module.PI


import some_module as sm
from some_module import PI as pi, g as gf

r1 = sm.f(pi)
r2 = gf(6, pi)



# templates and format() -----------------


template = "{0:.2f} {1:s} are worth US${2:d}"

template.format(88.46, "Argentine Pesos", 1)


# f-strings ----------------

amount = 10

rate = 88.46

currency = "Pesos"

f"{amount} {currency} is worth US${amount / rate}"



# Booleans -------------------

True and True

False or True

int(False)

int(True)

a = True
 
b = False
 
not a
 
not b
 

#   Dates and times ------------------------
 
 
 
 
 
