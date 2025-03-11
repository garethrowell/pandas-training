
# ----------------------------------------------------
# Ch 6 Data loading, storage and file formats
# ----------------------------------------------------

import numpy as np

import pandas as pd

from pandas import Series, DataFrame



# ----------------------------------------------------
# 6.1 Reading and writing data in text format
# ----------------------------------------------------

# C:\Users\GRowell\pydata-book\examples

# Text and binary data loading functions
# --------------------------------------
# read_csv, read_fwf, read_clipboard, read_excel,
# read_hdf (hierarchical data format), read_html,
# read_json, read_feather, read_orc (Hadoop and Spark),
# read_parquet, read_pickle (Python), read_sas,
# read_spss, read_sql, read_sql_table (uses SQLAlchemy),
# read_stata (statistics software), read_xml

# categories of optional arguments
# Indexing, Type inference and data conversion,
# Date and time parsing, Iterating, Unclean data issues

# Parsing functions 

# sample data:
#(pydata-book) C:\Users\GRowell\pydata-book\examples>type ex4.csv
# hey!
# a,b,c,d,message
# just wanted to make things more difficult for you
# who reads CSV files with computers, anyway?
#  1,2,3,4,hello
#  5,6,7,8,world
#  9,10,11,12,foo

pd.read_csv("../pydata-book/examples/ex4.csv", skiprows=[0, 2, 3])

# Handling missing values

#(pydata-book) C:\Users\GRowell\pydata-book\examples>type ex5.csv
#something,a,b,c,d,message
#one,1,2,3,4,NA
#two,5,6,,8,world
#three,9,10,11,12,foo

result = pd.read_csv("../pydata-book/examples/ex5.csv")

result

pd.isna(result)



# Using the na_values option

result = pd.read_csv("../pydata-book/examples/ex5.csv", na_values=["NULL"])

result

pd.isna(result)



#  Disabling the NaN value representations

result2 = pd.read_csv("../pydata-book/examples/ex5.csv", keep_default_na=False)

result2

pd.isna(result2)


result3 = pd.read_csv("../pydata-book/examples/ex5.csv", keep_default_na=False,
                                               na_values=["NA"])

result3

pd.isna(result3)



# Different NA sentinels specified by column in dictionary

sentinels = {"message": ["foo", "NA"], "something":["two"]}


pd.read_csv("../pydata-book/examples/ex5.csv", na_values=sentinels, keep_default_na=False)


# some pandas.read_csv function arguments
# ---------------------------------------
# path, sep, delimiter, header, index_col, names,
# skiprows, na_values, keep_default_na, comment,
# parse_dates, keep_date_col, converters,
# dayfirst, nrows, iterator, chunksize, skip_footer,
# verbose, encoding, squeeze, thousands, 
# decimel, engine


# Reading text files in pieces
# ----------------------------



# Writing data to text format
# ---------------------------


# Working with other delimited formsts
# ------------------------------------

# JSON data
# ---------



# XML and HTML: Web scraping
# --------------------------



# ----------------------------------------------------
# 6.2 Binary Data Formats
# ----------------------------------------------------


# Reading Microsoft Excel files
# -----------------------------


# Using HDF5 Format
# -----------------


# ----------------------------------------------------
# 6.3 Interacting with Web APIs
# ----------------------------------------------------


# ----------------------------------------------------
#  6.4 Interacting with databases
# ----------------------------------------------------



# ----------------------------------------------------
#  6.5 Conclusion
# ----------------------------------------------------












