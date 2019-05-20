#!/usr/bin/env python3
import sys, re

try:
    fasta_file = open(sys.argv[1], 'r')
except:
    print("Can't open needed fasta file.")

fasta_record = {}
gene, dna_seq = '', ''
for i in fasta_file:
    record = i.rstrip()

    if re.match(r">", record):
        if gene and dna_seq:
            sequence_set = set(dna_seq)
            for s in sequence_set:
                count_of = dna_seq.count(s)
                fasta_record[gene][s] += count_of
        dna_seq = ''
        header_info = re.split(' ', record)
        gene = re.sub(r'>', '', header_info[0])
        fasta_record[gene] = {}
    else:
        dna_seq = dna_seq + record
fasta_file.close()

# print last record.
sequence_set = set(dna_seq)
for s in sequence_set:
    count_of = dna_seq.count(s)
    fasta_record[gene][s] = count_of

for gene, counter in fasta_record.items():
    report = "{}\tA:{}\tT:{}\tG:{}\tC:{}"
    print(report.format(gene, counter['A'], counter['T'], counter['G'], counter['C']))
