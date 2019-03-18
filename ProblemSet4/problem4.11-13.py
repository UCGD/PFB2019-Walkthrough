#!/usr/bin/env python3


dna = ['ATGCCCGGCCCGGC','GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT','ATGGGCCC']

collection = []
for i in dna:
    place = dna.index(i)
    seqInfo = (place, len(i), i)
    collection.append(seqInfo)

print(collection)
