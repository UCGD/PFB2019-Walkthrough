#!/usr/bin/env python3
import re

fasta_file = open('Python_07.fasta', 'r')

for f in fasta_file:
    i = f.rstrip()
    header_match = re.search(r"^>((\w+)\|(\d+))\|(\w+)\|(\w+.\d)\|(.+)$", i)
    if header_match:
        report = 'id:"{}" desc:"{}"'
        print(report.format(header_match.group(1), header_match.group(6)))

fasta_file.close()


'''
for f in fasta_file:
    i = f.rstrip()
    header_match = re.search(r"^>(.+)$", i)
    if header_match:
        header_split = i.split('|')
        report = 'id:"{}{}" desc:"{}"'
        print(report.format(header_split[0], header_split[1], header_split[-1]))

fasta_file.close()
'''
