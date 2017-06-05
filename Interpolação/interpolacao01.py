import numpy as np
from matplotlib.pyplot import *

def polinear( x ):
	m = np.ones((x.shape[0] , x.shape[0]))
	
	for i in range( x.shape[0]):
		for j in range( x.shape[0]):
			m[i][j] = x[i] ** (x.shape[0] - j - 1)
			
	return m
def calcula( c , x):
	soma = 0
	for i in range( c.shape[0]):
		soma+= c[i] * x ** (c.shape[0] - i - 1)

	return soma

x = np.array([ 3 , 13 , 17])
y = np.array( [161.85 , 850.85 , 1302.85])

#plot(x , y)
#show()

m = np.zeros((x.shape[0] , x.shape[0]))

m = polinear( x )

#print( m )

c = np.linalg.solve( m , y)

print( c)

xteste = np.linspace(1 , 100 , 200)
yteste = calcula(c , xteste)
axvline( linewidth=1, color='r')
axhline( linewidth=1, color='r')
#axis('auto')

plot(xteste , yteste)

show()

# print( xteste )
# print( yteste )

while 1:
	x = int(input())

	result = calcula( c , x)
	print( result )