---
title: Key 5
author: Joy, Leon, Alek
---

# Problem 0 (Solution by Joy, and Alek)

First we make a really simple, and really slow recursive solution to fib
```python
def fib(n):
  if n == 1 or n == 2:
    return 1
  return fib(n-1)+fib(n-2)
```
This is super slow. Its running time is $2^{O(n)}$ (exponential). More specifically, its running time is `O(fib(n))`.

Recall that we can solve it really easily in linear time:

```python
def fibLin(n):
	lastFib = 1
	currentFib = 1
	for i in range(1, n):
		tmp = currentFib
		currentFib = currentFib + lastFib
		lastFib = tmp
	return lastFib
```

But the recursive version is nice and simple. So let's save it! 
We save it by **memoization**, storing previously computed answers. 


```python
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

```
Now it is once again linear runtime!


# Problem 1 (solution by Joy)

First we solve it with bit arithmetic. Note that we can think of a subset as a
binary string, where the $j$-th digit of the binary string is a boolean variable that indicates
whether the $j$-th element of the list is included in the subset.
We can simply enumerate all $n$ digit binary strings and generate the corresponding subsets:

```python
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
```
Bit arithmetic is super cool. Here are some key opperators

- `&` and, e.g. `1&0 = 0`
- `|` or, e.g. `1|0 = 1`
- `^` xor, e.g. `1^0 = 1`
- `<<` bit shift, e.g. `1<<5 = 32`
- `>>` bit shift, e.g. `8>>1 = 4`
- `~` not, e.g. `~3 & 7 = 4`

bit arithmetic is super fast.

Some useful functions in python related to bit arithmetic:
- `bin` binary representation of a number
- `hex` hexideciaml representation of a number

We can also solve it recursively, it's pretty simple too:
```python
def psetrecursive(a):
	if len(a) == 1:
		return [[], a]
	alek = psetrecurive(a[1:])
	powerset = []
	for i in alek:
		powerset.append(i)
		powerset.append(i+a[0])
	return powerset
```

# Problem something (dynamic programming edit distance)
```python
def prob2(string1, string2):
	if(string1 == string2):
		return 0
	if(string1 == 0 or string2 ==0):
		return max(len(string1), len(string2))
	if(string1[0] == string2[0]):
		return prob2(string1[1:], string2[1:])
	return min(1+prob2(string1[1:],string2), 1+prob2(string1,string2[1:]), 1+prob2(string[1:],string[1:]))

print(prob2("alek", "alik")) # 1
```



