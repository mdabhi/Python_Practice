#!/bin/python3.6

"""
///HackerRank///
Problem : Given an array of integers, calculate which fraction of its elements are positive, which fraction of its elements
are negative, and which fraction of its elements are zeroes, respectively. Print the decimal value of each fraction on a new line.
@ input param: n, arr of numbers
e.g. 5
     0 2 -3 5 -1
@ output: Positive #/total numbers, Negative # /total numbers, # of zeros/ total numbers
e.g. 0.4
     0.4
     0.2

"""

import sys
import decimal
from decimal import Decimal


def get_fraction(n,arr):
    i = 0
    poscnt = 0
    negcnt = 0
    zerocnt = 0
    result = list()

    while i < n:
        if arr[i] < 0:
            negcnt += 1
        elif arr[i] > 0:
            poscnt += 1
        else:
            zerocnt += 1
        i += 1
    posfraction = poscnt / n
    posfraction = float(posfraction)
    result = [posfraction]
    negfraction = negcnt / n
    result.append(negfraction)
    zerofraction = zerocnt / n
    result.append(zerofraction)
    return result

def main():
    n = int(input().strip())
    arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
    result = []
    result = get_fraction(n, arr)
    for i in result:
        print(i)

if __name__ == '__main__':
    main()
