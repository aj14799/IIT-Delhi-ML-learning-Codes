import numpy
x=numpy.array([4,5,6])
y=numpy.array([4,6,8])
x+y

x.max()
x.min()
x.mean()


x=numpy.array([[3,5,6],[2,7,8],[7,8,9]])


x.shape
x.min(axis=1)

x.max(axis=1)

x.max(axis=1)

x.max(axis=0)

x.min(axis=0)
x = numpy.arange(1,10,2)
x

x = numpy.arange(1,50,5)
x


x= numpy.random.rand(5)
x=numpy.random.randint(10,50,(2,3))
x

#linear alegebra
'''
4x-3y=9
x+2y=9
'''
a = [[4,-3],[1,2]]
b = [14,9]

numpy.linalg.solve(a,b)

##################################

m = numpy.matrix([[4,5,6],[7,5,2],[3,4,9]])

inv_m = numpy.linalg.inv(m)*m
inv_m.astype("int32")

inv_m.round(2)

