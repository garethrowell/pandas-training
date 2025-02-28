
# ----------------------------------------------------
# Ch 4 Numpy basics: arrays and vectorized computation
# ----------------------------------------------------

import numpy as np

data = np.array([[1.5, -0.1, 3], [0, -3, 6.5]])

data

data * 10



data + data


# -----------------------------------------------------
# 4.1 The Numpy ndarray: A multidomesional array object
# -----------------------------------------------------

# ndarray shape and data type

data.shape

data.dtype


# Creating ndarrays
# -----------------

# array() accepts any sequence-like object including other arrays

data1 = [6, 7.5, 8, 0, 1]

arr1 = np.array(data1)

arr1

# nested sequences create multi-dimensional arrays

data2 = [[1, 2, 3, 4], [5, 6, 7, 8]]

arr2 = np.array(data1)

arr2

# ndim and shape attributes

arr2.ndim

arr2.shape

# inferring data types

arr1.dtype

arr2.dtype

# other functions for creating arrays

np.zeros(10)

np.zeros((3, 6))

# below, not safe to assume return 0's

np.empty((2, 3, 2))

# range function

np.arange(15)

# default data type for these functions in float64

# array creation functions: 
# array, asarray, arange, ones, ones_like,
# empty, empty_like, full, full_like,
# eye, identity


# Data types for ndarrays
# -----------------------

# dtype is metadata

arr1 = np.array([1, 2, 3], dtype=np.float64)

arr2 = np.array([1, 2, 3], dtype=np.int32)

arr1.dtype

arr2.dtype


# NumPy data types
# int8, uint8, int16, utin16, int32, uint32, int64, uint64, 
# float16, float32, float64, float128, comnplext64, copmlex128,
# complex256, bool, object, string, unicode

arr = np.array([1, 2, 3, 4, 5])

arr.dtype

arr

float_arr = arr.astype(np.float64)

float_arr

float_arr.dtype

# example of truncating with float to int

arr = np.array([3.7, -1.2, -2.6, 0.5, 12.9, 10.1])

arr

arr.astype(np.int32)

# converting strings to numerics
# caution: _string type is fixed size and may trucate input

numeric_strings = np.array(["1.25", "-9.6", "42"], dtype=np.string_)

numeric_strings.astype(float)

# using another array's dtype

int_array = np.arange(10)

int_array

calibers = np.array([.22, 270, .357, .44, 50], dtype= np.float64)

int_array.astype(calibers.dtype)

# using short hand type code strings

zeros_uint32 = np.zeros(8, dtype="u4")

zeros_uint32

# Note: astype *always* creates a new copy


# Arithmetic with NubPy arrays
# ----------------------------

# vectorization via batch operations

arr = np.array([[1., 2., 3.,], [4., 5., 6.,]])

arr

arr * arr

arr - arr

# operations using scalars

1 / arr


arr ** 2

# Comparisons > or < yield booleans


arr2 = np.array([[0., 4., 1.,], [7., 2., 12.,]])

arr2 > arr

# Broadcasting - operations between differently
# sized arrays

# Basic indexing and slicing
# --------------------------

# Indexing on one dimensional arrays is similar to 
# slicing lists

arr = np.arange(10)

arr

arr[5]

arr[5:8]

arr[5:8] = 12 # here, we are broadcasting 12s in arr

arr


### array slices are VIEWS of the original source arrays - see below
### things tend to work on the original arrays rather than copies

arr_slice = arr[5:8]

arr_slice

# Note this step

arr_slice[1] = 12345

arr


arr_slice[:] = 64 # this is called a "bare" slice

arr

### Note, if you want to work on copies, then create them

arr[5:8].copy()

# in two dimensional arrays and higher, indexes are one-dimensional arrays

arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

arr2d

arr2d[2]

# consequently, elements can be accessed recursively
# or alternatively, you can use csv list of indices. E.g., 

arr2d[0][2]

arr2d[0, 2]

# Think of axis 0 as rows and axis 1 as columns

# In multi-dimensional arrays, omitting later indices, uses earlier indices

arr3d = np.array([[[1, 2, 3],[4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

arr3d

arr3d[0]

# Assigning scalars and arrays to arr3d[0]

old_values = arr3d[0].copy()

arr3d[0] = 42

arr3d

arr3d[0] = old_values

arr3d

##

arr3d[1, 0] # gives all values with indices start with (1, 0)

# This is the same as the following individual steps

x = arr3d[1]

x

x[0]

# all of these operations return VIEWS
# multi-dimensional indexing syntax from NumPy
# does not work in regular Python, e.g., lists-of-lists

# Indexing with slices
# --------------------

# one-dimensional slicing is similar to lists

arr

arr[1:6]

# two dimensional slicing is a bit different

arr2d

arr2d[:2] # slices along the 0 axis, 
          # slices along the first two rows of arr2d
          
# passing multiple slices

arr2d[:2, 1:]

# mixing indices and slice to get lower dimensions
# here, we select second row but only 1st two columns

lower_dim_slice = arr2d[1, :2]

lower_dim_slice

lower_dim_slice.shape

# more subsample slicing

arr2d[:2, 2]

# the colon by itself means take the entire axis

arr2d[:, :1]

arr2d

arr2d[:2, 1:]


arr2d[:2, 1:] = 0

arr2d



# Boolean indexing
# ----------------


names = np.array(["Bob", "Joe", "Will", "Bob", "Will", "Joe", "Joe"])

data = np.array([[4, 7], [0, 2], [-5, 6], [0, 0], [1, 2], [-12, -4], [3, 4]])

names

data 

names == "Bob"

# using a Boolean array for indexing
# it has to have the same length as the axis its indexing

data[names == "Bob"]

# more complex

data[names == "Bob", 1:]


data[names == "Bob", 1]


# selecting everything but Bob either != or ~

names

names != "Bob"

~(names == "Bob")

# using as an index

data

data[~(names == "Bob")]

# ~ use to invert Boolean array

cond = names == "Bob"

cond

~cond

data[~cond]

# combining multiple Boolean conditions

names

data

mask = (names == "Bob") | (names == "Will") # 'and' and 'or' don't work, use '&' and '|'

mask

data[mask]

# NOTE - selecting data with Boolean index and assigning to new variable
# ALWAYS creates a copy of data, even if unchanged


# 
data[data < 0]  # returns values that meet the condition

# then to assign those values to 0
data[data < 0]  = 0

data

# here setting entire rows or columns 
# to a value using one-dimensional array

data[names != "Joe"] = 7

data


# Fancy indexing
# --------------

# ALWAYS generates copy when assigning to a new variable


# indexing using integer arrays

arr = np.zeros((8, 4))

arr

for i in range(8):
    arr[i] = i

arr

# To select subset of rows in particular order

arr[[4, 3, 0, 6]]

# Selecting from the end

arr[[ -3, -5, -7]]

# More complex...
# Passing multiple index arrays does something different...
# It selects a one-dimensional array of elements
# corresponding to each tuple of indices

arr = np.arange(32).reshape((8, 4))

arr

# here, the elements (1, 0), (5, 3), (7, 1) and (2, 2)
arr[[1, 5, 7, 2], [0, 3, 1, 2]]

# in general, same number of arrays as there are axes -> one-dimensional

# Selecting a rectangular region of a matrix - this is not intuitive!!

arr

arr[[1, 4, 7]][:, [0, 3, 1, 2]]

# modifying index vaules with fancy indexing

arr

arr[[1, 5, 7, 2], [0, 3, 1, 2]]

arr[[1, 5, 7, 2], [0, 3, 1, 2]] = 0

arr


# Transposing arrays and Swapping Axes
# ------------------------------------

# Transposing an array is flipping it along its diagonal axis
# This is helpful for computer graphics and also for solving
# linear systems of equations. 

arr = np.arange(15).reshape((3, 5))

arr

arr.T

# Application: Computing the inner matric using the numpy dot function

arr = np.array([[0, 1, 0], [1, 2, -2], [6, 3, 2], [-1, 0, -1], [1, 0, 1]])

arr

np.dot(arr.T, arr) # more about the dot() function in linear algebra below


# The @ infix operator is another way to do matrix multiplication

arr.T @ arr

# Simple transposing with .T is a special case of swapping axes
# In general, use swapaxes() switches a pair of axes

# Note: swapaxes() also just returns a view and not a copy

arr

arr.swapaxes(0, 1)


# -----------------------------------------------------
# 4.2 Pseudorandom Number Generation
# -----------------------------------------------------

# numpy.random - supplements Python random
# example - 4 x 4 array of normal dist

samples = np.random.standard_normal(size=(4, 4,))

samples

# Benchmarking the performance of Numpy vs Python standard

from random import normalvariate

N = 1_000_000

%timeit samples = [normalvariate(0, 1) for _ in range(N)]

%timeit np.random.standard_normal(N)


# Coding an explicit generator

rng = np.random.default_rng(seed=12345)

data = rng.standard_normal((2, 3))

type(rng)

# methods available for random generator objects:
# permutation, shuffle, uniform, integers, standard_normal,
# binomial, normal, beta, chisquare, gamma, uniform


# ----------------------------------------------------------
# 4.3 Universal Functions: Fast Element-wise Array Functions
# ----------------------------------------------------------

# ufunc - these are fast, element-wise array functions

# unary ufuncs - many are simple element-wise transformations

arr = np.arange(10)

arr

np.sqrt(arr)

np.exp(arr)

# binary ufuncs - take two arrays and return a single array

x = rng.standard_normal(8)

y = rng.standard_normal(8)

x

y

# element-wise maximum of elements in x and y
np.maximum(x, y)

# binary ufuncs - a few can multiple arrays

arr = rng.standard_normal(7) * 5

arr

# numpy.modf - unary ufunc that returns more than one array

remainder, whole_part = np.modf(arr)

remainder

whole_part


# ufuncs can assign resulters to existing array using "out"



# Some unary universal functions:
# abs, fabs, sqrt, square, exp, log, log10, log2, log1p,
# sign, ceil, floor, rint, modf, isnan, 
# isfinite, isinf, cos, cosh, sinh, tan, tanh,
# arccos, arccosh, arcsin, arcsinh, arctan, arctanh
# logical_not

# Some binary universal functions:
# add, substract, multiply, divide, floor_divide,
# power, maximum, fmax, minimum, fmin, mod, copysign,
# greater, greater_equal, less, less_equal, equal, not_equal,
# logical_and, logical_or, logical_xor


# --------------------------------------------------------------
# 4.4 Array-oriented Programming with Arrays
# --------------------------------------------------------------

# vectorization - replacing loops with array expressions

points =  np.arange(-5, 5, 0.01) # 1000 equally spaced points

points

# meshgrid produces grid of (x,y) pairs

xs, ys = np.meshgrid(points, points) 

xs

ys

# here we are vectorizing with xs and ys

z = np.sqrt(xs ** 2 + ys ** 2)

# visualizing the Z pairs

import matplotlib.pyplot as plt

plt.imshow(z, cmap=plt.cm.gray, extent=[-5, 5, -5, 5])

plt.colorbar()

plt.title( "Image plot of $\sqrt{x^2 + y^2}$ for a grid of values")

plt.show()



plt.close("all")


# Expressing conditional logic as Array Operations
# ------------------------------------------------

# numpy.where function

xarr = np.array([1.1, 1.2, 1.3, 1.4, 1.5])

yarr = np.array([2.1, 2.2, 2.3, 2.4, 2.5])

cond = np.array([True, False, True, True, False])

# list comprehension form 
# not as efficient, using interpreted Python code
# also does not work with multi-dimensional arrays

result = [(x if c else y) for x, y, c in zip(xarr, yarr, cond)]

result

# do the above with numpy.where

result = np.where(cond, xarr, yarr)

result

# second and third arguments can be scalars
# can be used to modify matrices

arr = rng.standard_normal((4, 4))

arr

# want to replace positives with 2 and negatives with -2

arr > 0

np.where(arr > 0, 2, -2)


# combining scalars and arrays

np.where(arr > 0, 2, arr)
 

# Mathematic and statistical methods
# ----------------------------------

# aggregations car sometimes called reductions

# NumPy allows passing arrays to be aggregated

arr = rng.standard_normal((5, 4))

arr.mean()

np.mean(arr)

arr.sum()

# functions like mean and sum can optionally
# be applied over a given axes

arr

arr.mean(axis=1) # compute mean across the columns

arr.sum(axis=0) # compute sum down the rows
 
 # accumulation functions like cumsum and cumprod 
 # do not aggregate
 # instead, they provide intermediate results
 
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7])
 
arr.cumsum()
 
# accumulation functions and multi-dimensional arrays
# are partial aggregates along the indicated axis

arr = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])

arr

arr.cumsum(axis=0)  # computes along the columns

arr.cumsum(axis=1)  # computes along the rows


# basic statistical methods
# sum, mean, std, var, min, max, argmin, argmax,
# cumsum, cumprod

# Methods for Boolean arrays
# --------------------------

# Booleans are coerced to 1 (True) and 0 (Flase)
# sum counts 1's (True's)

arr = rng.standard_normal(100)

(arr > 0).sum() # sum all the positive values

(arr <= 0).sum() # Summ all the non-positive values

# using any and all with Boolean
# can also work on any array where non-zero value is true

bools = np.array([False, False, True, False])

bools

bools.any()

bools.all()

# Sorting
# -------

arr = rng.standard_normal(6)

arr

arr.sort()

arr

arr = rng.standard_normal((5, 3))

arr

arr.sort(axis=0) # sort across columns

arr

arr.sort(axis=1) # sort across rows

arr

# Note: numpy.sort returns a copy like python built-in sort()

arr2 = np.array([5, -10, 7, 1, 0, -3])

sorted_arr2 = np.sort(arr2)

arr2

sorted_arr2


# Unique and other set logic
# --------------------------

# Numpy set operations for one-dimesional arrays

names = np.array(["Bob", "Will", "Joe", "Bob", "Will", "Joe", "Joe"])

names

np.unique(names)

ints = np.array([3, 3, 3, 2, 1, 1, 4, 4])

np.unique(ints)

# this is the pure Python alternatively

sorted(set(names))


# numpy.in1d tests membership of values in one array in another

values = np.array([6, 0, 0, 4, 2, 5, 6])

values

np.in1d(values, [2, 3, 6])

# array set operations
# unique, intersection, union1d, in1d, setdiff1d, setor1d

# --------------------------------------------------------------
# 4.5 File Input and Output with Arrays
# --------------------------------------------------------------

arr = np.arange(10)

# uncompressed raw binary format

np.save("some_array", arr)

np.load("some_array.npy")

# save multiple arrays in uncompressed archive

np.savez("array_archive.npz", a=arr, b=arr)

arch = np.load("array_archive.npz")

arch["b"]

# compressed format

np.savez_compressed("arrays_compressed.npz", a=arr, b=arr)


# --------------------------------------------------------------
# 4.6 Linear Algebra
# --------------------------------------------------------------

# linear algebra operations
# matrix multiplication, decomnpositions, determinants, square matrix math

rng = np.random.default_rng(seed=12345)

x = np.array([[1., 2., 3.], [4., 5., 6.]])

y = np.array([[6., 23.], [-1, 7], [8, 9]])

x

y

x.dot(y)

np.dot(x, y)  # same as previous

np.ones(3)

x @ np.ones(3)

# numpy.linalg - matrix decompositions, inverse and determinants

from numpy.linalg import inv, qr

X = rng.standard_normal((5, 5))

X

# multiplying the transpose of X by X itself

mat = X.T @ X

mat

inv(mat)

# X.T.dot(X) computes the dot project of X and its transpose X.T

mat @ inv(mat)

# most commonly used linear algebra functions
# diag, dot, trace, det, trace, det, eig, inv, pinv, qr, svd, solve, lstsq


# --------------------------------------------------------------
# 4.7 Example: Random walks
# --------------------------------------------------------------

# application of array operations

import random
import matplotlib.pyplot as plt

position = 0

walk = [position]
nsteps = 1000
for _ in range(nsteps):
    step = 1 if random.randint(0,1) else -1
    position += step
    walk.append(position)
 
plt.plot(walk[:1000])
plt.show()

# random coin toss

nsteps = 1000

rng = np.random.default_rng(seed=1235)

draws = rng.integers(0, 2, size=nsteps)

steps = np.where(draws == 0, 1, -1)

walk = steps.cumsum()

walk.min()

walk.max()

# first crossing time
# when it crosses 10 either direction
# argmax() isn't efficient because it does a full scan of array each time

(np.abs(walk) >= 10).argmax()


# Simulating many random walks at once
# ------------------------------------

# simulating 5000 random walks at once
# see size(nwalks, nsteps) tuple below

nwalks = 5000
nsteps = 1000

draws = rng.integers(0, 2, size=(nwalks, nsteps)) # 0 or 1

steps = np.where(draws > 0, 1, -1)

walks = steps.cumsum(axis=1)

walks

# calculating ax and mix values over all walks

walks.max()

walks.min()

# calculating crossing line of abs 30 over all simulations
# tricky because not all will reach 30 therefore use any()

hits30 = (np.abs(walks) >= 30).any(axis=1)

hits30 

hits30.sum()

# selecting rows of walks that actually cross 30
# using argmax() across axis = 1

crossing_times = (np.abs(walks[hits30]) >= 30).argmax(axis=1)

crossing_times

# calculating average minimum crossing time:

crossing_times.mean()

# trying other distributions than coin-toss

draws = 0.25 * rng.standard_normal((walks, nsteps))


steps = np.where(draws > 0, 1, -1)

walks = steps.cumsum(axis=1)

walks

# calculating ax and mix values over all walks

walks.max()

walks.min()


# --------------------------------------------------------------
# 4.8 Conclusion
# --------------------------------------------------------------

# See  Appendix A for more advanced numpy 






























