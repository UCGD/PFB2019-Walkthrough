#!/usr/bin/env python3

"""
Open and print the reverse complement of each sequence in Python_06.seq.txt. Each line is the
following format: seqName\tsequence\n. Make sure to print the output in fasta format including
the sequence name and a note in the description that this is the reverse complement.
Print to STDOUT and capture the output into a file with a command line redirect '>'.
"""

seq_file = open('Python_06.seq.txt', 'r')


for line in seq_file:
    id, seq = line.split()
    new_id = id + '|sequence is reverse complemented'

    comp_dna = ""
    for nt in seq:
        if nt == 'A':
            nt = nt.replace('A', 'T')
        elif nt == 'T':
            nt = nt.replace('T', 'A')
        elif nt == 'G':
            nt = nt.replace('G', 'C')
        elif nt == 'C':
            nt = nt.replace('C', 'G')

        comp_dna = comp_dna + nt
    rev_comp_seq = ">{}\n{}"
    print(rev_comp_seq.format(new_id, comp_dna))
seq_file.close()