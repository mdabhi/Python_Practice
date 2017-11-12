#!/bin/python3.6

"""
///HackerRank///
Problem : Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly
four of the five integers. Then print the respective minimum and maximum values as a single line of two space-separated
long integers.
@ input param: 5 numbers with space separated
e.g. 1 5 2 3 5

@ output: min sum of 4 numbers , max sum of 4 numbers
e.g. 15 11
"""


import sys


def max_min_sum(arr):

    max_sum = 0
    min_sum = 0
    result = list()
    temp_arr1 = arr
    temp_arr2 = arr

    temp_arr1.sort(reverse=True)
    for i in range(0, 4):
        max_sum += temp_arr1[i]

    temp_arr2.sort()
    for i in range(0, 4):
        min_sum += temp_arr2[i]

    result = [min_sum]
    result.append(max_sum)

    return result


def main():
    arr = list(map(int, input().strip().split(' ')))
    res = list()
    res = max_min_sum(arr)

    print(res[0],res[1])

if __name__ == '__main__':
    main()
