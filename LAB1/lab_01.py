# Lab-01. Busqueda lineal y binaria. Ordenamiento por insercion. Experimentos. Analisis de resultados.

# Integrantes:
# <colocar nombre, apellido y carnet de cada integrante del grupo>

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

#def linear_search(A, x):


#def binary_search(A, x):


#def insertion_sort(A):


########################################################################


# leer los datos y preparar variables para correr experimentos
data = read_file('data/english.txt')
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

