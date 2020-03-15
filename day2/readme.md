# Corona Coding Club Day 2 
## Alek and Max

# EZ warmup problems

**Example:**
```python
def double_loop_loop(n):
  for i in range(2*n):
    for j in range(i+1, 2*n):
      print(i, j)
double_loop_loop(4)
```

## Problem 1
> Make a function that can count how many the word "like" occurs in a sentece you input, and also in the following sentence (case insensitive, i.e. capitalized counts):
> "Like it's really easy, like dude what're you like doing like what is this question, like this seems dumb like; oh man liken this tutorial unto yourselves like get scammed like wow like like like like ziyong is a pro yah like know?"

## Problem 1.5
> Make a function that can print out every other word in a string that you input, and also in the sentence from the previous problem.

## Problem 2
> Make a function that finds the element whose square is biggest in a list (break ties by which one occurs first in the list). e.g. `biggestSquare([0,0,0,0]) = 0; biggestSquare([0,1,0,0]) = 1, biggestSquare([0,1,-2,0]) = -2, biggestSquare([1,2,3,4,-4]) = 4`

## Problem 3
> Make a function that gives a random coronavirus related tip (from a list of coronavirus related tips)


# Number Theory

## Problem -1
> Write a program that outputs for each $i, j \in \{1,2,\ldots, n\}$ computes whether $i$ and $j$ are relatively prime (whether they have any common factors) and stores it in a 2d matrix.

**Definition:**
Modular arithmetic.
Consider a clock. The time is some number in $[0,12]$ as represented by clock
hands. If you are at time $x$, and you wait for $5$ hours, you are either at
time $x+5$, or time $x+5-12$, because in "clock arithmetic" the numbers wrap once 
you pass $12$. For example, in clock arithmetic $7+7 = 2$ (7 hours after 7pm it is 2am).

The `mod` opperator is very useful for a lot of reasons, which you will soon see.
It is defined as $x \% m = x - km$ where $k$ is an integer chosen so that $x-km \in [0,m)$.
Basically, you just subtract the mod off of the number until you lie in the right range, exactly like with the clock.

**Example:**
```python
zodiac_animals = ["Rat", "Ox", "Tiger", "Rabbit", "Dragon", "Snake", "Horse", "Goat", "Monkey", "Rooster", "Dog", "Pig"]
print("hey, want to know your zodiac animal! I can tell you.")
age = int(input("How old are you?"))
print("Your zodiac animal is" + zodiac_animals[age%12])
```

## Problem 0.5 *(VERY COOL)*
> Approximate $\pi$ with the following method:
> Draw a bunch of points uniformly at random from the unit square  (using `np.random.rand`)
> Calculate what fraction are in the unit circle too (satisfy $x^2 + y^2 \le 1$). This fraction approahces $\pi/4$ if you take more and more points.


## Problem 0 *(VERY COOL)*
> There is a game called "FLIP FLOP". $n$ people sit in a circle. They take turns saying numbers in ascending order. 
> Max says "1", Alek says "2", Justin says 3, Madeline says 4, David says 5, Ziyong says 6, and then Leon is like "FLIP!!!"
> (on any multiple of $7$ the person says FLIP instead of saying the number. When they say FLIP the direction around the circle changes)
> Then Ziyong says "FLOP!!!!"
> (on any multiple of $8$ the person says FLOP instead of saying the number. When they say FLOP a person is skipped in the current direction)
> Then David is sad because he was skipped.
> Madeline says 9
> Justin says 10
> Alek says 11
> Max says 12
> Melina says 13
> Ethan says FLIP
> Melina says 15
> Max says FLOP
> Alek feels left out
> Justin says 17
> etc


> Now here is the question, lets say there are 100 people in the circle.
> Bob is 50 seats clockwise of Max
> Does he ever get a chance to play?
> SIMULATE IT!
> once you are done, you can check against my simulation: [aleks flipflop](http://flipflop.surge.sh/)


## Problem 1 *(VERY COOL)*

> Write a program that computes the last 5 digits of $2^{123412341234134}$

> Note: if you try to make python compute $2^{123412341234134}$ it will blow up, this is a ridiculously big number
> Instead of doing that, use the following mathematical fact (that you should verify!)  `(a * b)% m = (a%m * b%m)% m`
> Also note, that the number is big, so even a for loop will take a while!
> Hint: "Exponentiation by squaring"
> You could also probably find a pattern, stuff repeats in modular arithmetic




