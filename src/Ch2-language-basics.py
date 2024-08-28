


# ----------------------------------------------------------
# 2.3 Python Language Basics  
# ----------------------------------------------------------




# Language Semantics
# ----------------------------------------------------------


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


a_tuple = (3, 5, (4, 5))

a_tuple[1] = "four" # throws a type error


# Scalar types
# ----------------------------------------------------------

# None, str, bytes, float, bool, int, 

# Numeric types

# int

ival = 17239871

ival

ival ** 6

# float

fval = 7.243

fval

fval2 = 6.78e-5

fval2


# int division

3 / 2

3 // 2

# strings

a = 'one way of writing a string'
a

b = "another way"
b

# multiline string

c = """
This is a longer string that
spans multiple lines
"""
c

# how many lines text

c.count("\n")


# Strings are immmutable

a = "this is a string"

a[10] = "f"

# instead, you need to create a new string

b = a.replace("string", "longer string")

b

# cast to string using str()

a = 5.6

s = str(a)

print(s)

# Strings as sequences

s = "python"

list(s)

s[:3]


# \ as escape character

s = "12\\34"

print(s)


# use raw strings, r, to when interpreting slashes as is

s = r"this\as\no\special\characters"

s


# adding two strings concatencates them

a = "this is the first half"

b = " and this is the second half"

a + b


# using the string format method

template = "{0:.2f} {1:s} are worth US${2:d}"

template.format(88.46, " Argentine Pesos", 1)


# using Python 3.6 f-strings

amount = 10

rate = 88.46

currency = "Pesos"

result = f"{amount} {currency} is worth US${amount / rate}"

result

# including format specifiers

f"{amount} {currency} is worth US${amount / rate:.2f}"


# Bytes and unicode

# UTF-8

val = "español"

val

val_uts8 = val.encode("utf-8")

val_uts8

type(val_uts8)

val_uts8.decode("utf-8")


# Other coding systems

val.encode("latin")

val.encode("utf-16")


# Booleans

True and True

False and True

# Converting to integer

int(False)

int(True)

# using not with Boolean values

a = True

b = False

not a

not b

# Type casting ----

s = "3.14159"

type(s)

fval = float(s)

type(fval)

int(fval)

bool(fval)

bool(0)


# None ------

a = None

a is None

b = 5

b is not None

True

# None and function arguments

def add_and_maybe_multiple(a, b, c=None):
    result = a + b
    
    if c is not None:
        result = result * c
        
    return result
    
    
# datetime, date, time types

from datetime import datetime, date, time

dt = datetime(2011, 10, 29, 20, 30, 21)

dt.day

dt.date()

dt.time()

dt.strftime("%Y-%m-%d %H:%M")

datetime.strptime("20091021", "%Y%m%d")

# see Table 11-2 for full list of format specifications

dt_hour = dt.replace(minute=0, second=0)

dt_hour

dt

dt2 = datetime(2011, 11, 15, 22, 30)

delta = dt2 - dt

delta

dt

dt + delta



# Contol flow
# ----------------------------------------------------------


# if, elif, and else

x = -5

if x < 0:
    print("Its negative")


if x < 0:
    print("It's negative")
elif x == 0:
    print("Equal to zero")
elif 0 < x < 5:
    print("Positive but smaller than 5")
else:
    print("Positive and large than or equal to 5")
    
   
# Chaining comparisons

4 > 3 > 2 > 1


# for loops

for value in collection:
    
sequence = [1, 2, None, 4, None, 5]
total = 0

# using continue

for value in sequence:
    if value is None:
        continue
    total += value
    print("total = ", total)
    
    
# using break
























































