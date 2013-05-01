#Given an array of N numbers, implement a function which returns the amount of absolute distinct numbers.
#So, if an array contains 3 and -3 they should count only as one element.
def absDistinct ( A ):
  count = {}
  for i in A:
    if abs(i) in count:
      count[ abs(i)] = count[i] + 1
    else:
      count[ abs(i)] = 1
  
  return len(count.keys()) 