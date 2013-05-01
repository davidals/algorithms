def nums_that_sum_to(N, nums):
 nums.sort()
 result = []
 i = 0;
 recur(N,0,nums,result)
 
def recur(N, sum, nums, result):
 if(sum == N):
  print result
 
 elif(sum > N): 
  return
 
 else:
  for x in nums:
   result.append(x)
   recur(N, sum + x, nums, result)
   result.pop(len(result)-1)