#Randomized-Quicksort
import random

def Partition(A=list, p=int, r=int):
	Pivote = A[r]
	i = p - 1
	for j in range(p,r):
		if A[j] <= Pivote:
			i = i + 1
			A[i],A[j]=A[j],A[i]
	A[i+1],A[r]=A[r],A[i+1]
	return i + 1

def Randomized_Partition(A=list, p=int, r=int):
	i = random.randint(p, r)
	A[i],A[r]=A[r],A[i]	
	return Partition(A, p, r)

def Randomized_Quicksort(A=list, p=int, r=int):
	if p < r :
		q = Randomized_Partition(A, p, r)
		Randomized_Quicksort(A, p, q-1)
		Randomized_Quicksort(A, q+1, r)
	return A

#Test:
A=[1,3,4,5,5,3,5,8,99]
print(Randomized_Quicksort(A,0,len(A)-1))