from matplotlib.pyplot import*
import numpy as np
import matplotlib.pyplot as plt


def f(x):
	return x+1

	
def refina(a,b,f):
	x = (a+b)/2.0
	if(f(a)*f(x)<0): 
		b=x
	else:
		a=x
	return (a,b,x)
def isola(a,b,f):
	i=0
	x=238749287
	dif = 1000000000
	while(i<20 and dif > 0.001 ):
		ant = x
		(a,b,x) = refina(a,b,f)
		dif = abs(x - ant)
		ptx = np.linspace(a,b,100)
		plot(ptx,f(ptx),'b-')
		i=i+1
		

		axvline(x=a,color='r',linestyle='--')
		axvline(x=b,color='r',linestyle='--')
		plot(x,0,'r--o')
		show()
		print('Iteracao: ' , i , ' a: ' , a , ' b: ' , b , 'dif: ' , dif)

isola(-15,15,f)

