import sys

def min(numbers):
	m = numbers[0]
	index = 0
	for i in range(len(numbers)):
		if(numbers[i] < m):			
			index = i
			m = numbers[i]
	
	return index

def kway_merge(*lists):
	indexes = []
	for l in lists:
		indexes.append(0)

	result = []		
	tuple = []


	while(True):
		tuple = []
		#This loop gets the current position of every list
		#which is the minimum element that wasn't visited yet
		#if we used all elements of the list, consider that element as the maximum int
		for i in range(len(lists)):
			if(indexes[i] >= len(lists[i])):
				tuple.append(sys.maxint)
			else:
				tuple.append(lists[i][indexes[i]])
		
		#Here we find the minimum element among all of the minimuns from each list		
		minelement = min(tuple)

		#If we only have maxints on the tuple, we reached the end of every list
		if(tuple[minelement] == sys.maxint):
			break
		#This element is the next on the merged list
		result.append(lists[minelement][indexes[minelement]])
		indexes[minelement] +=1

	print result


	

kway_merge([1,2,3,4], [1,3,5,7], [2,4,6,8])
#print min([2,5,1,3])