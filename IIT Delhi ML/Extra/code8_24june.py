# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 21:51:28 2019

@author: Anshu Pandey
"""

import numpy
import pandas
import matplotlib.pyplot as plt
import seaborn as sns


# load the data
df = pandas.read_csv(r"F:\Data\Codes\Python\ML\IIT Delhi ML\Day 1 and 2\Code\Bank_churn_modelling.csv
# drop some columns which are not so important based on domain knowledge

df.drop(['CustomerId',"Surname","RowNumber"],axis=1,inplace=True)
# axis =1 to drop a cloumn and axis = 0 to drop a row
# inplace = True => permanent changes to the dataframe
df.shape
##############################################################
# check for missing values - wether data has missing values or not
df.isnull().sum()
# our data doesnt have missing values so we are good to go ahead

# check for duplicates
df.duplicated().sum()
# df.drop_duplicates(inplace=True)
# we dont dont have duplicate customer entries so we are good to
# go ahead

###########################################################
# Analytics using Data Visualization
# impact of creditscore v/s exited
# probability distribution analysis
plt.figure(figsize=(12,5))
sns.distplot(df["CreditScore"][df["Exited"]==0])
sns.distplot(df["CreditScore"][df["Exited"]==1])
plt.legend(['0','1'])
plt.show()

# age v/s exited
plt.figure(figsize=(12,5))
sns.distplot(df["Age"][df["Exited"]==0])
sns.distplot(df["Age"][df["Exited"]==1])
plt.legend(['0','1'])
plt.show()

#################################################
#################################################
# georgaphy v/s exited
plt.figure(figsize=(6,4))
sns.countplot(df['Geography'])
plt.show()
plt.figure(figsize=(6,4))
sns.countplot(df['Geography'][df['Exited']==1])
plt.show()


# gender v/s exited
plt.figure(figsize=(6,4))
sns.countplot(df['Gender'])
plt.show()
plt.figure(figsize=(6,4))
sns.countplot(df['Gender'][df['Exited']==1])
plt.show()


# HasCrCard v/s exited
plt.figure(figsize=(6,4))
sns.countplot(df['HasCrCard'])
plt.show()
plt.figure(figsize=(6,4))
sns.countplot(df['HasCrCard'][df['Exited']==1])
plt.show()

















