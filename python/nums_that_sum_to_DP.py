def nums_that_sum_to(target, nums):
	nums.sort()
	matrix = []
		
	for i in range(target + 1):
		matrix.append([])
		for j in range(len(nums)):
			matrix[i].append(-1)

	#row = target
	#column = numbers

	#init first column 1 with ones, since to reach 1 we need only the number 1
	for i in range(target + 1):
		matrix[i][0] = 1
	#init first row with zeros, since to reach 0 we need 0 numbers
	for i in range(len(nums)):
		matrix[0][i] = 0
	
	#if one of the numbers is one, the first column will always be 1, since for N you can put N ones
	

	for i in range(len(matrix)):

		for j in range(1,len(matrix[i])):
			matrix[i][j] = 0

			#If the target value is the number, than it surely has at least one way. 
			#Using Only this number
			if(i == nums[j]):
				matrix[i][j] += 1
			#If the target value is greater, than it can be done the same ways as
			#without this number plus using this number and all the ways that
			#target - number can be found.
			if(i > nums[j]):				
				matrix[i][j] += matrix[i][j-1]
				matrix[i][j] += matrix[ i - nums[j] ] [j]
			#Finally, if this number is greater than the target, we won't use it anyway.
			else:
				matrix[i][j] += matrix[i][j-1]

	print matrix[target][len(nums)-1]
	

'''            coins
target  | 1 | 2 | 5 | 10 |
      0 | 0 | 0 | 0 |  0 |
      1 | 1 | 1 | 1 |  1 |
      2 | 1 | 2 | 2 |  2 |
      3 | 1 | 2 | 2 |  2 |
      4 | 1 | 3 | 3 |  3 |
      5 | 1 | 3 | 4 |  4 |
      6 | 1 | 4 | 5 |  5 |
      7 | 1 | 4 | 6 |  6 |
      8 | 1 | 5 | 7 |  7 |
      9 | 1 | 5 | 8 |  8 |
     10 | 1 | 6 | 10|  11|
'''


nums_that_sum_to(10,[1,2,5,10])		
