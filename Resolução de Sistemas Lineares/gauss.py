import numpy as np 

def LU( A ):
	L = np.zeros( A.shape );
	U = np.zeros( A.shape );

	U[:] = A

	for i in range(L.shape[0]):
		L[i][i] = 1 

	for i in range( A.shape[0] - 1):
		for j in range( i + 1 , A.shape[1]):
			L[j][i] = U[j][i]/U[i][i]

			for k in range( i , A.shape[1]):
				U[j][k] = U[j][k] - L[j][i] * U[i][k]
	return (L,U)

def Resolvedor( L , U , B):
	#LUx = B
	
	#Ly = B

	y = np.zeros( (A.shape[0] , 1))
	x = np.zeros( (A.shape[0] , 1))

	for i in range( L.shape[0] ):
		soma = 0
		for j in range( i ):
			soma = soma + L[i][j] * y[j]

		y[i] = (B[i] - soma)/L[i][i]

	#Ux = y

	

	for i in range( L.shape[0] - 1 , -1 , -1 ):
		soma = 0
		for j in range(L.shape[0] - 1  , i - 1 , -1):
			soma = soma + U[i][j] * x[j]

		x[i] = ( y[i] - soma)/U[i][i]


	return (y, x)





A = np.array([[ 1,  2, 4],
       		[ 3,  8,  14],
       		[2,  6,  13]])

(L,U) = LU( A )

print('Matriz L:')
print( L )
print('Matriz U:')
print( U )
print('Matriz B: ')
B = np.array( [[3] , [13] , [4]])
print( B )

(y , x) = Resolvedor( L , U , B)

print('Matriz Y: ')

print( y )

print('Matriz X: ')

print( x )
