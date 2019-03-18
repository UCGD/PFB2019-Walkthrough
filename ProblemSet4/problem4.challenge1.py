#!/usr/bin/env python3
import random

dna = 'GCTAGCTAGCAATACGATAAACCGGGCTAGCTAGCAATACGATAAACCGG'
dnaLen = len(dna)

for i in range(0, dnaLen):
    randSeqA = random.randrange(dnaLen)
    randSeqB = random.randrange(dnaLen)

    randDna = dna.replace(dna[randSeqA], dna[randSeqB])

print("OG seq:\n", dna)
print("Fisher-Yates shuffle:\n", randDna)




