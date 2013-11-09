'''
You have k lists of sorted integers. Find the size of the smallest range that includes at least one number from each of the k lists.

For example,
List 1: [4, 10, 15, 24, 26]
List 2: [0, 9, 12, 20]
List 3: [5, 18, 22, 30]

The smallest range here would be [20, 24] as it contains 24 from list 1, 20 from list 2, and 22 from list 3, the function should return 4.
'''
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
		for i in range(0,len(lists)):
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
		result.append((lists[minelement][indexes[minelement]],minelement))
		indexes[minelement] +=1
	
	return result

def is_valid(lst, indexes):
	if(len(lst) < len(indexes)):
		return False
	found = []
	for x in lst:
		if( not x[1] in found):
			found.append(x[1])
		if(len(found) == len(indexes)):
			return True
	return False

def range_of_list(lst, indexes):
	found = []
	if(is_valid(lst, indexes)):
		return lst[len(lst)-1][0] - lst[0][0]
	else:
		return sys.maxint

def find_min_range_recursive(lst, indexes):
	if(is_valid(lst, indexes)):		
		current_range = range_of_list(lst, indexes)		
		range_minus_first = find_min_range_recursive(lst[1:], indexes)		
		range_minus_last = find_min_range_recursive(lst[:len(lst) -1], indexes)

		ranges = [current_range, range_minus_last, range_minus_first]
		return ranges[min(ranges)]
	return sys.maxint



	
a = [4,10,15,24,26]
b = [0,9,12,20]
c = [5,18,22,30]
print find_min_range_recursive(kway_merge(a,b,c), [1,2,3])