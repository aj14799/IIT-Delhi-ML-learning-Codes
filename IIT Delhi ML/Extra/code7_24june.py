

import numpy
import matplotlib.pyplot as plt
import theano

# developing the algorithm
x = theano.tensor.fvector('x')
y = theano.tensor.fvector('y')
m = theano.shared(0.6,'m')
c = theano.shared(0.8,'c')
# regeression equation
yhat = m*x + c

# cost function
cost = theano.tensor.mean(theano.tensor.sqr(y-yhat))/2

# gradient descent algorithms
LR = 0.08
gradm = theano.tensor.grad(cost,m) # dj/dm
gradc = theano.tensor.grad(cost,c) # dj/dc
#gradient descent equaation to update m & c
mn = m - LR*gradm
cn = c - LR*gradc

# creating a function for the above process
train = theano.function(inputs=[x,y],outputs=cost,
                        updates=[(m,mn),(c,cn)])

# lets prepare data
# take some random data
area = [1.2,1.8,2.6,4.5,3.6,8.6,7.6,2.6,3.5,3.4,5.6]
price = [180,210,240,420,380,780,720,320,420,410,580]

area = numpy.array(area).astype('float32')
price = numpy.array(price).astype('float32')

# train the model with the data
for i in range(500):
    cost_val = train(area,price)
    print(cost_val)


m.get_value()
c.get_value()

ypred = area*m.get_value() + c.get_value()
# plot the data points
plt.scatter(area,price)
plt.plot(area,ypred,c='r')
plt.show()




