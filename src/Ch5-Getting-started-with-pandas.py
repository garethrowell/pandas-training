

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

# drop method returns new object with values deleted
# from axis

obj = pd.Series(np.arange(5.), index=["a", "b", "c", "d", "e"])

obj

new_obj = obj.drop("c")

new_obj

obj.drop(["d","c"])

# index can be deleted from either axis with DataFrame

data = pd.DataFrame(np.arange(16).reshape((4, 4)),
                    index=["Ohio", "Colorado", "Utah", "New York"],
                    columns=["one", "two", "three", "four"])

data

# drop on a sequence of labels - axis 0 is rows

data.drop(index=["Colorado","Ohio"])

# Use keyword "columns" to drop column labels

data

data.drop(columns=["two"])

# using axis = 1 is same thing

data.drop("two", axis=1)

# or axis = "columns"

data.drop("two", axis="columns")


# Indexing, Selection and Filtering
# ---------------------------------

# Series indexing

obj = pd.Series(np.arange(4.), index=["a", "b", "c", "d"])

obj

obj["b"]

obj[1]

obj[2:4]

obj[["b", "a", "d"]]

obj[[1, 3]]

obj[obj < 2 ]

# better way is to use loc() to select index values

obj.loc[["b", "a", "d"]]

# preferred because loc indexes exclusively with labels
# and iloc indexes exclusively with integers
# without loc, behavior of index will depend on datatype

# For example... // the following is deprecated...

obj1 = pd.Series([1, 2, 3]), index[2, 0, 1])

obj1



obj2 = pd.Series([1, 2, 3], index["a", "b", "c"])

obj1

obj2

##....


# Indexing into a DataFame

data = pd.DataFrame(np.arange(16).reshape((4, 4)), 
                    index=["Ohio", "Colorado", "Utah", "New York"],
                    columns=["one", "two", "three", "four"])
                    
data


data["two"]

data[["three", "one"]]

# Slicing or selecting with Boolean array

data[:2]

data[data["three"] > 5]

# Using a scalar to produce a Boolean dataframe

data < 5

# assigning 0 to True

data[data < 5] = 0

# DataFrame also has loc and iloc

data

data.loc["Colorado"]

# selecting row and column with loc

data.loc["Colorado", ["two", "three"]]

# similar selection using iloc

data.iloc[2]

data.iloc[[2, 0]]

data.iloc[2, [3, 0, 1]]

data.iloc[[1, 2], [3, 0, 1]]

# loc and iloc work with slices, single labels or lists of labels

data.loc[: "Utah", "two"]

data.iloc[:, :3]

data.iloc[:, :3][data.three > 5]

# summary of ways to select and rearrange DataFrames
# df[column], df.loc[rows], df.loc[:, cols], df.loc[rows, cols]
# df.iloc[rows], df.iloc[:, cols], df.iloc[rows, cols],
# df.at[row, col], df.iat[row, col], reindex





# Integer indexing pitfalls
# -------------------------

# pandas integer indexing works different from 
# built=in Python structures

# for example, this generates an error....

ser = pd.Series(np.arange(3.))

ser

# ser[-1]  <<<<<<<<<<<<<<<<<<<

# So the issue is *integer* indexing, which are labels

# Here, we are using a non-integer index without any arrors

ser2 = pd.Series(np.arange(3.), index=["a", "b", "c"])

ser2

ser2[-1] # this also sends off "future" warnings

# Its better to use loc for labels and iloc for integers!!
# ===========================================================

ser.iloc[-1]

ser2.loc["a"]

# Pitfalls with chained indexing
#-----------------------------

# In general, AVOID chained indexing for assignments

data

data.loc[:, "one"] = 1

data

data.iloc[2] = 5

data

data.loc[data["four"] > 5] = 3

data

# But this DOES NOT WORK!!

# data.loc[data.three == 5]["three"] = 6

data

# rewrite the changed assignment using single loc operation

data.loc[data.three == 5, "three"] = 6

data



# Arithmetic and Data Alignment
# -----------------------------

# What happens when we union two objects
# with different indexes?

# Looking at Series

s1 = pd.Series([7.3, -2.5, 3.4, 1.5], index=["a", "c", "d", "e"])

s2 = pd.Series([-2.1, 3.6, -1.5, 4, 3.1], index=["a", "c", "e", "f", "g"])

s1

s2

# Missing values generated where label locations don't overlap

s1 + s2


# Looking at DataFrame, alignment performed on both row and columns
# Note: NaN's for rows and columns not shared in df1 + df2

df1 = pd.DataFrame(np.arange(9.).reshape((3, 3)), columns=list("bcd"), index=["Ohio", "Texas", "Colorado"])

                   
df2 = pd.DataFrame(np.arange(12.).reshape((4, 3)), columns=list("bde"), index=["Utah", "Ohio", "Texas", "Oregon"])
                   
df1

df2

df1 + df2

# Next example, df1 and df2 don't share any rows or columns

df1 = pd.DataFrame({"A": [1, 2]})

df2 = pd.DataFrame({"B": [3, 4]})

df1 

df2

df1 + df2

# Arithmetic methods with fill values
# Setting NA(nulls) by assigning to np.nan

df1 = pd.DataFrame(np.arange(12.).reshape((3, 4)), columns=list("abcd"))
 
df2 = pd.DataFrame(np.arange(20.).reshape((4, 5)), columns=list("abcde"))
                                       
df1

df2

df1 + df2

df2.loc[1, "b"] = np.nan

df1 + df2

# fill_value substitutes passed value with fill value


df1.add(df2, fill_value=0)

# letter r reverses the argument order
# so the following two expressions are the same

1 / df1

df1.rdiv(1)

# Using reindexing and specifying different fill value

df1.reindex(columns=df2.columns, fill_value=0)

# Flexible arithmetic methods and their r equivalents
# add, radd, sub, rsub, div, rdiv, floordiv, ffloordiv,
# mul, rmul, pow, 



# Operations between DataFrame and Series
# ---------------------------------------

# Like NumPy operations with arrays of different dimensions
# There is arithmetic between DataFrames and Series

# Begin by looking two dimensional array and one of its rows

arr = np.arange(12.).reshape((3, 4))

arr

arr[0]

# the following is called broadcasting

arr - arr[0]

# Operations between DataFrame and Series is like this

frame = pd.DataFrame(np.arange(12.).reshape((4, 3)), 
                    columns=list("bde"), index=["Utah", "Ohio", "Texas","Oregon"])
                    
series = frame.iloc[0]

frame

series

# series and dataframe arithmetic matches index <-> columns

frame - series

# if index value not in DataFrame column or Series index
# then objects reindexed to form union

series2 = pd.Series(np.arange(3), index=["b", "e", "f"])

series2

frame + series2

frame - series

frame - series2

# broadcasting over columns, matching on rows

series3 = frame["d"]

frame

series3

frame.sub(series3, axis="index") # the axis to match on



# Function Application and Mapping
# --------------------------------

# NumPy ufuncs (element-wise array methods) work with pandas objects

frame = pd.DataFrame(np.random.standard_normal((4, 3)),
                    columns=list("bde"),
                    index=["Utah", "Ohio", "Texas","Oregon"])
                    
                    
frame

np.abs(frame)


# applying function on one-dimensional arrays to each column or row
# using apply

def f1(x):
    return x.max() - x.min()
    
frame

frame.apply(f1)

# apply across the columns

frame.apply(f1, axis="columns")

# most common array statistics are DataFrame methods so
# you don't need to use apply

# apply returns scalars but it can also return Series for multiple values

def f2(x):
    return pd.Series([x.min(), x.max()], index=["min", "max"])
    
frame
    
frame.apply(f2)

# can also do element-wise functions, here applying format

def my_format(x):
    return f"{x:.2f}"
    
frame.applymap(my_format) # applymap to be deprecated
                            # use DataFrame.map instead
                            
frame["e"]
                            
frame["e"].map(my_format) # Using Series map



# Sorting and ranking
# -------------------

# sort_index() sorts row or column labels

# series example

obj = pd.Series(np.arange(4), index=["d", "a", "b", "c"])

obj

obj.sort_index()

# dataframe example

frame = pd.DataFrame(np.arange(8).reshape((2, 4)),
                     index=["three", "one"],
                     columns=["d", "a", "b", "c"])
                     
frame
                     
frame.sort_index()

frame.sort_index(axis="columns")

# sorting descending order

frame.sort_index(axis="columns", ascending=False)


# sorting a Series by its values

obj = pd.Series([4, 7, -3, 2])

obj

obj.sort_values() <<<<<<<<<<<<

# missing values are sorted at the end

obj = pd.Series([4, np.nan, 7, np.nan, -3, 2])

obj

obj.sort_values()

# sorting them at the start 

obj.sort_values(na_position="first")

# sorting a DataFrame on more than one column

frame = pd.DataFrame({"b":[4, 7, -3, 2], "a":[0, 1, 0, 1]})

frame

frame.sort_values("b")

frame.sort_values(["a", "b"])

# ranking - default is to break ties with mean rank

obj = pd.Series([7, -5, 7, 4, 2, 0, 4])

obj

obj.rank()

# assigning ranks to the order in which they are observed
# in the data, ties are sorted base on the order in which they are observed

obj.rank(method="first")

# ranking in descending order

obj.rank(ascending=False)

# computing DataFrame ranks over rows or columns

frame = pd.DataFrame({"b": [4.3, 7, -3, 2], "a": [0, 1, 0, 1],
                        "c": [-2, 5, 8, -2.5]})
                        
frame

frame.rank(axis="columns")

# Tie-breaking methods with rank
# average, min, max, first, dense


# Axis Indexes with Duplicate labels
# ----------------------------------

# All above working with unique axis labels (index values)
# Severala pandas functions require this

# Series with duplicate indieces

obj = pd.Series(np.arange(5), index=["a", "a", "b", "b", "c"])

obj

# testing for unique using is_unique()

obj.index.is_unique

# This affects data selection and makes coding
# really complicated

obj["a"]

obj["c"]

# Likewise in data frames

df = pd.DataFrame(np.random.standard_normal((5, 3)),
                  index=["a", "a", "b", "b", "c"])
                  
df









# ----------------------------------------------------
# 5.3 Summarizing and Computing Descriptive Statistics
# ----------------------------------------------------

# Correlation and covariance
# --------------------------

# Unique values, value couns, and membership
# ------------------------------------------

# Conclusion
# ----------





