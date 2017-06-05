from matplotlib.pyplot import*
import numpy as np
import matplotlib.pyplot as plt


def f(x):
	return x**2 - 6*x + 8



def secantes( a , b  , f ,  kmax ):
	ant = a
	x = b
	i = 0
	dif = 10000000

	while( i < kmax and dif > 0.0000001 ):

		x = b - (( f(b)/( f(b) - f(a))) * (b - a))

		a = b
		b = x

		dif = abs( b - a)
		i = i + 1
		print('Iteração: ' , i , ' xn: ' , b)

	print('result: ' , x)



secantes( 10 , 20 , f  , 5000)
	

