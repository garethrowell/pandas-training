

# ----------------------------------------------------
# 2.3 Python language basics
# ----------------------------------------------------

# Language semantics
# ------------------


# Scalar types
# ------------

# Control flow
# ------------



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
 


# ----------------------------------------------------------
# 2.3 Python Language Basics  
# ----------------------------------------------------------


# Language Semantics
# ------------------

# Scalar Types
# ------------

# Control Flow
# ------------




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

b

# b now references [1, 2, 3]
# a new copy is NOT created 


a.append(4)

b

# When you pass objects as options to a function,
#  THE NEW LOCAL VARIABLES REFERENCE THE ORIGINAL OBJECTS
#  WITHOUT COPYING!!

def append_element(some_list, element):
    somelist.append(element)
    
data = [1, 2, 3]

append_element(data, 4)

data # [1, 2, 3, 4]



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

# don't care about type, but need to know about whether it has certain methods or behavior
# for example, does it implement the iterator protocol, _iter_ magic method

def isiterable(obj):
    try:
        iter(obj)
        return True
    except TypeError: # not interable
        return False
        
        
isiterable("a string")

isiterable([1, 2, 3])

isiterable(5)



# importing modules 
 
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


#  Binary operators

a + b

a - b

a * b

a / b

a // b  # a divided by b dropping fractional remainder

a ** b

a & b  # True if both are true

a | b # True if either a or b is True

a ^ b  # True if either a or b is True but not both

a == b

a != b

a < b, a <= b 

a > b, a >= b

a is b  # True if a and b reference the same object

a is not b  # True if a and b reference different objects

# is keyword

a = [1, 2, 3]

b = a

c = list(a) # list always creates a new Python list

a is b

a is not c

a == c #  not the same thing as 'a is c'

# Use 'is' and 'is not'to check for 'None'

a = None

a is None

# Mutable and immutable objects

# mutable objects include
    # lists
    # dictionaries
    # NumPy arrays
    # most user defined classes
    
a_list = ["foo", 2, [4,5]]

a_list[2] = (3, 4)

a_list

# immutable objects include strings and tuples




 
 
 
