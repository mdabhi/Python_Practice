#!/bin/python3

"""
///HackerRank///
Problem : Colleen is turning n years old! Therefore, she has candles of various heights on her cake, and candle has height h.
Because the taller candles tower over the shorter ones, Colleen can only blow out the tallest candles.
Given the for each individual candle, find and print the number of candles she can successfully blow out.
@ input param: n, arr of numbers
e.g. 4
     5 2 3 5
@ output: total no. of tallest candles
e.g. 2

"""

import sys


def birthdayCakeCandles(n, ar):
    # Complete this function
    maxnum = max(ar)
    cnt = 0
    for i in range(0,n):
        if ar[i]==maxnum:
            cnt = cnt+1
    return cnt

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = birthdayCakeCandles(n, ar)
print(result)