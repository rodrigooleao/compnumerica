import numpy as np 

def CalculaOrdens( x , y ):
	ord = np.zeros( (x.shape[0] , x.shape[0]))
	ord [0] = y

	for i in range( 1 , x.shape[0]):
		for j in range( 0, (x.shape[0] - i) ):
			ord[i][j] = ( ord[i-1][j+1] - ord[i-1][j])/( x[j + i]- x[j])


	#print( ord )
	return ord

def Interpola( xalvo , x , y , mat):
	soma = mat[0][0]
	prod = 1

	for i in range( 1 , x.shape[0]):
		prod = mat[i][0]

		for j in range( i ):
			prod *= ( xalvo - x[j])
			

		soma += prod


	return soma;
	

x = np.array([0.0, 0.2, 0.3, 0.5, 0.6])
y = np.array([1.008, 1.064 , 1.125, 1.343 , 1.512])

result = Interpola( 0.2 , x , y , CalculaOrdens(x , y) )
print('Resultado: ' , result)