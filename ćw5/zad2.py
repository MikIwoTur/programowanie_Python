import re


class Seq():

    def __init__(self, tag, value):
        self.tag = tag
        self.value = value

    @classmethod
    def from_file(cls, file='sonic_sequence.txt'):
        fasta = {}

        with open(file) as f:
            proper_sequence = None
            for line in f:
                line = line.strip()
                if not line:
                    continue
                if line.startswith(">"):
                    proper_sequence = line[1:]
                    if proper_sequence not in fasta:
                        fasta[proper_sequence] = ''
                    continue
                value = re.sub('[^ATUCG]', '', line)
                fasta[proper_sequence] += value

        seq_dict = {}
        for tag, value in fasta.items():
            seq_dict[tag] = Seq(tag, value)

        if not seq_dict:
            return None

        return seq_dict

    def __len__(self):
        return len(self.value)

    def __str__(self):
        return str(self.value)


class DNASeq(Seq):
    def __init__(self, tag, value):
        super().__init__(tag, value)
        self.characteristics_nucleotides = set(['A', 'T', 'G', 'C'])

    def DNAtoRNA(self):
        return RNASeq(self.tag, self.value.replace('T', 'U'))


class RNASeq(Seq):
    def __init__(self, tag, value):
        super().__init__(tag, value)
        self.characteristics_nucleotides = set(['A', 'U', 'G', 'C'])
    
    def calculatorOfGC(self):
        amountGC = self.value.count('G') + self.value.count('C')
        allAmount = len(self.value)
        return (amountGC / allAmount) * 100


seq_dict_output = Seq.from_file()

if seq_dict_output is None:
    print("No sequence")
else:
    for tag, value in seq_dict_output.items():
        print(f"Tag: {tag}, \nLength: {(len(value))}, \nsequence: {value}")

        dna_output = DNASeq(tag, value)
        rna_output = DNASeq.DNAtoRNA(value)
        ProcOfGC = RNASeq.calculatorOfGC(value)
        print(f"From DNA to RNA: {rna_output}")
        print(f"Procentage of GC pairs in sequence: {ProcOfGC}")