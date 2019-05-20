#!/usr/bin/env python3
import sys, re

try:
    codon_file = open('Python_08.codons-6frames.nt', 'r')
    aa_file = open('Python_08.translated.aa', 'w')
except IOError:
    print("Can't open needed files.")

translation_table = {
    'GCT':'A', 'GCC':'A', 'GCA':'A', 'GCG':'A',
    'CGT':'R', 'CGC':'R', 'CGA':'R', 'CGG':'R', 'AGA':'R', 'AGG':'R',
    'AAT':'N', 'AAC':'N',
    'GAT':'D', 'GAC':'D',
    'TGT':'C', 'TGC':'C',
    'CAA':'Q', 'CAG':'Q',
    'GAA':'E', 'GAG':'E',
    'GGT':'G', 'GGC':'G', 'GGA':'G', 'GGG':'G',
    'CAT':'H', 'CAC':'H',
    'ATT':'I', 'ATC':'I', 'ATA':'I',
    'TTA':'L', 'TTG':'L', 'CTT':'L', 'CTC':'L', 'CTA':'L', 'CTG':'L',
    'AAA':'K', 'AAG':'K',
    'ATG':'M',
    'TTT':'F', 'TTC':'F',
    'CCT':'P', 'CCC':'P', 'CCA':'P', 'CCG':'P',
    'TCT':'S', 'TCC':'S', 'TCA':'S', 'TCG':'S', 'AGT':'S', 'AGC':'S',
    'ACT':'T', 'ACC':'T', 'ACA':'T', 'ACG':'T',
    'TGG':'W',
    'TAT':'Y', 'TAC':'Y',
    'GTT':'V', 'GTC':'V', 'GTA':'V', 'GTG':'V',
    'TAA':'*', 'TGA':'*', 'TAG':'*'
}

for i in codon_file:
    codon = i.lstrip().rstrip()

    if re.match(r'^Gene', codon):
        continue

    split_record = codon.split(':')
    try:
        split_seq = split_record[1].split()
        translated = [translation_table[x] for x in split_seq]
        protein_seq = ''.join(translated)
        print(codon, len(protein_seq))
        aa_file.write(protein_seq + '\n')
    except:
        continue
codon_file.close()
aa_file.close()

