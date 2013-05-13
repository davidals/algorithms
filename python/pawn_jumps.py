# coding: utf-8
'''
A non-empty zero-indexed array A consisting of N integers is given. Each element of the array can be treated as a relative pointer to another element in the array: if A[K] = M then element A[K] points to element A[K+M].
The array defines a sequence of jumps of a pawn as follows:
initially, the pawn is located at element A[0];
on each jump the pawn moves from its current element to the destination element pointed to by the current element; i.e. if the pawn stands on element A[K] then it jumps to the element pointed to by A[K];
the pawn may jump forever or may jump out of the array.

Write a function:
def solution(A)
that, given a non-empty zero-indexed array A consisting of N integers, returns the number of jumps after which the pawn will jump out of the array. The function should return −1 if the pawn will never jump out of the array.
'''

def pawn_jumps(A):
	visited = { }
	pos = 0
	count = 0
	while(1):		
		visited[pos] = True		
		if(pos >= len(A)):		
			return count
		pos = pos + A[pos]		
		if(pos in visited):
			return -1		

		count += 1

		

print pawn_jumps([2,3,-1,1,3])
print pawn_jumps([1,1,-1,1])
print pawn_jumps([1,1,1,1,1])