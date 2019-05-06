#!/usr/bin/env python3
import re

nobody_file = open('Python_07_nobody.txt', 'r')

word_count = 0
for l in nobody_file:
    l = l.rstrip()
    found = re.search(r"(nobody)", l, re.I)
    if found:
        word_count = word_count + 1
        position = found.start() + 1
        print("Found at position: ", position)

nobody_file.close()
print('Total number of word "Nobody" found: ', word_count)
