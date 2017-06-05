import numpy as np 
import time 

def fat( x ):
	res = 1;
	for i in range(1 , x + 1):
		res *=i

	return i;

def f( x ):
	return np.sin( np.deg2rad(x)) + 2 * x + 1

# def f( x ):
# 	return ( 10 * x ** 4) + (2 * x ) + 1
	
def CalculaOrdens( x , y ):
	ord = np.zeros( (x.shape[0] , x.shape[0]))
	ord [0] = y

	for i in range( 1 , x.shape[0]):
		for j in range( 0, (x.shape[0] - i) ):
			ord[i][j] = ( ord[i-1][j+1] - ord[i-1][j])


	#print( ord )
	return ord

def Interpola( xalvo , x , y , mat):
	soma = mat[0][0]
	prod = 1

	ux = ( xalvo - x[0])/( x[1] - x[0])
	for i in range( 1 , x.shape[0]):
		prod = (mat[i][0]/ fat(i))

		for j in range( i ):
			prod *= ( ux - j)
			

		soma += prod


	return soma;
	

ini = time.clock()

# x = np.array([ 1250 , 1000 , 750])
# y = np.array([25 , 15 , 10])

# x = np.array([0.0,  0.3,  0.6])
# y = np.array([1.008,  1.125,  1.512])

x = np.array([ 0.1 , 0.2 ])
y = np.array([f(0.1) , f(0.2)])

# x = np.array([ 1950 , 1970 , 1991])
# y = np.array([139620 , 311622 , 1011500])

# print('Altura 850 -> distancia: ' , Interpola( 850 , x , y , CalculaOrdens(x , y) ))
# print('Altura 1050 -> distancia: ' , Interpola( 1050 , x , y , CalculaOrdens(x , y) ))
# print('Altura 1200 -> distancia: ' , Interpola( 1200 , x , y , CalculaOrdens(x , y) ))

# print('Ano 1958 -> Populacao: ' , Interpola( 1958 , x , y , CalculaOrdens(x , y) ))
# print('Aano 1988 -> Populacao: ' , Interpola( 1988 , x , y , CalculaOrdens(x , y) ))

interpolado = Interpola( 0.15 , x , y , CalculaOrdens(x , y) )
real = f( 0.15 )

print('P(0.15): ' , interpolado)
print('Real: P(0.15) =  ' , real )
print('Erro absoluto' , abs( real - interpolado) )
print('Erro relativo' , (abs( real - interpolado) / real) * 100 , '%')

print('-------------------')

x = np.array([ 0.1 , 0.2 , 0.3 ])
y = np.array([f(0.1) , f(0.2) , f(0.3)])

interpolado = Interpola( 0.15 , x , y , CalculaOrdens(x , y) )
real = f( 0.15 )

print('P(0.15): ' , interpolado)
print('Real: P(0.15) =  ' , real )
print('Erro absoluto' , abs( real - interpolado) )
print('Erro relativo' , (abs( real - interpolado) / real) * 100 , '%')

fim = time.clock()

print('Tempo: ' , fim - ini)