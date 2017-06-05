from matplotlib.pyplot import*
import numpy as np
import matplotlib.pyplot as plt


def f(x):
	return x**2 - 85*x + 400



def falsi( a , b  , f ,  kmax ):
	i = 0
	dif = 10000000
	x = 1

	while( i < kmax and dif > 0.0000001 ):

		ant = x
		x = ( (f(b) * a - f(a) * b) / ( f(b) - f(a)))

		if( f(a) * f(x) < 0 ):
			b = x
		else:
			a = x


		dif = abs( x - ant)
		i = i + 1
		print('Iteração: ' , i , ' xn: ' , x)

	print('result: ' , x)



falsi( -10000 , 50 , f  , 5000)
	

