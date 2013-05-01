#Print all the numbers, in decimal, with n digits


def gen_string(s, n, k):
  if(len(s) == n):
    print s
  else:
    for x in range(k):
      gen_string(s+str(x),n, k)
  

gen_string("",3,3)
