#http://codeforces.com/contest/349/problem/A
def give_change(bills, v):
	value = v	
	for x in sorted(bills.keys(), reverse=True):
		while(value >= x and bills[x] > 0):
			value = value - x			
			bills[x] = bills[x] -1			
	
	return value == 0


n = int(raw_input())
bills = [ int(x) for x in raw_input().split(' ')]
available_cash = {25:0, 50:0, 100:0}

result = True;
for p in bills:
	if(not give_change(available_cash, p - 25)):
		result = False;
	available_cash[p] = available_cash[p] + 1
	
if(result):
	print "YES"
else:
	print "NO"
