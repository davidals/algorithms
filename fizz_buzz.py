import sys

def divisible(a,b):
    return a % b == 0
 
def fizzbuzz(num,a,b):    
    if(divisible(num,a) and divisible(num,b)):
        return "FB"
    elif(divisible(num,a)):
        return "F"
    elif(divisible(num,b)):
        return "B"
    else:
        return str(num)
            
test_cases = open(sys.argv[1], 'r')
 
for test in test_cases:
    
    split = test.split()
    a = int(split[0])
    b = int(split[1])
    n = int(split[2])
    
    print ' '.join([fizzbuzz(num,a,b) for num in range(1,n+1)])   
   

test_cases.close()