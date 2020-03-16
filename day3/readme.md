# Corona Coding Club Day 3 Data Science

# Pre-probelm lesson:

### IO
First, import the following really important libraries:
```python
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
```

If you get import errors when you try importing them, install pip:
(https://pythonprogramming.net/using-pip-install-for-python-modules/) and type
`pip install matplotlib` and `pip install numpy` into your terminal

Today we are going to be learning how to do input/output with data, and how to visualize data.

For basic input/output (IO) you can use the `with` function in `python`:
```python
with open("data.txt", "r") as f:
  for line in f:
    print(line)
```

The `r` parameter in the `open` function is **VERY** important. It can have a couple different values

  - `r`: read mode
  - `w`: write mode
  - `wa`: append write mode
  - `r+`: read and write mode

One really important thing to know is that opening a file with `w` will
*overwrite its contents*. You won't be able to get them back! So don't do that.
`w` mode is for creating new files with a program.

For reading in special file types like `csv`s, `xml`s, `json`s, `xlsx`s, which have computer readable data, you will want to use a different function to read the file.
`pandas` is great for IO with tables. For example,
```python
import pandas as pd
pd.read_csv("data.csv")

df = pd.DataFrame({"alek tennis score": [1,2,3,4], "max tennis score":[5,56,7,7]})
df.to_csv("tennis.csv")
```

`json` is great for `json` files:
```python
import json

with open("data.json", "r") as f:
  json.load(f)


with open("data.json", "w") as f:
  json.dump(data, f)
```

`BeautifulSoup` is super helpful for parsing `html` and `xml`.

## plotting data
Plotting data is a really good thing to be able to do too. `matplotlib` is the basic plotting library, `seaborn` is a nice wrapper around `matplotlib`.

Here are some examples of plots:
```python
import numpy as np
import matplotlib.pyplot as plt
plt.plot(np.sin(np.linspace(0,10,1000)))
plt.show()

# flip some coins, wow binomial distribution!
coins = [sum([np.random.randint(2) for j in range(100)]) for i in range(1000)]
plt.hist(coins)
plt.show()

```


# Problem 1
Plot a sine wave. Plot another sine wave. Add them together!

# Problem 1.75
Write some text to a file called `data.txt`. Specifically write out this text: 
```python
data = "The cup game is a classic problem in computer science that models work scheduling. In the cup game on n cups, a filler and an emptier take turns adding and removing water from cups (i.e. new tasks come in and the scheduler must allocate processors to handle the incoming work). On each round the filler will distribute some new amount of water among the cups, and the emptier will remove some amount of water from some of the cups. The filler can distribute the water however it wants (as long as it places at most 1 water in each cup), but the emptier has an added discretization constraint: it can only remove water from some fixed number of cups. The problem is to analyze how well each player can do, that is, how much water can the filler force to be in the fullest cup, and what is the upper bound on this fill that an appropriate emptying strategy can guarantee? We study several variants of the problem and answer some open questions."
```

# Problem 1.5
Read in that file called `data.txt` and print it out

# Problem 2
Make a histogram of how many times each character occurs in that file


# Problem 3
Generate some data of "happiness versus sleep".
It should be slightly random noise added to some distribution (e.g. `happiness = 1000-(sleep-7)**2 + np.random.random()`).

# Problem 4
Write that data out to a `csv` `happydata.csv`
Hint: use `import pandas`, or `import json`

# Problem 5
Read the data in from `happydata.csv`, and make a parabola of best fit (or whatever is appropriate based on your model). 
Hint: use `numpy`

# Problem 6
Make a heat map of `gcd(i,j)` $$i,j\in\{1,2,\ldots, n\}$$

# Problem 7
Make a graph of the primes.

