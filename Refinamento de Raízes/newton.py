from matplotlib.pyplot import*
import numpy as np
import matplotlib.pyplot as plt


def f(x):
	return 2*x**3 + 3*x**2 - 2

def flinha( x ):
	return 6*x**2 + 6 * x


def newton( x0 , f , flinha, kmax ):
	ant = x0
	x = x0
	i = 0
	dif = 10000000

	while( i < kmax and dif > 0.00001 ):
		ant = x
		x = x - ( f(x)/flinha(x))
		dif = abs( x - ant)
		i = i + 1
		print('Iteração: ' , i , ' xn: ' , x)

	print('result: ' , x)



newton( 0.5 , f , flinha , 5000)
	

