
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







# Basic indexing and slicing
# --------------------------

# Boolean indexing
# ----------------


# Fancy indexing
# --------------

# Transposing arraus and Swapping Axes
# ------------------------------------

# -----------------------------------------------------
# 4.2 Pseudorandom Number Generation
# -----------------------------------------------------

# ----------------------------------------------------------
# 4.3 Universal Functions: Fast Element-wise Array Functions
# ----------------------------------------------------------

# --------------------------------------------------------------
# 4.4 Array-oriented Programming with Arrays
# --------------------------------------------------------------

# Expressing conditional logic as Array Operations
# ------------------------------------------------

# Mathematic and statistical methods
# ----------------------------------

# Methods for Boolean arrays
# --------------------------

# Sorting
# -------

# Unique and other set logic
# --------------------------


# --------------------------------------------------------------
# 4.5 File Inout and Output with Arrays
# --------------------------------------------------------------



# --------------------------------------------------------------
# 4.6 Linear Algebra
# --------------------------------------------------------------


# --------------------------------------------------------------
# 4.7 Linear Algebra
# --------------------------------------------------------------

# --------------------------------------------------------------
# 4.7 Example: Random walks
# --------------------------------------------------------------

# Simulating many random walks at once
# ------------------------------------


# --------------------------------------------------------------
# 4.8 Conclusion
# --------------------------------------------------------------
































