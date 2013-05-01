"""A zero-indexed array A consisting of N integers is given. A triplet (P, Q, R) is triangular if 0 ≤ P < Q < R < N and

·   A[P] + A[Q] > A[R],
·   A[Q] + A[R] > A[P],
·   A[R] + A[P] > A[Q].

Given an array find out if any of its triplets is triangular
"""
def triangle ( A ):
    sortedArr = sorted(A)
    for i in range(1,len(sortedArr)):
      if i+1 < len(sortedArr) :
        if sortedArr[i] + sortedArr[i-1]  > sortedArr[i+1] :
          return 1
    return 0
    
    
print triangle([1, 2, 5, 8, 10, 20])
