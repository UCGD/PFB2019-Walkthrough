#!/usr/bin/env python3

elements = [101,2,15,22,95,33,2,27,72,15,52]

evnSum = 0
oddSum = 0 
for e in elements:
    print("The element: ", e)
    if e % 2 == 0:
        evnSum += e
    if e % 2 != 0:
        oddSum +=e

print("Sum of even numbers: ", evnSum)
print("Sum of odd: ", oddSum)
