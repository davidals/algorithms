def adding_number_in_base_minus_2 ( A,B ):
 #Revert to add from the least significant to the most
 revA = A[::-1]
 revB = B[::-1]
 result = []
 i = 0
 n = 0
 carry = 0
 #iterate on the digits
 while(True):
  #Attention to this first if
  if(i >= len(A) and i >= len(B) and carry == 0):
   break
  #Do the actual sum
  if(i < len(A) and i < len(B)):
   n = revA[i] + revB[i] + carry
  elif(i < len(A)):
   n = revA[i] + carry
  elif(i < len(B)):
   n = revB[i] + carry
  else:
   n = carry
   
  #This derives from the table 
  if(n % 2 == 0):
   result.append(0)
  else:
   result.append(1)
 
  if(n < 0):
   carry = 1
  elif(n > 1):
   carry = -1
  else:
   carry = 0 
 
  i = i + 1
 return result[::-1]