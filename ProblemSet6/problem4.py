#!/usr/bin/env python3

"""
Open the FASTQ file Python_06.fastq and go through each line of the file. Count the number of lines and the number of characters per line. Have your program report the:
total number of lines
total number of characters
average line length
"""

fq_file = open('Python_06.fastq', 'r')

line_count = 0
num_chars = 0
for line in fq_file:
    line = line.rstrip()
    line = ''.join( line.split() )
    line_count = line_count + 1

    num_chars = num_chars + len(line)

average_length = num_chars/line_count

fq_report ="""
total number of lines {}
total number of characters {}
average line length {}
"""
print(fq_report.format(line_count, num_chars, average_length))


