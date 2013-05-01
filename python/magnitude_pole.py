#A zero-indexed array A consisting of N integers is given. A magnitude pole of this array is an integer Q such that:
#0 ≤ Q < N;
#A[P] ≤ A[Q] for 0 ≤ P < Q;
#A[Q] ≤ A[R] for Q < R < N.
#For example, consider array A consisting of ten elements such that:
#A[0] = 4  A[1] = 2  A[2] = 2
#A[3] = 3  A[4] = 1  A[5] = 4
#A[6] = 7  A[7] = 8  A[8] = 6
#A[9] = 9
#Number 5 is a magnitude pole of this array, because all elements to the left of A[5] have values smaller than or equal to A[5] (4, 2, 2, 3 and 1 are smaller than or equal to 4) and all elements to the right of A[5] have values greater than or equal to A[5] (7, 8, 6 and 9 are greater than or equal to 4). Number 9 is also a magnitude pole of this array.
#Write a function:
#def magnitudePole(A)
#that, given a zero-indexed array A consisting of N integers, returns any of its magnitude poles. The function should return −1 if array A does not have a magnitude pole.

def checkLeft(N,A,i):
	for j in A[:i]:
		if j > N:
			return False
	return True

def checkRight(N,A,i):
	for j in A[i:]:
		if j < N:
			return False
	return True

def magnitudePole ( A ):
    for i in range(len(A)):
    	if( checkLeft(A[i],A,i) and checkRight(A[i],A,i)):
    		return A[i]
    return -1

def max_on_left(A):
	if(len(A) == 0 ):
		return []

	result = [A[0]]
	for i in range(1,len(A)):
		if(A[i] > result[-1]):
			result.append(A[i])
		else:
			result.append(result[-1])
	return result

def min_on_right(A):
	if(len(A) == 0 ):
		return []
		
	result = [A[-1]]
	for i in reversed(range(len(A)-1)):
		if(A[i] < result[0]):
			result.insert(0,A[i])
		else:
			result.insert(0,result[0])
	return result

def magnitudePole2 ( A ):		
	maxs = max_on_left(A)
	mins = min_on_right(A)	
	
	for i in range(len(A)):	
		if(A[i] >= maxs[i] and A[i] <= mins[i]):
			return A[i]

	return -1


print magnitudePole([4,2,2,3,1,4,7,8,6,9])
print magnitudePole([1,2,3,4,5,6,7,8,9])
print magnitudePole([5,4,3,2,1])
print magnitudePole([3,2,5,1,4,6,9,10,8,7,6])
print magnitudePole([])

print "-------------"
print magnitudePole2([4,2,2,3,1,4,7,8,6,9])
print magnitudePole2([1,2,3,4,5,6,7,8,9])
print magnitudePole2([5,4,3,2,1])
print magnitudePole2([3,2,5,1,4,6,9,10,8,7,6])
print magnitudePole2([])