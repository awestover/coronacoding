---
title: Huffman Coding
author: Alek Westover
---

Today we did Huffman coding. Here is the code:

```python
codes = {}

# compression

# what is compresssion?

# english: abcde etc
# english is bad because frequency of e is >> frequency of x

# ultimately in a computer stuff is stored in binary/hex
# (really just as numbers)

# english characters associated with numbers
# a --> 00000
# b --> 00001
# c --> 00010
# d --> 00011
# e --> 00100
# f --> 00101
# ...

# this is kinda dumb
# frequency of e is >> frequency of x BUT e and x have the same length "codes"
# so lets do it better

# frequent stuff gets shorter codes
# Leon: e-->1
# Alek: but wait, then nothing else can have a 1 in it.(kind of) RIP. kinda bad.
# we aren't screwed.
# we can still come up with a prefix free encoding that is gooder than giving 5 bits to each character


"""

Huffman coding:
nodes = [ Node(blah, frequency), ...  ]

nodes = [Node(a, 10%), Node(b, 14%), Node(c, 5%), ....]

while length(nodes) > 1:
    merge the two nodes with smallest frequencies into a single node 

This creates a binary tree that gives you the codes

"""

class Tree:
    def __init__(self, val, freq):
        self.val = val
        self.freq = freq
        self.right_child = None
        self.left_child = None

    def print_tree_codes(self, parent_stuff):
        print(self.val, parent_stuff)
        if self.right_child:
            self.right_child.print_tree_codes(parent_stuff+"1")
        if self.left_child:
            self.left_child.print_tree_codes(parent_stuff+"0")

    def write_global_codes(self, parent_stuff):
        if self.right_child or self.left_child:
            if self.right_child:
                self.right_child.write_global_codes(parent_stuff+"1")
            if self.left_child: 
                self.left_child.write_global_codes(parent_stuff+"0")
        else:
            codes[self.val] = parent_stuff

    def __str__(self):
        return f"{self.val} {self.freq}"

letter_freqs = {"E": 0.1202, "T": 0.091, "A": 0.0812, "O": 0.0768, "I": 0.0731, "N": 0.0695, "S": 0.06280000000000001, "R": 0.0602, "H": 0.0592, "D": 0.0432, "L": 0.0398, "U": 0.0288, "C": 0.0271, "M": 0.026099999999999998, "F": 0.023, "Y": 0.021099999999999997, "W": 0.0209, "G": 0.0203, "P": 0.0182, "B": 0.0149, "V": 0.0111, "K": 0.0069, "X": 0.0017000000000000001, "Q": 0.0011, "J": 0.001, "Z": 0.0007000000000000001}

trees = [Tree(character, letter_freqs[character]) for character in letter_freqs]

while len(trees) > 1:
    trees.sort(key=lambda x: x.freq)
    parent = Tree(f"({trees[0].val})({trees[1].val})", trees[0].freq + trees[1].freq)
    parent.right_child = trees[0]
    parent.left_child = trees[1]
    trees = trees[2:]
    trees.append(parent)

trees[0].print_tree_codes("")


with open("lots_of_text.txt", "r") as f:
    data = f.read().upper()

taboo_characters = set(data)
print(taboo_characters)
for character in letter_freqs:
    if character in taboo_characters:
        taboo_characters.remove(character)
    
for taboo_character in taboo_characters:
    data = data.replace(taboo_character, "")

with open("clean_text.txt", "w") as f:
    f.write(data)

trees[0].write_global_codes("")
print([(ci, codes[ci]) for ci in codes])


# loop over the text
# we're gonna concatenate the codes
# everytime we exceed 512 bits, we "write something out"

output = []
buffer_code = ""
for character in data:
    buffer_code += codes[character]
    if len(buffer_code) >= 8:
        output.append(int(buffer_code[:8], base=2))
        buffer_code = buffer_code[8:]

output = bytes(output)
#  print(output)

with open("encoded_text.txt", "wb") as f:
    f.write(output)
    

```

You can also see this code on Alek's blog, at [compression blogpost](https://awestover.github.io/skyspace/compression/).

Wikipedia is also a great resource.

