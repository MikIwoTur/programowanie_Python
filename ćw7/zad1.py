import random


def randomNucleotides():
    Nucleotides = "AGTC"
    amount = random.randint(1, 10)

    seq = random.choice(Nucleotides)
    seq2 = random.choice(Nucleotides)
    seq3 = random.choice(Nucleotides)
    seq4 = random.choice(Nucleotides)
    seq5 = random.choice(Nucleotides)

    full_seq = seq + seq2 + seq3 + seq4 + seq5
    return full_seq * amount


randomNucleotides = randomNucleotides()
print(randomNucleotides)
