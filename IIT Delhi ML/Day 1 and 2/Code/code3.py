# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 15:51:08 2019

@author: Anshu Pandey
"""
'''
numpy = mathematical computation on data
pandas = data import / export and analysis
matplotlib, seaborn - data visualization
'''

import numpy

x = [4,5,6]
y = [7,1,2]

x + y

############################################

x = numpy.array([4,5,6])
y = numpy.array([2,3,8])

x + y
#############################################

x = numpy.array([7,5,2,6,4])

x.max()
x.min()
x.mean()
x.std()
#############################################
x = numpy.array([[4,5,6],[2,7,8],[11,2,9]])
x

x.size  # total number of elements in the array
x.shape # total rows and columns
x.min() # minimum value from array
x.max() # maximum value from array
x.min(axis=1) # row wise minimum values
x.max(axis=1) # row wise maximum values
x.max(axis=0) # column wise maximum values
x.min(axis=0) # column wise minimum values

# creating arrays using numpy
x = numpy.arange(1,10,2)
x = numpy.random.rand(2,3)
x
x = numpy.random.randint(10,50,(2,3))
x
# linear algebra with numpy
'''
4x - 3y = 14
x + 2y = 9
'''
a = [[4,-3],[1,2]]
b = [14,9]
numpy.linalg.solve(a,b)

###################

m = numpy.matrix([[4,5,6],[7,5,2],[3,4,9]])

inv_m = numpy.linalg.inv(m)*m
inv_m.astype("int32")

inv_m.round(2)








