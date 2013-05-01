#Print all the numbers, in binary, with at most N bits.

def gen_string_bits(s, n):
  if(len(s) == n):
    print s
  else:
    gen_string_bits(s+"0",n)
    gen_string_bits(s+"1",n)

gen_string_bits("",3)
