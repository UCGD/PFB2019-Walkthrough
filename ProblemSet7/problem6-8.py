#!/usr/bin/env python3
import re

fa_file = open('Python_07_ApoI.fasta', 'r')

dna_string = ''
for i in fa_file:
    line = i.rstrip()
    header_match = re.search(r"^>", line)
    if header_match:
        continue
    restriction_match = re.sub(r"([AG])(AATT)([CT])", r"\1^\2\3", line)
    if restriction_match:
        dna_string = dna_string + restriction_match

fa_file.close()
print("Seq with cut sites: ", dna_string)

## split and sort by entry length.
fragments = dna_string.split('^')
fragments.sort(key=len)
print("Sequence by length:")
for site in fragments:
    print(site)
