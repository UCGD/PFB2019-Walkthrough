#!/usr/bin/env python3

a = {3, 14, 15, 9, 26, 5, 35, 9}
b = {60, 22, 14, 0, 9}

# intersection, difference, union, and symetrical difference
print("Intersection: ", set(a) & set(b))
print("Difference: ", set(a) - set(b))
print("Union: ", set(a) & set(b))
print("symetrical difference: ", set(a) ^ set(b))
