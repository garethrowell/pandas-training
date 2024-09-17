

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

for word in words:
    letter = word[0]
    if letter not in by_letter:
        by_letter[letter] = [word]
    else:
        by_letter[letter].append(word)
        
by_letter

# setdefault method to simplify

by_letter = {}

for word in words:
    letter = words[0]
    by_letter.setdefault(letter, []).append(word)
    
by_letter

# built-in collections module has class defaultdict 
# makes even easier
# pass type or functions

from collections import defaultdict

by_letter = defaultdict(list)

for word in words:
    by_letter[word[0]].append(word)
    
by_letter

# Valid dictionary key types

# keys are generally immutable scalars or tuples
# "hashability" - determine with has function

hash("string")

hash((1, 2, (2, 3)))

hash((1,2, [2, 3]))

# To use a list as a key, convert to tuple

d = {}

d[tuple([1, 2, 3])] = 5

d1

hash(tuple([1, 2, 3]))


# Set
# ---

# set is unordered collection of unique elements
# create a set using set function or set literal {}

set([2, 3, 3, 1, 3, 3])

{2, 2, 2, 1, 3, 3}

# set operations - union, intersection, difference, symmetric_difference

a = {1, 2, 3, 4, 5}

b = {3, 4, 5, 6, 7, 8}

# using union or the binary operator |

a.union(b)

a | b

# intersection with intersection() or & operator

a.intersection(b)

a & b

# other set operators

c = a.copy()

c

c |= b # update

c

d = a.copy()
 
d

d &= b # intersection

d

# set elements are immutable and must be hashable
# you can convert them to tuples first

my_data = [1, 2, 3, 4]

my_data

my_set = {tuple(my_data)}

my_set

a_set = {1, 2, 3, 4, 5}

a_set

# is a subset of
{1, 2, 3}.issubset(a_set)

# contains all the elements of
a_set.issuperset({1, 2, 3})

# true if and only if contents are equal
{1, 2, 3} == {1, 3, 2}



# Built-in Sequence Functions
# ---------------------------
# use these at every opportunity

# enumerate

# keeping track of index of current item

index = 0
for value in collection:
    # do something
    index += 1
    
 # this is so common that there is specific function 
 
 for index, value in enumerate(collection):
     # do something
     
# sorted
# returns new sorted list from elements of any sequence

sorted([7, 1, 2, 6, 0, 3, 2])

sorted("horse race")

# zip
# pairs up elements of list, tuples, or other sequences 
# into list of tuples

seq1 = ["foo", "bar", "baz"]
seq2 = ["one","two", "three"]

zipped = zip(seq1, seq2)

list(zipped)

# zip creates shortest sequence of arbitrary number of sequences

seq3 = [False, True]

list(zip(seq1, seq2, seq3))

# combine zip with enumerate to interate of multiple sequences

for index, (a, b) in enumerate(zip(seq1, seq2)):
    print(f"{index}: {a}, {b}")
    
# reversed is a generator

list(reversed(range(10)))
 

# List, set and dictionary comprehensions
# ---------------------------------------

[expr for value in collection if condition]

# meaning...

result = []

for value in collecteion:
    if condition:
        result.append(expr)
        
 
# for example
 
strings = ["a", "as", "bat", "car", "dove", "python"]
 
# set and dictionary comprehensions

dict_comp = {key-exp: value-expr for value in collection if condition}

set_comp = {expr for value in collection if condition}

 # using set to find the unique length in strings
 
unique_lengths = {len(x) for x in strings}
 
unique_lengths
 
 # a dictionary comprehensions example
 
 loc_mapping = {value: index for index, value in enumerate(strings)}
 
 loc_mapping
 
 # nested list comprehensions
 
 # list of lists with names
 
 all_data = [["John","Emily","Michael", "Mary", "Steven"],
             ["Maria","Juan","Javier","Marta","Pilar"]]
             
 all_data
 
 # list all the names with two or more 'a's in them
 
names_of_interest = []
 
for names in all_data:
    enough_as = [name for name in names if name.count("a") >= 2]
    names_of_interest.extend(enough_as)
    
names_of_interest

# nested list comprehensions, example with tuples

some_tuples = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]

some_tuples

flattened = [x for tup in some_tuples for x in tup]

flattened

# the order of the for loops looks like this

flattened = []

for tup in some_tuples:
    for x in tup:
        flattened.append(x)
        
# probably shouldn't go further than two loops
 
# this is different from above - a list comprehension inside 
# another list comprehension

[[x for x in tup] for tup in some_tuples]

# vs

[x for tup in some_tuples for x in tup]



# -------------
# 3.2 Functions
# -------------

# your basic function

def my_function(x, y):
    return x + y
    
    
my_function(1, 2)

result = my_function(1, 2)

result

# multiple returns are okay
# None is returned if no return reached

def function_without_return(x):
    print(x)
    
result = function_without_return("hello!")

result

print(result)

print(function_without_return("hello!"))

# functions can have positional arguments
# functions can also have keyword arguments as defaults 
#    or optional arguments

# below, z is an optional argument with a default value of 1.5

def my_function2(x, y, z=1.5):
    if z > 1:
        print("z > 1")
        return z * (x + y)
    else:
        print("else")
        return z / (x + y)
        
# The keyword is optional, but the positional
# are required
# the keyword must follow the positional 

my_function2(5, 6, z=0.7)

my_function2(3.14, 7, 3.5)

my_function2(10, 20)   


# Namespaces, scope and local functions
# -------------------------------------

# Functions can access local variables
# *and* outside the functions including global
# variables

# namespace = variable scope

# function's arguments have local namespace
# local namespace is destroyed when the function 
# is finished

def func(): # function is called
    a = []  # empty list a is created
    for i in range(5):
        a.append(i) # five elements are appended
        print(a)
print(a)
# a is destroyed when function is ended

# here we define list a before the function
# and every call to func() will modify list a
a = []

def func():
    for i in range(5):
        a.append(i)
        print(a)
             
print(a)


# using global and nonlocal
# use globals to store some kind of state in a system
# generally not good practice

a = None

def bind_a_variable():
    global a
    a = []
    
bind_a_variable()

print(a)
    
# Returning multiple values
# ---------------------------

def f():
    a = 5
    b = 6
    c = 7
    return a, b, c 
 
f()

# This is really cool...

a, b, c = f()

a

b

c


# Functions are objects
# ---------------------

# This facilitates many constructs

# Some messy data

states = ["   Alabama", "Georgia!", "Georgia", "georgia", \
"FlOrIda", "south   carolina##", "West virginia?"]


# importing regex module

import re

# using regex expressions

def clean_strings(strings):
    result = []
    for value in strings:
        value = value.strip()
        value = re.sub("[!#?]", "", value)
        value = value.title()
        result.append(value)
    return result

clean_strings(states)

# Alternatively, make a list of desired operations
# This "functional pattern" allows for easy modification
# clean_strings is more generic


def remove_punctuation(value):
    return re.sub("[!#?]", "", value)

clean_ops = [str.strip, remove_punctuation, str.title]

def clean_strings(strings, ops):
    result = []
    for value in strings:
        for func in ops:
            value= func(value)
        result.append(value)
    return result
    
clean_strings(states, clean_ops)


# Anonymous (Lambda) Funtions
# ---------------------------

# consist of single statement 
# resulting in a returned value

# very helpful for data analysis
# where functions are used as arguments

def short_function(x):
    return x * 2

equiv_anon = lambda x: x * 2

# another example

def apply_to_list(some_list, f):
    return[f(x) for x in some_list]
    
ints = [4, 0, 1, 5, 6]

apply_to_list(ints, lambda x:x * 2)

    
# an example using sort and string length 
# to sort collection of strings by their
# distict letters

strings = ["foo", "card", "bar", "aaaa", "abab"]


strings.sort(key = lambda x:len(set(x)))

strings

# Generators
# ----------

# an iterator protocol
# generic way to make objects iterable
# create a generator with the key word yield

some_dict = {"a": 1, "b": 2, "c": 3}

for key in some_dict:
    print(key)
   
    
dict_iterator = iter(some_dict)
dict_iterator

list(dict_iterator)

# To create a generator, use the "yield" keyword

def squares(n=10):
    print("Generating squares from 1 to {n ** 2}")
    for i in range(1, n + 1):
     yield i ** 2
     
# when you call the generator, no code is immediately executed
# its not until you request the elements
     
gen = squares()

gen
 
for x in gen:
    print(x,end = " ")
     
     
# generator expressions
# analog to list, dict and set comprehensions

gen = (x ** 2 for  x in range(100))

gen

# This is equivalent to 

def _make_gen():
    for x in range(100):
        yield x ** 2
gen2 = _make_gen()

gen2

# using a generator instead of list comprehension
# as a function argument

sum(x ** 2 for  x in range(100))

dict((i , i** 2) for i in range(5))

# generators can sometimes be faster than comprehension expressions


# itertools module
# collection of iterators for various data algorithms

# example - groupby takes any sequence and function
#    grouping consecutive elements in sequence by 
#    return value of function

import itertools

def first_letter(x):
    return x[0]
    
names = ["Alan", "Adam", "Wes", "Will", "Albert", "Steven"]

for letter, names in itertools.groupby(names, first_letter):
    print(letter, list(names)) # names in a generator


# Errors and exception handling
# -----------------------------

# Example of code throwing exception

num = float("1.2345")

num

float("something") # this cast won't work

# to catch this exception

def attempt_float(x):
    try:
        return float(x)
    except:
        return x
        
float((1,2)) # also raises exception

attempt_float("1.2345")

attempt_float("something")

# To just capture value error

def attempt_float(x):
    try:
        return float(x)
    except ValueError:
        return x
        
        
attempt_float((1, 2)) # throws exception

# catch multiple types of exceptions 

def attempt_float(x):
    try:
        return float(x)
    except (TypeError, ValueError):
        return x
        
attempt_float((1, 2))

# To execute - whether or not try succeeds
# use finally
# here, file f will always get closed

f = open(path, mode="w")

try:
    write_to_file(f)
finally:
    f.close()
    
    
 
 
        
        



















# ----------------------------------
# 3.3 Files and the operating system
# ----------------------------------

# Bytes and unicode with files




