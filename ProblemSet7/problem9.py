#!/usr/bin/env python3
import re, sys

net_file = open('bionet.txt', 'r')
fasta_file = open(sys.argv[1], 'r')
enzymes = sys.argv[2]

bionet_lookup = {}
for line in net_file:
    text_line = line.rstrip()
    unneeded = re.match(r"(REBASE|Rich|^\s+|^\s+$)", text_line)
    if unneeded:
        continue
    enzymes_sites = re.findall(r"(\w+)\s+\((\w+)\)\s+(\w+)", text_line)
    if len(enzymes_sites) < 1:
       continue
    bionet_lookup[enzymes_sites[0][0]] = enzymes_sites[0][-1]
    bionet_lookup[enzymes_sites[0][1]] = enzymes_sites[0][-1]

net_file.close()

for i in fasta_file:
    line = i.rstrip()
    header_match = re.search(r"^>", line)
    if header_match:
        continue
    enzymes_match = re.findall(bionet_lookup[enzymes], line)
    if enzymes_match:
        restriction_site = line.replace(bionet_lookup[enzymes], '^' + bionet_lookup[enzymes])
        print(restriction_site)

