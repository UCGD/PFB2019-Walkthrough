#!/usr/bin/env python3

# Faster none practice way
from math import factorial
import sys

factor = int(sys.argv[1])
start = 1
fact = 1

while True:
    if start == factor + 1:
        break
    fact = fact * start
    start += 1
print(fact)

## Fast double check
double_check = factorial(factor)
if double_check == fact:
    print("Double check match!", double_check)

