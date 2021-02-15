# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 17:36:52 2019

@author: aj147
"""

#Data Visualization using matplotlib
import numpy
import matplotlib.pyplot as plt

x = numpy.arange(1,10,0.5)
y = numpy.sin(x)

plt.figure(figsize=(12,5))
plt.plot(x,y,c='r')
plt.show()

#scatter plot
plt.figure(figsize=(12,5))
plt.scatter(x,y,c='r')
plt.show()

# pie chart
lbs = ["Del","BLR","BOM","MAA"]
vals = [45,34,23,56]
 
plt.pie(vals,labels=lbs)
plt.show()
