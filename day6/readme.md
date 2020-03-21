---
author: Alek Westover
title: tick tack toe
---

# Problem 1
Make a representation of a tick tack toe board on the computer, and make a function that can nicely print the current board state

# Problem 1.23
Write a function that can determine the "state" of a board. i.e. is it a 
- X win state
- O win state
- tie state
- game in progress state

# Problem 1.5
Make it so that two humans can play tick tack toe against one another with your program showing the board in between their moves, and asking them to input their moves.

# Problem 2
Hard code some logic for a tick tack toe bot. e.g. go in the center first

# Problem 3
Make some smarter logic 
- e.g. If there are 2 X's in a row and the last square in the row is onoccupied (or more generally if any winning move is available) take it
- e.g. block winning moves for the opponent

# Problem 3.5 (SUPER DUPER COOL)
A genetic agent has some DNA, i.e. a set of instructions for how to act. In the context of tick tack toe this could mean the DNA is a lookup table for what moves to perform, i.e. if the board is empty go in the center.
To train a good genetic agent, repeat the following for many generations:
- Create a lot of genetic agents and play them against each other
- Take the algorithms that win the most, "survival of the fittest": these algorithms survive to the next round
- These algorithms should also have progeny
- To generate progeny you basically should probably just create kids with DNA that is slightly mutated from their parents
- good mutations should stay in the population and predominate over time
- If you made a decent bot with hard coded logic then playing the genetic algorithms against that could also help them improve

See if your genetic agent is any good.

# Problem 4
Upgrade it to be 5 by 5 tick tack toe, or bigger.



