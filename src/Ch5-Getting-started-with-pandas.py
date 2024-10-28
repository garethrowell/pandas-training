

# ----------------------------------------------------
# Ch 5 Getting started with pandas
# ----------------------------------------------------

import numpy as np

import pandas as pd

from pandas import Series, DataFrame



# ----------------------------------------------------
# 5.1 Introduction to pandas data structures
# ----------------------------------------------------

# Series
# ------


obj = pd.Series([4, 7, -5, 3])

obj

# default indext is 0 through N - 1

obj.array

obj.index

# using index to identify each data point with label

obj2 = pd.Series([4, 7, -5, -3], index=["d", "b", "a", "c"])

obj2

obj2.index

# selecting single or sets of values in label index

obj2["a"]

obj2["d"] = 6

obj2[["c", "a", "d"]]

# Using numpy like operations

obj2

obj2[obj2 > 0]

obj2 * 2

np.exp(obj2)

# Series can be viewed as fixed-length ordered data dictionary
# where index maps to data values

"b" in obj2

"e" in obj2

# creating a series from a dictionary

sdata = {"Ohio":35000, "Texas":71000, "Oregon":16000, "Utah":5000}

sdata

obj3 = pd.Series(sdata)

obj3

# convert a Series to a dictionary using to_dict() method

obj3

obj3.to_dict()

# default - original order is preserved, override with index containing
# the order you want

sdata = {"Ohio":35000, "Texas":71000, "Oregon":16000, "Utah":5000}

obj3

states = ["California", "Ohio", "Oregon", "Texas"]

obj4 = pd.Series(sdata, index=states)

obj4

# Using is na and is not na

pd.isna(obj4)

pd.notna(obj4)

# alternative Series methods

obj4.isna()

# Series aligns indexes for arithmetic operations
# this is similar to a join operation

obj3

obj4

obj3 + obj4

# the Series 'name' attribute

obj4.name = "population"

obj4.index.name = "state"

obj4

# altering Series index by in-place assignment

obj

obj.index = ["Bob", "Steve", "Jeff", "Ryan"]

obj


# DataFrame
# ---------
# DataFrames are typically 2 dimensional but higher dimensions
# work just find with hierarachical indexing

# construct DataFrame using dictionary of equal-length lists
# or numpy arrays

# here, the order of the keys in data determine the DataFrame layout

data = {"state": ["Ohio", "Ohio", "Ohio", "Nevada", "Nevada", "Nevada"],
        "year": [2000, 2001, 2002, 2001, 2002, 2003],
        "pop": [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]}

data
        
frame = pd.DataFrame(data)

frame

# head returns first 5 rows
# tail returns last 5 rows

frame.head()

frame.tail()

# controlling column arrangement

pd.DataFrame(data, columns=["year", "state", "pop"])

# passing a column that isn't in the dictionary

frame2 = pd.DataFrame(data, columns=["year", "state", "pop", "debt"])

frame2

frame2.columns

# Retrieving as a Series, two forms

frame2["state"]

frame2["year"]

# Preferred form as attribute, avoid method name conflicts
 
frame2.state 

frame2.year 

# Using iloc and loc attributes to retrieve rows

frame2

frame2.loc[1]

frame2.iloc[2]

# modifying columns by assignment

frame2["debt"] = 16.5

frame2

frame2["debt"] = np.arange(6.)

frame2

# the value length must match the df length

val = pd.Series([-1.2, -1.5, -1.7], index=["two", "four", "five"])

val

frame2["debt"] = val

# Assigning a column that doesn't exist creates new column

frame2["eastern"] = frame2["state"] == "Ohio"

# this doesn't work using dot notation

# use del method to remove column

frame2.columns

del frame2["eastern"]

frame2.columns


# using nested dictionary of dictionaries

populations = {"Ohio":{2000: 1.5, 2001: 1.7, 2002: 3.6}, "Nevada":{2001: 2.4, 2002: 2.4, 2002: 2.9}}

populations

# outer keys goes to columns, inner keys goes to rows

frame3 = pd.DataFrame(populations)

frame3

frame3.columns

# Transposing ala numpy

Tframes3 = frame3.T

Tframes3

# Transposing back loses some data type infor

Tframes3.T

# using explicit index

pd.DataFrame(populations, index=[2001, 2002, 2003])

# distionaries with Series object

pdata = {"Ohio": frame3["Ohio"][:-1], "Nevada":frame3["Nevada"][:2]}

pdata

pd.DataFrame(pdata)

# Things that you can pass to the DataFrame constructor
# 2D ndarray (optional row and column labels; dictionary of arrayrs, lists,
# or tuples (all sequences must have same length; NumPy structured array; 
# dictionary of Series; dictionary of dictionaries; list of dictionaries or Series
# list lists or tuples (2D ndarray); another DataFrame; numpy masked array.

# index names

frame3.index.name = "year"

frame3.columns.name = "state"

frame3

# DataFrame has index and column names
# Series has name attribute

# converting DataFrame to 2D ndarray

frame3.to_numpy()

# when columns have different data types

frame2

frame2.to_numpy()


# Index objects
#--------------

# index objects hold axis labels 
# (names, column names, axis name or names)

obj = pd.Series(np.arange(3), index=["a", "b", "c"])

index = obj.index

index

index[1:]

# indexes are immutable

# index[1] = "d"
# TypeError: Index does not support mutable operations

# this makes is safe to share Index objects among data structures

labels = pd.Index(np.arange(3))

labels

obj2 = pd.Series([1.5, -2.5, 0], index=labels)

obj2

obj2.index is labels

# Index also behaves like a fixed-size set

frame3

frame3.columns

"Ohio" in frame3.columns

2003 in frame3.index

# NOTE - pandas Index *can* contain duplicate labels:

pd.Index(["foo", "foo", "bar", "bar"])

# Some Index methods and properties
# append(), difference(), intersection(), union(), isin(),
# delete(), drop(), insert(), is_monotonic(), unique()

# ----------------------------------------------------
# 5.2 Essential Functionality
# ----------------------------------------------------

# Reindexing
# ----------

# creates new object with values rearranged to align new index

obj = pd.Series([4.5, 7.2, -5.3, 3.6], index=["d", "b", "a", "c"])

obj

obj2 = obj.reindex(["a", "b", "c", "d", "e"])

obj2

# for ordered data like time series, want to fill in values when reindexing

obj3 = pd.Series(["blue", "purple", "yellow"], index=[0, 2, 4])

obj3

obj3.reindex(np.arange(6), method="ffill")

# reindex can alter rows, columns or both

frame = pd.DataFrame(np.arange(9).reshape((3, 3)), 
                    index=["a", "c", "d"], 
                    columns=["Ohio", "Texas", "California"])

frame

frame2 = frame.reindex(index=["a", "b", "c", "d"])

frame2

# reindexing the columns with column keyword

states = ["Texas", "Utah", "California"]

frame.reindex(states, axis="columns")

# reindex function arguments
# labels, index, columns, axis, method (ffil - fill forwards, bfill - fill backwares),
# fill_value, limit, tolerance, level, copy

# loc operator reindex for new existing labels
# as opposed to reindex which actually insert
# missing data for new labels

# e.g.

frame.loc[["a", "d", "c"], ["California", "Texas"]]


# Dropping Entries from an Axis
# -----------------------------


# Indexing, Selection and Filtering
# ---------------------------------

# Arithmetic and Data Alignment
# -----------------------------

# Function Application and Mapping
# --------------------------------

# Sorting and ranking
# -------------------

# Axis Indexes with Duplicate labels
# ----------------------------------



# ----------------------------------------------------
# 5.3 Summarizing and Computing Descriptive Statistics
# ----------------------------------------------------

# Correlation and covariance
# --------------------------

# Unique values, value couns, and membership
# ------------------------------------------

# Conclusion
# ----------





