#!/usr/bin/env python3

import sys


start = int(sys.argv[1])
end = int(sys.argv[2]) + 1

for x in range(start, end):
    print(x)

    if x % 2 != 0:
        print("The odds: ", x)
