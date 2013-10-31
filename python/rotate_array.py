arr = [1,2,3,4,5]

def rotate(array, n):
	reverse(array, 0, n-1)
	reverse(array, n, len(array) - 1)
	reverse(array, 0, len(array) - 1)

def reverse(array, begin, end):
	i = begin
	j = end
	while(j >=i):
		temp = array[i]
		array[i] = array[j]
		array[j] = temp
		i += 1
		j -=1



