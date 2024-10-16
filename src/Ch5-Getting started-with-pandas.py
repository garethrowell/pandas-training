

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




















# DataFrame
# ---------

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





