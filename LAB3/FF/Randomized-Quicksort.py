#Randomized-Quicksort
import random

def Partition(A=list, p=int, r=int):
	Pivote = A[r]
	i = p -1
	k = p -1
	for j in range(p,r):
		if A[j] <= Pivote:		#Para cambiar de creciente a decreciente
			i = i + 1			#basta con cambiar el <= por >=
			A[i],A[j]=A[j],A[i]
		elif A[j] == Pivote:
			k = k + 1
			A[k],A[j]=A[j],A[k]
	A[i+1],A[r]=A[r],A[i+1]
	return i + 1,k+1

def Randomized_Partition(A=list, p=int, r=int):
	i = random.randint(p, r)
	A[i],A[r]=A[r],A[i]	
	return Partition(A, p, r)

def Randomized_Quicksort(A=list, p=int, r=int):
	if p < r :
		q1,q2 = Randomized_Partition(A, p, r)
		Randomized_Quicksort(A, p, q1-1)
		Randomized_Quicksort(A, q2+1, r)
	return A

#Test:
A=[(4,'Josue'),(4,'Jose'),(2,''),(1,''),(3,''),(4,'Jacinto')]
print(Randomized_Quicksort(A,0,len(A)-1))
print(Partition(A,0,len(A)-1))