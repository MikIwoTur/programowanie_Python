import re
from pathlib import Path
import json

fasta = {}
wrong_fasta = {}
p = Path('data.txt')
file = p.rename(p.with_suffix('.fasta'))

with open(file) as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        if line.startswith(">"):
            active_sequence_name = line[1:]
            if active_sequence_name not in fasta:
                fasta[active_sequence_name] = []
            continue
        sequence = re.findall('[ATCG]', line)
        fasta[active_sequence_name].append(len(sequence))

    f.seek(0)

    for line in f:
        line = line.strip()
        if not line:
            continue
        if line.startswith(">"):
            active_error = line[1:]
            if active_error not in wrong_fasta:
                wrong_fasta[active_error] = []
            continue
        wron_seq = [i for i, char in enumerate(line) if char == "-"]
        wrong_fasta[active_error].append(wron_seq)

    with open('failedProcess.py', "w") as FP:
        json.dump(wrong_fasta, FP)

print(fasta)