
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

pd.options.display.max_rows = 10

result = pd.read_csv("../pydata-book/examples/ex6.csv")

result


pd.read_csv("../pydata-book/examples/ex6.csv", nrows=5)


# chunksize is number of rows

chunker = pd.read_csv("../pydata-book/examples/ex6.csv", chunksize=1000)

type(chunker)

# returns -> pandas.io.parsers.readers.TextFileReader
# use to interate over csv file

tot = pd.Series([], dtype='int64')
for piece in chunker:
    tot = tot.add(piece["key"].value_counts(), fill_value=0)
    tot
    
tot = tot.sort_values(ascending=False)

tot  = tot.sort_index()


# Writing data to text format
# ---------------------------

data = pd.read_csv("../pydata-book/examples/ex5.csv")

data.to_csv("out1.csv")

# Using othter separators

import sys

data.to_csv(sys.stdout, sep="|")

# Using a sentinel for a missing value

data.to_csv(sys.stdout, na_rep="NULL")

# default rows and column labels are written - disabled below

data.to_csv(sys.stdout, index=False, header=False)

# working with a subset of columns

data.to_csv(sys.stdout, index=False, columns=["a", "b", "c"])



# Working with other delimited formsts
# ------------------------------------

# here, using built-in Python csv module

import csv

f = open("../pydata-book/examples/ex7.csv")

reader = csv.reader(f)

for line in reader:
    print(line)
    
f.close()

# somne data wrangling

with open("../pydata-book/examples/ex7.csv") as f:
    lines = list(csv.reader(f))

# split the lines into header and data

header, values = lines[0], lines[1:]

header

values

# create a dictionary of data columns
# using dictionary comprehension
# and zip(*values) - this is memory intensive

data_dict = {h:  v for h, v in zip(header, zip(*values))}

data_dict

# many flavors of csv files - csv.Dialect

import csv

f = open("../pydata-book/examples/ex7.csv")


class my_dialect(csv.Dialect):
    lineterminator = "\n"
    delimiter = ";"
    quotechar = '"'
    quoting = csv.QUOTE_MINIMAL


reader = csv.reader(f, dialect=my_dialect)

for line in reader:
    print(line)
    
# CSV dialect options
# delimiter, lineterminator, quotechar, 
# quoting, skipinitialspace, doublequote,
# escapechar

# using csv.writer with dialect

with open("mydata.csv", "w") as f:
    write = csv.writer(f, dialect=my_dialect)
    write.writerow(("one", "two", "three"))
    write.writerow(("1", "2", "3"))
    write.writerow(("4", "5", "6"))
    write.writerow(("7", "8", "9"))
    

# JSON data
# ---------

# example of a JSON record

obj = """
{"name": "Wes",
 "cities_lived": ["Akron", "Nashville", "New York", "San Francisco"],
 "pet": null,
 "siblings": [{"name": "Scott", "age": 34, "hobbies": ["guitars", "soccer"]},
              {"name": "Katie", "age": 42, "hobbies": ["diving", "art"]}]
}
"""

# JSON basic types are objects (dictionaries), arrays (lists), strings,
# numbers, Booleans, and nulls. All keys must be strings.

# standard Python library

import json

result = json.loads(obj) # converts to Python form

result

asjson = json.dumps(result) # converts back to JSON

asjson

# passing list of dictionaries (from JSON objects) to 
# DataFrame constructor and select subset of fields

siblings = pd.DataFrame(result["siblings"], columns= ["name", "age"])

siblings

# exanples.example.json
[{"a": 1, "b": 2, "c": 3},
 {"a": 4, "b": 5, "c": 6},
 {"a": 7, "b": 8, "c": 9}]

data = pd.read_json("../pydata-book/examples/example.json")

data

# exporting to JSON
data.to_json(sys.stdout)

data.to_json(sys.stdout, orient="records")



# XML and HTML: Web scraping
# --------------------------

# conda install lxml beautifulsoup4 html5lib

tables = pd.read_html("../pydata-book/examples/fdic_failed_bank_list.html")

tables

len(tables)

failures = tables[0]

failures.head()

close_timestamps = pd.to_datetime(failures["Closing Date"])

close_timestamps.dt.year.value_counts()

# parsing XML with lxml.objectify
# data from the New York Metropolitan Transportation Authority (MTA)
# xml data from a single train or bus service

# Example - single record
#<INDICATOR>
#  <INDICATOR_SEQ>373889</INDICATOR_SEQ>
#  <PARENT_SEQ></PARENT_SEQ>
#  <AGENCY_NAME>Metro-North Railroad</AGENCY_NAME>
#  <INDICATOR_NAME>Escalator Availability</INDICATOR_NAME>
#  <DESCRIPTION>Percent of the time that escaltors are operational
#  systemwide. The availability rate is based on physical observations performed
#  the morning of regular business dayes only. This is a new indicator
#  the agency began reporting in 2009.</DESCRIPTION>
#  <PERIOD_YEAR>2011</PERIOD_YEAR>
#  <PERIOD_MONTH>12</PERIOD_MONTH>
#  <CATEGORY>Service Indicators</CATEGORY>
#  <FREQUENCY>M</FREQUENCY>
#  <DESIRED_CHANGE>U</DESIRED_CHANGE>
#  <INDICATOR_UNIT>%<INDICATOR_UNIT>
#  <DECIMAL_PLACES>1</DECIMAL_PLACES>
#  <YTD_TARGET>97.00</YTD_TARGET>
#  <YTD_ACTUAL></YTD_ACTUAL>
#  <MONTHLY_TARGET>97.00</MONTHLY_TARGET>
#  <MONTHLY_ACTUAL></MONTHLY_ACTUAL>
#</INDICATOR>

from lxml import objectify

path = "../pydata-book/datasets/mta_perf/Performance_MNR.xml"

with open(path) as f:
    parse = objectify.parse(f)
    
root = parse.getroot()

root.INDICATOR

data=[]

skip_fields = ["PARENT_SEQ", "INDICATOR_SEQ", 
               "DESIRED_CHANGE", "DECIMAL_PLACES"]
               
               
for elt in root.INDICATOR:
    el_data = {}
    for child in elt.getchildren():
        if child.tag in skip_fields:
            continue
        el_data[child.tag] = child.pyval
    data.append(el_data)
    
    
pd.set_option('display.max_columns', None)

    
perf = pd.DataFrame(data)

perf.head()


# pandas.read_xml function does all of the above

perf2 = pd.read_xml(path)

perf2.head()

# Use docstring for more complex XML





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












