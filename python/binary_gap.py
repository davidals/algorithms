#A binary gap is the largest amount of consecutive 0s on a binary number.
def binary_gap ( N ):
  b = bin(N)
  b =  b[2:] #Take away the 0b from string
  b = b.rstrip('0') #If ends on 0 all 0s before doesn`t form a gap
  gaps = b.split('1') #Takes all gaps
  maxGap = 0
  for gap in gaps:
     maxGap = len(gap) if len(gap) > maxGap else maxGap #Find max Gap
  return maxGap


