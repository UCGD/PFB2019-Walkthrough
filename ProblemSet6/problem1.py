#!/usr/bin/env python3

tp_heart = open('Python_06.txt', 'r')
out_file = open('Python_06_uc.txt', 'w')

for line in tp_heart:
    line = line.rstrip()
    out_file.write(line.upper() + '\n')

tp_heart.close()
out_file.close()


