#!/usr/bin/env python3
import sys, re

class FileNameError(Exception):
    pass

try:
    in_file = sys.argv[1]
    fasta_file = open(in_file, 'r')
    if not in_file.endswith('.fa'):
        raise FileNameError
except IndexError:
    print('Fasta file required.')
except IOError:
    print("Can't open needed fasta file.")
except FileNameError:
    print('fasta file must end in .fa')

fasta_record = {}
gene, dna_seq = '', ''
for i in fasta_file:
    record = i.rstrip()

    if re.match(r">", record):
        if gene and dna_seq:
            codon = re.sub(r'(...)', r' \1 ', dna_seq)
            print(gene, codon)
        dna_seq = ''
        header_info = re.split(' ', record)
        gene = re.sub(r'>', '', header_info[0])
        fasta_record[gene] = {}
    else:
        dna_seq = dna_seq + record
fasta_file.close()
