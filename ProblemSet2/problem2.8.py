#!/usr/bin/env python3
import sys

## Get value from command line.
## And convert to type int.
x = int(sys.argv[1])

## Run tests.
if x > 0:
    print("value ", x,  " is positive")
    if x < 50:
        print("value ", x,  "is positive, but less then 50.")
        if x % 2 == 0:
            print("it is an even number that is smaller than 50")
    if x > 50:
        if ((x /3) % 2 == 0):                
            print("it is larger than 50 and divisible by 3")
elif x == 0:
    print("value ", x,  " is equal to 0.")
else:
    print("value ", x,  " is negative")
