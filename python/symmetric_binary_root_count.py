#An integer obtained by reversing the bits of a given integer A is denoted as bit-rev(A). For example, bit-rev(25) = 19, because the binary representation of 25 is 11001, and reversing those bits yields 10011, i.e. 19. Similarly, bit-rev(26) = 11 and bit-rev(11) = 13.
#A symmetric binary root of a given positive integer N is a positive integer A such that N = A * bit-rev(A). For example, the symmetric binary root of 50 is 10, because 10 * bit-rev(10) = 10 * 5 = 50. Note that 5 is not a symmetric binary root of 50. The number 286 has two symmetric binary roots: 22 and 26.
#Write a function:
#def symmetric_binary_root_count(N)
#that, given a positive integer N, returns the smallest symmetric binary root of N. The function should return −1 if N has no symmetric binary root.
#For example, given N = 3245 the function should return 55.


import math
def bit_rev(A):
    a_bin = bin(A)[2:]
    return int(''.join(reversed(a_bin)),2)

def symmetric_binary_root_count ( N ) :
    ret = -1
    for i in range(1,int(math.floor(math.sqrt(N)))):
        if(N % i == 0):
            q = int(N / i)
            if bit_rev(i) == q:
                return i
            elif bit_rev(q) == i:
                ret = q if ret == -1 else min(ret,q)
    return ret


print bit_rev(25)
print bit_rev(19)
print bit_rev(26)
print bit_rev(11)

print bit_rev(55)
print bit_rev(50)
print bit_rev(10)
print bit_rev(3245)

print "symmetric_binary_root_count"
print symmetric_binary_root_count(50)
print symmetric_binary_root_count(286)
print symmetric_binary_root_count(3245)


