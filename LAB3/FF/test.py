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

A=[50,50,305,20,45,32,2,7,86,5,2,5,6,58,7867]
quicksort_randomized(A)
B=A
quicksort(B)
print A
print B