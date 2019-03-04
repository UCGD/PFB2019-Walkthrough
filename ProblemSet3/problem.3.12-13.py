#!/usr/bin/env python3

dna = 'GATGGGATTggggttttccccTCCCATGTGCTCAAGACTGGCGCTaaaaGttttGAGCTTCTCaaaaGTCTAGAGCCACCGTCCAGGGAGCAGGTAGCTGCTGGGCTCCggggACACTTTGCGTTCGGGCTGGGAGCGTGCTTTCCACGACGGTGACACGCTTCCCTGGATTGGCAGCCAGACTGCCTTCCGGGTCACTGCCATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGccccCTCTGAGTCAGGAAACAttttCAGACCTATGGAAACTACTTCCTGaaaaCAACGTTCTGTccccCTTGCCGTCCCAAGCAATGGATGATTTGATGCTGTccccGGACGATATTGAACAATGGTTCACTGAAGACCCAGGTCCAGATGAAGCTCCCAGAATTCGCCAGAGGCTGCTccccCCGTGGccccTGCACCAGCAGCTCCTACACCGGCGGccccTGCACCAGccccCTCCTGGccccTGTCATCTTCTGTCCCTTCCCAGaaaaCCTACCAGGGCAGCTACGGTTTCCGTCTGGGCTTCTTGCATTCTGGGACAGCCAAGTCTGTGACTTGCACGTACTccccTGCCCTCAACAAGATGttttGCCAACTGGCCAAGACCTGCCCTGTGCAGCTGTGGGTTGATTCCACAccccCGCCCGGCACCCGCGTCCGCGCCATGGCCATCTACAAGCAGTCACAGCACATGACGGAGGTTGTGAGGCGCTGccccCACCATGAGCGCT'

dna_upper = dna.upper()
sub_dna = dna_upper[101:200]

comp_dna = ""
for seq in sub_dna:
    if seq == 'A':
        seq = seq.replace('A', 'T')
    elif seq == 'T':
        seq = seq.replace('T', 'A')
    elif seq == 'G':
        seq = seq.replace('G', 'C')
    elif seq == 'C':
        seq = seq.replace('C', 'G')

    comp_dna = comp_dna + seq

## Print report
report = """
        Original Sequence  5' {} 3'
        From base 100-200 5' {} 3'
        Number of G's in substring {}
        Complement         3' {} 5'
        Reverse Complement 5' {} 3'
"""
print(report.format(dna, sub_dna, sub_dna.count('G'), comp_dna, comp_dna[::-1]))
