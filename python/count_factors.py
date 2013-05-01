#Count factors of a number
import math
def count_factors ( N ):
  count = 0;
  for x in range(1, int(math.sqrt(N)) + 1):
    if N % x == 0:
      count = count + 2
  return count

print count_factors(24)
