# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 17:47:07 2019

@author: Anshu Pandey
"""

import numpy
import pandas
import matplotlib.pyplot as plt
import seaborn as sns

df = pandas.read_csv(r"F:\Data\Codes\Python\ML\IIT Delhi ML\Day 1 and 2\Code\Bank_churn_modelling.csv")
#3 to tdrop threee columns
df.drop(['RowNumber',"CustomerId","Surname"],axis=1,inplace=True)

# probability distributiion of credit score

plt.figure(figsize=(12,5))
sns.distplot(df["CreditScore"][df["Exited"]==0])
sns.distplot(df["CreditScore"][df["Exited"]==1])
plt.legend(['0','1'])
plt.show()


plt.figure(figsize=(12,5))
sns.distplot(df["Age"][df["Exited"]==0])
sns.distplot(df["Age"][df["Exited"]==1])
plt.legend(['0','1'])
plt.show()

###########################################
############################################

plt.figure(figsize=(8,4))
sns.countplot(df["Geography"])
plt.show()
plt.figure(figsize=(8,4))
sns.countplot(df["Geography"][df['Exited']==1])
plt.show()


plt.figure(figsize=(8,4))
sns.countplot(df["Gender"])
plt.show()
plt.figure(figsize=(8,4))
sns.countplot(df["Gender"][df['Exited']==1])
plt.show()

plt.figure(figsize=(8,4))
sns.countplot(df["HasCrCard"])
plt.show()
plt.figure(figsize=(8,4))
sns.countplot(df["HasCrCard"][df['Exited']==1])
plt.show()

##########################################
# age v/s geography v/s exited

plt.figure(figsize=(12,5))
sns.swarmplot(x = "Geography",y = "Age",hue="Exited",data=df)
plt.show()










