---
title: key 4
author: Alek Westover
---

```python

import numpy as np


# let the array be of size n

def bubbleSort(data, start, length):
    # compare each thing to every other thing
    # running time: n choose 2 = (n+1)n  /2 = O(n^2)

    # note: in-place

    for i in range(start, start+length):
        for j in range(i+1, start+length):
            if data[i] > data[j]: 
                # do the swap
                tmp = data[j]
                data[j] = data[i]
                data[i] = tmp

def quickSort(data, start, length): # data[start], data[start+1], ..., data[start+length-1]
    # chose a pivot
    # partition the array relative to the pivot
    # ex: partition [4,3,3,6,7,8,1,3,4,6] relative to pivot = 5 would be [4,3,3,1,3,4, | 6,7,8,6]
    # recursively sort the lower and upper sub arrays

    # running time:
    # technically, worst case is O(n^2)
    # but really, it's super fast
    # with high probability in n, it has running time O(n log n), with really good constant
    
    if length < 10:
        if length > 1:
            bubbleSort(data, start, length)
        return

    def partition(pivot):
        low = start 
        high = start+length-1
        while low < high:
            while low < high and data[low] <= pivot:
                low += 1
            while low < high and data[high] > pivot:  
                high -= 1
            # swap
            if low < high:
                tmp = data[low]
                data[low] = data[high]
                data[high] = tmp

        if low < start+length and data[low] <= pivot:
            low += 1
        return low

    pivot = data[int(np.random.rand()*length)+start]
    low = partition(pivot)

    quickSort(data, start, low-start)
    quickSort(data, low, length-(low-start))

def insertionSort(data, n):
    # in place
    #  O(n^2) 
    # basically, repeatedly insert a new element into a sorted prefix array
    for i in range(1,n):
        val = data[i]
        j = i-1
        while j >= 0 and data[j] > val:
            data[j+1] = data[j]
            j-=1
        data[j+1] = val


def mergeSort(data, n):
    # split the array in half 
    # sort the left and right halves
    # merge the two sorted arrays

    # running time: O(n log n)

    if n == 0 or n == 1:
        return data

    # merge sort is not in-place

    # ex:
    # [2,3,1, ||| 2,6,7]
    # [1,2,3 ||| 2,6,7]
    # [1,2,2,3,6,7]

    def merge(A, B):
        C = []
        a = 0
        b = 0
        for i in range(len(A)+len(B)):
            if a >= len(A) or b>=len(B):
                break
            if A[a] < B[b]:
                C.append(A[a])
                a+=1
            else:
                C.append(B[b])
                b+=1

        while a < len(A):
            C.append(A[a])
            a+= 1

        while b < len(B):
            C.append(B[b])
            b+= 1

        return C
    
    # recursion:
    firstHalf = mergeSort(data[:n//2], n//2)
    secondHalf = mergeSort(data[n//2:], n-n//2)
    merged = merge(firstHalf, secondHalf)
    return merged


def countingSort(data, k, n): # 0 <= data[i] < k
    # integer sorting
    # running time: O(n)

    counts = [0 for i in range(k)]
    for i in range(n):
        counts[data[i]] += 1

    ## ex. k = 3
    ## data = [0,0,0,0,1,2,2,2,2,2,1,1,1,1,0,1]
    ## counts = [10, 2, 3]
    ## running_sums = [0, 10, 12]

    running_sums = []
    running_sum = 0
    for i in range(k):
        running_sums.append(running_sum)
        running_sum += counts[i]

    # go through data
    # we know where to put stuff now
    # by the running_sum array

    output = [0 for i in range(n)]
    for i in range(n):
        output[running_sums[data[i]]] = data[i]
        running_sums[data[i]] += 1

    return output

def timSort(data):
    data.sort() # :), this is python's built in function
    # although you may never have to implement a sorting function yourself
    # sorting functions are great examples for doing running time analysis
    # and are also just super useful :) 

def radixSort(data):
    pass
    # look this one up on wikipedia if you're  curious, its like counting sort  but a lot of times!

# many more!


import numpy as np
import matplotlib.pyplot as plt
N = 100

# running bubbleSort
data = np.random.rand(N)
bubbleSort(data, 0, N)
plt.plot(data)
plt.title("bubbleSort")
plt.show()

# running insertionSort
data = np.random.rand(N)
insertionSort(data, N)
plt.plot(data)
plt.title("insertionSort")
plt.show()

# running quickSort
data = np.random.rand(N)
quickSort(data, 0, N)
plt.plot(data)
plt.title("quickSort")
plt.show()

# running mergeSort
data = np.random.rand(N)
sorted_data = mergeSort(data, N)
plt.plot(sorted_data)
plt.title("mergeSort")
plt.show()


# running counting sort
K = 10
integer_data = [int(x) for x in np.random.rand(N)*K]
sorted_data = countingSort(integer_data, K, N)
plt.plot(sorted_data)
plt.title("countingSort")
plt.show()

```
