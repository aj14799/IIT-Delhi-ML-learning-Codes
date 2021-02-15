# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 16:37:04 2019

@author: aj147
"""

import pandas


'''
pandans has 3 data types

1. Pandas Series - to represent 1D data
1. Pandas Dataframe - to represent 2D data
1. Pandas Panel - to represent 3D data
'''

#to read data from a csv file

df = pandas.read_csv(r"C:\Users\aj147\Desktop\ML\datawh.csv")
df.head()
type(df)
df.shape

#####################

# filtering data frame
df["Temperature"]
type(df["Temperature"])

cols=["Temperature","Humidity"]
df[cols]
df["Dates"]

#conditions
df["Dates"][df["Humidity"]>400]

'''
find the dates when pressure >3 and air quality >1

'''
df["Dates"][df["Pressure"]>3][df["Air Quality"]>1]


########################################
df["Dates"][(df["Pressure"]>3) & (df["Air Quality"]>1)]

##############################################
#Or Condition
df["Dates"][(df["Pressure"]>3) | (df["Air Quality"]>1)]

################
#Statistical analysis
df.describe()

df["Humidity"].mean()
df["Humidity"].min()
df["Humidity"].max()
df["Humidity"].median()
df["Humidity"].mode()
df["Humidity"].var()
df["Humidity"].std()


df = pandas.read_csv(r"C:\Users\aj147\Desktop\ML\datanh.csv", header= None)
df.columns = ["Temp", "humid", "pressure", "airquan"]
df.head()

df = pandas.read_html("https://coinmarketcap.com/currencies/bitcoin/historical-data/")
len(df)

df1=df[0]
df2=df[1]

df1.to_csv("bitcoin.csv")

#####################################################












