# Lab-03.

# Integrantes:
# <Jose, Barrera y 15-10123>

# extender el limite de la profundidad del stack de recursion
from sys import setrecursionlimit
from sys import path
setrecursionlimit(int(1e6))
path.insert(0, '..')

# importar base
from common.base.basic import read_file
from common.base.basic import Random
from common.base.test_lab_01 import test_sort

from common.base.sort import native_sort
from common.base.sort import _mergesort as mergesort
from common.base.sort import verifier_sort



########################################################################

#### HEAPSORT

# aplica heapsort al arrego A
def heapsort(A):
    heapsort_aux(A, 0, len(A) - 1)

# aplica heapsort al arrego A[p...r]
def heapsort_aux(A, p, r):

    # Build a maxheap.
    build_max_heap(A,p,r)
 
    for i in range(r, 0, -1):
        A[i], A[0] = A[0], A[i]
        max_heapify(A,0,p,i)

# aplica max-heapify en nodo i del arreglo A[p..r]
def max_heapify(A, i, p, r):

    left = heap_left(i,p,r)
    right = heap_right(i,p,r)
    largest=i
    
    if left < r and A[left] > A[i]:
        largest=left
    
    if right < r and A[right] > A[largest]:
        largest=right
    
    if largest != i:
        A[i],A[largest]=A[largest],A[i]
        max_heapify(A,largest,p,r)

# construye un max-heap en el arreglo A[p...r]
def build_max_heap(A, p, r):
    for i in range(r+1, -1, -1):
        max_heapify(A,i,p,r+1)

# retorna el indice del hijo izquierdo del nodo i en el heap [p...r]
def heap_left(i, p, r):

    index = i - p + 1
    left_child = 2 * index
    return p + left_child - 1

# retorna el indice del hijo derecho del nodo i en el heap [p...r]
def heap_right(i, p, r):

    index = i - p + 1
    right_child = 2 * index + 1
    return p + right_child - 1

#### QUICKSORT

# aplica quicksort al arreglo A
def quicksort(A):
    quicksort_rec(A, 0, len(A) - 1, partition)

# aplica quicksort randomizado al arreglo A
def quicksort_randomized(A):
    quicksort_rec(A, 0, len(A) - 1, partition_randomized)

# funcion de particion para quicksort deterministico sobre el arreglo A[p...r]
def partition(A, p, r):
    pivot = A[r]
    return partition_with_pivot(A, p, r, pivot)

# funcion de particion para quicksort randomizado sobre el arreglo A[p...r]
def partition_randomized(A, p, r):
    pivot_index = Random(p, r)
    pivot = A[pivot_index]
    A[pivot_index],A[r] = A[r], A[pivot_index]
    return partition_with_pivot(A, p, r, pivot)

# aplica quicksort con funcion de particion dada al arreglo A[p...r]
def quicksort_rec(A, p, r, partition_function):
    if p < r :
        l,m = partition_function(A,p,r)
        quicksort_rec(A, p, l,partition_function)
        quicksort_rec(A, m, r,partition_function)


# funcion de particion con pivote dado. El ultimo elemento en el
# arreglo es igual al pivote. La funcion retorna dos indices l,m
# tales que:
#   *  A[i] < pivot para p <= i < l
#   *  A[i] == pivot para l <= i <= m
#   *  A[i] > pivot para m < i <= r
#
# La funcion es simiular a la vista en clase excepto que para el lazo
# principal hay tres indices i, j, k tales que el siguiente invariante
# se mantiene:
#   * elementos A[p], A[p+1], ..., A[i] son < pivot
#   * elementos A[i+1], A[i+2], ..., A[j-1] son > pivot
#   * elementos A[j], A[j+1], ..., A[k-1] son "desconocidos"
#   * elementos A[k], A[k+1], ..., A[r] son == pivot
#
# Inicialmente, i = p-1, j = p, y k = r. El procedimiento tiene un 
# lazo principlan y corre en tiempo linear.
#
# Una vez que el lazo principal termina, se deben mover los elementos
# A[k], A[k+1], ..., A[r] que son iguales al pivote al "medio" del 
# arreglo en las posiciones A[l], A[l+1], ..., A[m]
def partition_with_pivot(A, p, r, pivot):
    i = p-1
    j = p
    k = r
    while j<k:
        if A[j] < pivot:
            i = i + 1
            A[i],A[j]=A[j],A[i]
            j+=1
        elif A[j] == pivot:
            k = k - 1
            A[k],A[j]=A[j],A[k]
        elif A[j] > pivot:
            j+=1
    for o in range(r-k+1):
        A[k+o],A[i+1+o]=A[i+1+o],A[k+o]
    l,m=i,i+r-k+1
    return l,m
# Para retornar los indices l,m en la funcion partition_with_pivot, 
# utilice 'return l, m'

# Para recibir los indices l,m en la llama da partition_function en la
# funcion quicksort_rec, utilice 'l, m = partition_function(A, p, r)'


########################################################################


# leer los datos y preparar variables para correr experimentos
data = read_file('data/web2')
sizes = [ 2**i for i in range(16) ]
fractions = [ .5, .05, .005, .0005]
runs_for_each_size_and_fraction = 10

# imprimir encabezado de resultados
print 'type,name,size,i,time,verification'

# experimentos para algoritmos de ordenamiento
test_sort('nativo', sizes, fractions, data, runs_for_each_size_and_fraction, native_sort, verifier_sort)
test_sort('mergesort', sizes, fractions, data, runs_for_each_size_and_fraction, mergesort, verifier_sort)
test_sort('heapsort', sizes, fractions, data, runs_for_each_size_and_fraction, heapsort, verifier_sort)
test_sort('quicksort', sizes, fractions, data, runs_for_each_size_and_fraction, quicksort, verifier_sort)
test_sort('quicksort-randomizado', sizes, fractions, data, runs_for_each_size_and_fraction, quicksort_randomized, verifier_sort)

