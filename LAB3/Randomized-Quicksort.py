#Randomized-Quicksort
import random

def Randomized-Quicksort(A=list, p=int, r=int):
	if p < r
		q = Randomized-Partition(A, p, r)
		Randomized-Quicksort(A, p, q-1)
		Randomized-Quicksort(A, q+1, r)

def Randomized-Partition(array A, int p, int r):
	i = Random(p, r)
	Intercambiar A[i] con A[r]
	return Partition(A, p, r)