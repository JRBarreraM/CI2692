# Lab-01. Busqueda lineal y binaria. Ordenamiento por insercion. Experimentos. Analisis de resultados.

# Integrantes:
# <Jose, Barrera y 15-10123>

# extender el limite de la profundidad del stack de recursion
from sys import setrecursionlimit
from sys import path
setrecursionlimit(int(1e6))
path.insert(0, '..')

# importar base
from common.base.basic import read_file
from common.base.test_lab_01 import test_search
from common.base.test_lab_01 import test_sort

from common.base.search import verifier_linear_search
from common.base.search import verifier_binary_search
from common.base.sort import native_sort
from common.base.sort import verifier_sort


########################################################################

def linear_search(A=str, x=str):
	for i in range(len(A)):
		if A[i]==x:
			return i
		i=i+1
	return -1

def binary_search(A=str, x=str):
	start = 0
	end = len(A) -1
	while start < end :
		mid = (start+end)/2
		if A[mid]==x:
			return mid
		elif x>A[mid]:
			start=mid+1
		elif x<A[mid]:
			end=mid-1

	if A[start]==x:
		return start
	return -1

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

########################################################################


# leer los datos y preparar variables para correr experimentos
data = read_file('./data/english.txt')
sizes = [ 2**i for i in range(16) ]
runs_per_each_size = 10
fractions = [ .5, .05, .005, .0005]
runs_per_each_size_and_fraction = 3

# imprimir encabezado de resultados
print 'type,name,size,i,time,verification'

# experimentos para algoritmos de busqueda en arreglos
test_search('linear', sizes, data, runs_per_each_size, linear_search, verifier_linear_search, False)
test_search('binary', sizes, data, runs_per_each_size, binary_search, verifier_binary_search, True)

# experimentos para algoritmos de ordenamiento
test_sort('native', sizes, fractions, data, runs_per_each_size_and_fraction, native_sort, verifier_sort)
test_sort('insertion', sizes[:-1], fractions, data, runs_per_each_size_and_fraction, insertion_sort, verifier_sort)