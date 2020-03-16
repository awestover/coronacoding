
# numbers
n = 123412341234134
mod = 10**5

# ok, here is the "basic" solution:

def powmod2(n, mod):
    if n==1:
        return 2
    tmp = powmod2(n//2, mod)
    if n % 2 == 0:
        return (tmp*tmp)%mod
    else:
        return (((tmp*tmp)%mod)*2)%mod 

print(powmod2(n,mod))

# here is the troll solution
print(pow(2, n, mod))
# yeah thats right, its a built in function!

# here is a solution that is too cool for school. 
# so freaking pro

def v2(n):
    ct = 0
    while n % 2 == 0:
        n//= 2
        ct += 1
    return ct

ct = 0
running = 1
while running != 1<<v2(mod) or ct  <= v2(mod):
    running = (running<<1) % mod
    ct += 1

# note that 2**ct % mod == 2**v2(mod)

# so 2**n % mod = (2**ct)**(n//ct) * (2**(n%ct)) % mod

prod = 1
while n > 1:
    prod = (prod*powmod2(n%ct, mod))% mod
    n = (n//ct)*v2(mod)
print(prod)


