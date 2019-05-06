#!/usr/bin/env python3
import re

name = input("What name to use...")

nobody_file = open('Python_07_nobody.txt', 'r')
new_file = open(name + '.txt', 'w')

for l in nobody_file:
    found = re.search(r"(nobody)", l, re.I)
    if found:
        new_line = re.sub(found.group(1), name, l, re.I)
        new_file.write(new_line)
    else:
        new_file.writelines(l)

nobody_file.close()
new_file.close()
