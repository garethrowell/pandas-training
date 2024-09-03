

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

a, b = 1, 2 <<<<<<<<<<<<<<<<<








# List
# ----


# Dictionary
# ----------


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




