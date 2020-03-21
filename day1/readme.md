---
title: day 1
author: Alek Westover
---

Thoughts from the author: 
The problems are sorted by difficulty within each section.
Some of these problems are pretty hard.
Work together! Ask Questions!

Pre-Lesson Homework: do the first 2 pythonprogramming.net tutorials.
Post-Lesson Homeowrk: do the next 2 tutorials. Do any of these problems that you thought were interesting.

pdf version of this tutorial: [day1.pdf](day1.pdf)

#Easy Stuff
Demo program: 
```python
  name = input()
  print("Hello "+ name)
```

# Problem 1
  Create a program that prints all even numbers up to your age.
  -From "Python for kids"

# Problem 2
  Create a program that asks someone for their name, and then compliments them.

# Problem 3
  Create a number guessing game. ("Im thinking of a number in [1,100]" User says "high and low", computer guesses numbers)


# Number Theory Stuff
Demo program: check if a number is a perfect square:
```python
  def checkIsSquare(n):
    i = 1
    while i*i <= n:
      if n == i*i:
        return True
      i+=1
    return False
```

# Problem 4
  Write a program to compute the $n$-th fibonacci number.
  Recall $f_0=f_1=1$, $f_n=f_{n-1}+ f_{n-2}$.

  Bonus: use linear algebra to do it in time $O(\log n)$

# Problem 5
  Write a program that makes an array with $x[i]$ indicating whether $i$ is prime or not.

# Problem 6
  Write a function that checks if a number is prime.

# Problem 7
  Write a program to compute the greatest common divisor of 
  two numbers.

  Hint: you can bash it, or do the euclidean algorithm


# Encryption Stuff
Demo: reverse cipher

```python
"".join([chr(26-(ord(x)%26)+ord('a')) for x in input_string])
```

# Problem 8
  Make a program that does a caesar cipher. That is, it takes in some english text, and cyclically shifts all the letters by some key, for example 1.


# Signal Stuff
Demo program: makes a graph of some noise.
```python
  import matplotlib.pyplot as plt
  import numpy as np
  data = np.random.rand(100)
  plt.plot(data)
  plt.show()
```

# Problem 9
  Print a thousand random numbers.

# Problem 10
  Generate a random signal with 1000 data points. Plot it. Make a smoothed version of the signal.

  Hint: use moving average




