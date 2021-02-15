# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 17:09:49 2019

@author: Anshu Pandey
"""

print("Hello World")

x = 5
print(x)
# i am single line comment

'''
i amm comment
i am also comment
...
...
we all are comment in three quotes
'''
'''
Four superheros of any programming language

1. Data Types    - integer, float, string
2. Control flow - if else, for loop and while loop
3. Functions - user defined and built in functions
4. OOPs - Object oriented programming
'''
# 1. Data types
x = 5
x
type(x)
y = 0.25
type(y)
z = "hello"
type(z)
#########################
x = [4,5,8,6,8,"hi",0.258]
type(x)
x[0]
x[2]
x[5]
x[-1]
x[-2]
x[-3]

############################################
###########################################
# if else in python
weight = 48

if weight<50:
    print("you are underweight")
    print("Eat more study less")
elif weight>50 and weight<70:
    print("you are fit")
    print("Stay healthy and stay away from fooders")
    print("Stay fit")
else:
    print("you may be overweight")
    print("start using stairs, lift is ur enemy")
    print("Leave CSE and join mechanical")

##################################################
#################################################


for i in range(5):
    print("Hello from Python",i)
    

for i in range(3,10):
    print("hello from python ", i)

for i in range(3,10,2):
    print("hello from python ", i)

################################################
################################################
    
while True:
    print("python is awesome")
    
x=5
while x<20:
    print("python is amazing")
    x = x+1
    
    
x = 5
while True:
    print("Python is both awesome and amazing")
    x = x+1
    if x>20:
        break
    
################################################
###############################################

# Functions
x = [7,5,8]

len(x)
max(x)    
min(x)    
sum(x)    
#############################
# user defined functions in python

def robotech_labs():
    print("Hello from Robotech Labs")    
    

robotech_labs()

def myfun(a,b,c):
    d = a + b - c
    return d    
    
myfun(7,4,2)    












