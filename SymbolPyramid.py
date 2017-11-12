#!/bin/python3

"""
///HackerRank///
Problem : Write a program that prints a staircase of size n.
@ input: size n
e.g. 5
     @ output: Prints a staircase of size n
e.g.
      *
     **
    ***
   ****
  *****

"""
import sys

n = int(input().strip())
i = 1
j = n-1

for i in range(1, n+1, 1):
    print(' '*j + '*'*i)
    j = j-1
