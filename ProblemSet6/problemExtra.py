#!/usr/bin/env python3

"""
get the raw file Python_06.seq.txt
in a script, open this file
iterate over each line in this file (seqName\tsequence\n)
for each sequence:
calculate and store the count of each unique nucleotide character in a dictionary
report the name, total of each nucleotide count, and the GC content
"""

seq_file = open('Python_06.seq.txt', 'r')

for line in seq_file:
    line = line.rstrip()

    id, sequence = line.split()
    uniq_seq = set(sequence)

    seq_count = {}
    for nt in uniq_seq:
        seq_count[nt] = sequence.count(nt)

    print("ID: ", id)
    total_bases = 0
    gc_content = 0
    for base, count in seq_count.items():
        total_bases = total_bases + count
        if base == 'G':
            gc_content = gc_content + count
        elif base == 'C':
            gc_content = gc_content + count

        report = "Base: {} Count: {}"
        print(report.format(base, count))

    gc_report = "Total GC content: {:.1f}%"
    print(gc_report.format((gc_content/total_bases) * 100))
    print("------------------")

seq_file.close()

