#!/usr/bin/env python3
import sys, re

class FileNameError(Exception):
    pass

class SeqTypeError(Exception):
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

try:
    out_file = open('Python_08.codons-6frames.nt', 'w')
except IOError:
    print("Cant create needed file: Python_08.codons-6frames.nt")

fasta_record = {}
gene, dna_seq = '', ''
for i in fasta_file:
    record = i.rstrip()

    if re.match(r">", record):
        if gene and dna_seq:
            first_codon = re.findall('...', dna_seq)
            first_reverse = first_codon[::-1]

            second_codon = re.findall('...', dna_seq[1:])
            second_reverse = second_codon[::-1]

            third_codon = re.findall('...', dna_seq[2:])
            third_reverse = third_codon[::-1]

            report = """
            Gene {}
            first frame: {}
            first reverse: {}
            second frame: {}
            second reverse: {}
            third frame: {}
            third reverse: {} 
            """
            out_file.write(report.format(gene, ' '.join(first_codon), ' '.join(first_reverse), ' '.join(second_codon), ' '.join(second_reverse),
                                ' '.join(third_codon), ' '.join(third_reverse)))
        dna_seq = ''
        header_info = re.split(' ', record)
        gene = re.sub(r'>', '', header_info[0])
        fasta_record[gene] = {}
    else:
        try:
            if re.match(r'[^ATGCN]', dna_seq):
                raise SeqTypeError('Sequence other then ATGCN not allowed.')
        except SeqTypeError:
            print("Error found.", dna_seq)
        dna_seq = dna_seq + record
fasta_file.close()
out_file.close()
