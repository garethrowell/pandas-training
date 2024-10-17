

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
















# Index objects
#--------------



# ----------------------------------------------------
# 5.2 Essential Functionality
# ----------------------------------------------------


# Reindexing
# ----------

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





