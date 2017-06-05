import numpy as np
from matplotlib.pyplot import *

def lagrange( xalvo , x , y ):
	z = 0
	for i in range( x.shape[0] ):
		mult = y[i]
		for j in range( x.shape[0]):
			if( j !=  i ):
				mult = mult * (( xalvo - x[j])/( x[i] - x[j]))

		z = z + mult
	return z

x = np.array([ 1250 , 1000 , 750])
y = np.array( [25 , 15 , 10])

res = lagrange( 850 , x , y)

print( "fon" , res )

