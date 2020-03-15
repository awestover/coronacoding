def isPrime(x):
  if x==1:
    return False
  if x==2:
    return True
  i = 1
  while i*i < x:
    i += 1
    if x%i == 0:
      return False
  return True

for i in range(1,100):
  print(i, isPrime(i))
