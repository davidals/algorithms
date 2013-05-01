#Find the least element on a rotated list
import math

def find_least(lst, low, hi):
  
  if(hi == low):
    return hi
    
  if(hi == low +1):
    if (lst[hi] < lst[low]):
      return hi
    else:
      return low
      
  mid = int(math.floor((hi + low) / 2))
  if (lst[hi] < lst[low]):
    return find_least(lst, mid, hi) 
  else:
    return find_least(lst, low, mid)
    
mid = int(math.floor((0 + 4) / 2))
print find_least([3,4,5,1,2],0,4)
print find_least([3,4,5,6,1,2],0,5)
print find_least([3,4,5,6,7,1,2],0,6)
print find_least([2,3,4,5,6,7,1],0,6)
print find_least([1,2,3,4,5,6,7],0,6)
