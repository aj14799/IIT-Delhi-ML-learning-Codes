# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 17:36:42 2019

@author: Anshu Pandey
"""

'''
Data Visualization using matplotlib
'''
import numpy
import matplotlib.pyplot as plt

x = numpy.arange(1,10,0.5)
y = numpy.sin(x)
# line plot
plt.figure(figsize=(12,5))
plt.plot(x,y,c='r')
plt.show()

# sactter plot
plt.figure(figsize=(12,5))
plt.scatter(x,y,c='r')
plt.show()

# pie chart
lbs = ["DEL","BLR","BOM","MAA"]
vals = [45,23,56,78]

plt.pie(vals,labels=lbs)
plt.show()










