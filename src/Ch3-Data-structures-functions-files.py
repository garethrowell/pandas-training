

# ----------------------------------------------------------
# Ch 3 Data structures, functions and files  
# ----------------------------------------------------------

# ---------------------------------
# 3.1 Data structures and sequences
# ---------------------------------

# Tuple
# -----

# creating a tuple

tup = (4, 5, 6)

tup

# you can omit the parentheses

tup2 = 4, 5, 6

tup2

# convert an iterator or sequence to a tuple


tuple([4, 0, 2])

tup = tuple('string')

tup

# illustrating the zero index

tup[0]


# for more complex expressions, use parentheses

nested_tup = (4, 5, 6), (7, 8)

nested_tup

nested_tup[0]

nested_tup[1]

# immutable nature of tuples

tup = tuple(['foo', [1, 2], True])

tup[2]

tup[2] = False

# If object inside tuple is mutable, you can modify it in place

tup[1].append(3)

tup

# use the '+' sign to concatenate tuples

(4, None, 'foo') + (6, 0) + ('bar',)

# multiply tuple with integer - concatenating multiple copies
# note the objects aren't copied, just their references

('foo', 'bar') * 4


# Unpacking tuples ---------------------

tup = (4, 5, 6)

a, b, c = tup

b


# Unpacking sequencs of nested tuples

tup = 4, 5, (6, 7)

a, b, (c, d) = tup

d

# swapping variable names
# traditional

tmp = a

a = b

b = tmp

# Python approach

a, b = 1, 2 

a

b

b, a = a, b

a

b

# more tuple unpacking

seq = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]

for a, b, c in seq:
    print(f'a={a}, b={b}, c={c}')
    
    
# tuples are also a good way to return multiple values from a functions

# *rest can be used to capture arbitrarily long positional arguments, or to pull out
# individual arguments as follows

values = 1, 2, 3, 4, 5

a, b, *rest = values

a

b

rest

# alternate syntaz

a, b, *_ = values



# Tuple methods ---------------------

a = (1, 2, 2, 2, 3, 4, 2)

a.count(2)



# List
# ----

# are variable length and can be modified in-place

a_list = [2, 3, 7, None]

tup = ("foo", "bar", "baz")

b_list = list(tup)

b_list

b_list[1] = "peekaboo"

b_list

# Lists and tuples can be used interchangeably in many functions

# materializing an iterator or generator

gen = range(10)

gen

list(gen)

# adding and removing elements

b_list.append("dwarf")

b_list

b_list.insert(1, "red")

b_list

# insert is computationally expensive compared to append
# consider collections.deque

# using pop

b_list.pop(2)

b_list

# remove() takes off the first occurrence of the values

b_list.append("foo")

b_list

b_list.remove("foo")

b_list

# Using in keyword
# This is much slower than using dictionaries and sets

"dwarf" in b_list

"dwarf" not in b_list

# Concatenating and combining lists

[4, None, "foo"] + [7, 8, (2, 3)]

# using the extend keyword

x = [4, None,"foo"]

x.extend([7, 8, (2, 3)])

x

# Using extend is usually better than + concetenation
# + requires creating a copy

everything = []
for chunk in list_of_lists:
    everything.extend(chunk)
 
# is faster than

everything = []
for chunk in list_of_lists:
    everything = everyting + chunk
    
    
       
# Sorting ----------------------

# sorting in place (no copies)

a = [7, 2, 5, 1, 3]

a.sort()

a

# here we are passing a secondary sort key

b = ["saw", "small", "He", "foxes", "six"]

b.sort(key=len)

b

# Slicing ----------------------

seq = [7, 2, 3, 7, 5, 6, 0, 1]

seq[1:5]

seq[3:5] = [6, 3]

seq

# default start and stop indices


seq[:5]

seq[3:]

# negative indices

seq[-4:]

seq[-6: -2]

# a second colon to say every other element as follows

seq[::2]

seq[::-1] # this reverses the order!!








# Dictionary
# ----------

# aka hash maps or associative arrays

# key + value - both are objects

empty_dict = {}

d1 = {"a": "some value", "b": [1, 2, 3, 4]}

d1


# use the same syntax as lists or tubles

d1[7] = "an integer"

d1

# checking if a dictionary contains a key

"b" in d1

# delete a value using either del or pop

d1[5] = "some value"

d1["dummy"] = "another value"

d1


del d1[5]

d1

ret = d1.pop("dummy")

ret

d1

# list() keys and values method gives iterators for keys
# and values respectively

d1

list(d1.keys())

list(d1.values())

# iterating over both keys and values with items()
# gives 2 tuples

list(d1.items())

# merge one dictionary into another as well as
# updating in place

d1.update({"b": "foo", "c": 12})

# creating dictionaries from sequences
# when you want to pair up element-wise

# this is an alternative to dictionary comprehensions
# discussed later on - this is the general form

mapping = {}
for key, value in zip(key_list, value_list):
    mapping[key] = value
    
# zip defined later on
# dictionaries are essentially collections of 2-tuples

tuples = zip(range(5), reversed(range(5)))

tuples

mapping = dict(tuples)

mapping

# Default values

# common to see the following

if key in some_dict:
    value = some_dict[key]
else:
    value = default_value

# this allows get and pop to take default values

value = some_dict.get(key, default_value)

# get by default returns None while
# pop will raise an exception

# values in a dictionary may come from another collection
# like a list
# here, we categorize words by their first letter

words = ["apple", "bat", "bar", "atom", "book"]

by_letter = {}

<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<












# Set
# ---

# Built-in Sequence Functions
# ---------------------------

# List, set and dictionary comprehensions
# ---------------------------------------


# -------------
# 3.2 Functions
# -------------


# Namespaces, scope and local functions
# -------------------------------------

# Returning multiple values
# ---------------------------

# Functions are objects
# ---------------------

# Anonymous (Lambda) Funtions
# ---------------------------

# Generators
# ----------

# Errors and exception handling
# -----------------------------


# ----------------------------------
# 3.3 Files and the operating system
# ----------------------------------

# Bytes and unicode with files




