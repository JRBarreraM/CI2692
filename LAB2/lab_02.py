# Lab-01. Busqueda lineal y binaria. Ordenamiento por insercion. Experimentos. Analisis de resultados.

# Integrantes:
# <Jose, Barrera y 15-10123>
# <Alfredo, Cruz y 14-10261>

# extender el limite de la profundidad del stack de recursion
from sys import setrecursionlimit
from sys import path
setrecursionlimit(int(1e6))
path.insert(0, '..')

# importar base
from common.base.basic import read_file
from common.base.basic import Random
from common.base.test_lab_01 import test_sort
from common.base.test_lab_02 import test_freivalds
from common.base.test_lab_02 import test_amplified_freivalds
from common.base.test_lab_02 import test_problema_3_8

from common.base.sort import native_sort
from common.base.sort import verifier_sort
from common.base.problema_3_8 import verifier_problema_3_8

########################################################################

def insertion_sort(A):
	start=0
	end=len(A)
	for j in range(end):
		key = A[j]
		i = j - 1
		while i >= start and A[i] > key :
			A[i+1] = A[i]
			i = i - 1
		A[i+1] = key
	return A

def merge(A, p, r, q):
    n1 = r - p + 1
    n2 = q- r
 
    L = [0] * (n1)
    R = [0] * (n2)
 
    for i in range(0 , n1):
        L[i] = A[p + i]
 
    for j in range(0 , n2):
        R[j] = A[r + 1 + j]
 
    i = 0
    j = 0
    k = p
 
    while i < n1 and j < n2 :
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        A[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        A[k] = R[j]
        j += 1
        k += 1
 

def aux_mergesort(A,p,q):			# Esta funcion auxiliar es necesaria para que el merge
    if p < q:						# no use centinelas y se mantengan las firmas de las
        r = int((p+(q-1))/2)		# subrutinas tal y como se pidieron, ademas no afecta
        aux_mergesort(A, p, r)		# el tiempo de ejecucion del algoritmo.
        aux_mergesort(A, r+1, q)
        merge(A, p, r, q)

def mergesort(A):
	aux_mergesort(A,0,len(A)-1)
	return A			

def multiply(N, A, Z):
	ZZ= N*[0]
	for I in range(N):
		for J in range(N):
			ZZ[I]=ZZ[I]+(A[I][J]*Z[J])
	return ZZ

def freivalds(N, A, B, C):
	Z = N*[0]				# vector fila de ceros
	for I in range(N):
		Z[I] = Random(0,1)	# construimos vector aleatorio
	Y=multiply(N,B,Z)
	X1 = multiply(N,A,Y)
	X2 = multiply(N,C,Z)
	return X1 == X2 

def amplified_freivalds(k, n, A, B, C):
    for i in range(k):
        r = freivalds(n, A, B, C)
        if r == False:
            return False
    return True

def check_if_exist(A=str, x=str): #es un binary_search con un cambio en el output
	start = 0						# pues no nos interesa el numero, solo si existe.
	end = len(A) -1
	while start < end :
		mid = (start+end)/2
		if A[mid]==x:
			return True
		elif x>A[mid]:
			start=mid+1
		elif x<A[mid]:
			end=mid-1
	if A[start]==x:
		return True
	return False

def problema_3_8(A, x):	# problema_3_8, es O(nlog(n)) en el peor de las casos,
	mergesort(A)		# pues mergesort es O(nlog(n)) y binary_search es O(log(n)),
	N=len(A)			# ya que aplicamos binary_search a lo sumo n veces,
	for I in range(N):  # el tiempo de corrida en el peor caso es n(log(n)),
		KEY=x-A[I]		# por lo que todo el programa toma 2(nlog(n)).
		if check_if_exist(A,KEY):
			return True
	return False

########################################################################


# leer los datos y preparar variables para correr experimentos
data = read_file('data/web2')
sizes = [ 2**i for i in range(16) ]
fractions = [ .5, .05, .005, .0005]
runs_for_each_size = 50
runs_for_each_size_and_fraction = 3
amplification = 20

# imprimir encabezado de resultados
print 'type,name,size,i,time,verification'

# experimentos para algoritmos de ordenamiento
test_sort('nativo', sizes, fractions, data, runs_for_each_size_and_fraction, native_sort, verifier_sort)
test_sort('insertion', sizes[:-1], fractions, data, runs_for_each_size_and_fraction, insertion_sort, verifier_sort)
test_sort('mergesort', sizes, fractions, data, runs_for_each_size_and_fraction, mergesort, verifier_sort)

# experimentos para freivalds
test_freivalds("freivalds", [ 2, 4, 8, 16, 32, 64, 128 ], 0, 30, runs_for_each_size, freivalds)
test_amplified_freivalds("amplified-freivalds", [ 2, 4, 8, 16, 32, 64, 128 ], 0, 30, runs_for_each_size, amplified_freivalds, 50)

# preparar datos para problema 3.8
test_problema_3_8("problema-3-8", [ 2**i for i in [ 4, 6, 8, 10, 12, 14, 16 ] ], 100, 10000, runs_for_each_size, problema_3_8, verifier_problema_3_8)