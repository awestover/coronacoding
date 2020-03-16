---
title: Key 3
author: Alek and Max
---

# Problem 6
```python
import matplotlib.pyplot as plt
import numpy as np

def gcd(n,m):
  n,m = max(m,n), min(m,n)
  if n % m == 0:
    return m
  return gcd(n%m, m)

def lcm(n,m):
  return (n*m) // gcd(n,m)

n=100
data = [[lcm(i,j) for i in range(1,n)] for j in range(1,n)]
plt.imshow(data)
plt.show()

# nicer plot with seaborn
import seaborn as sns
sns.heatmap(data, cbar=False)
plt.show()

```
![gcd](gcd.png)
![lcm](lcm.png)


