count = 0

fibs = {}
def fib(n):
	try:
		return fibs[n]
	except: 
		global count
		count +=1
		if n==1 or n==2:
			return 1
		else:
			result = fib(n-1) + fib(n-2)
			fibs[n] = result
			return result






def fibLin(n):
	lastFib = 1
	currentFib = 1
	for i in range(1, n):
		tmp = currentFib
		currentFib = currentFib + lastFib
		lastFib = tmp
	return lastFib

def powerSet():
	array = ["a", "b", "c"]
	powerSet = []
	for i in range(2**len(array)):
		subset = []
		for j in range(len(array)):
			if(2**j & i):
				subset.append(array[j])
		powerSet.append(subset)

	print(powerSet)

def psetrecursive(a):
	if len(a) == 1:
		return [[], a]
	alek = psetrecurive(a[1:])
	powerset = []
	for i in alek:
		powerset.append(i)
		powerset.append(i+a[0])
	return powerset

def prob2(string1, string2):
	if(string1 == string2):
		return 0
	if(string1 == 0 or string2 ==0):
		return max(len(string1), len(string2))
	if(string1[0] == string2[0]):
		return prob2(string1[1:], string2[1:])
	return min(1+prob2(string1[1:],string2), 1+prob2(string1,string2[1:]), 1+prob2(string[1:],string[1:]))




print(prob2("alek", "alik"))



