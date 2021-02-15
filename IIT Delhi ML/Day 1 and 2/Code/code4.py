# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 16:36:41 2019

@author: Anshu Pandey
"""

import pandas

'''
pandas has 3 data types
1. Pandas Series - to represent 1D data
2. Pandas Dataframe - to represent 2D data
3. Pandas Panel - to represent 3D data
'''

# to read data from a csv file
df = pandas.read_csv(r"D:\AI\iitdelhi\datawh.csv")
df.head()
type(df)
df.shape
##############################
# filtering dataframes
df["Temperature"]
cols=["Temperature","Humidity"]
df[cols]

# conditions

df["Dates"][df["Humidity"]>400]
'''
find the dates when pressure>3 and airquality>1
'''
df["Dates"][df["Pressure"]>3][df["Air Quality"]>1]

#################################################
# AND Condition
df["Dates"][(df["Pressure"]>3) & (df["Air Quality"]>1)]


# OR Condition
df["Dates"][(df["Pressure"]>3) | (df["Air Quality"]>1)]

#########################################################

# statistical analysis
df.describe()

df["Humidity"].mean()
df["Humidity"].min()
df["Humidity"].max()
df["Humidity"].median()
df["Humidity"].mode()
df["Humidity"].var()
df["Humidity"].std()
#################################
###################################
df = pandas.read_csv(r"D:\AI\iitdelhi\datanh.csv",header=None)
df.columns = ["Temp","humi","pressure","airqua"]

#############################################
######### bitcoin data
df=pandas.read_html("https://coinmarketcap.com/currencies/bitcoin/historical-data/")
len(df)
df1 = df[0]
df2 = df[1]

# exporting the dataframe as a file
df1.to_csv("bitcoin.csv")
#######################################################










