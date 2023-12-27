import math
import re
from collections import Counter

f1 = "Język programowania python jest super"
f2 = "Język programowania javascript odraża mnie"


WORD = re.compile(r"\w+")


def COS(vec, vec2):
    inter = set(vec.keys()) & set(vec2.keys())
    numerator = sum(vec[x] for x in inter)

    sum_vec = sum([vec[x] ** 2 for x in list(vec.keys())])
    sum_vec2 = sum([vec2[x] ** 2 for x in list(vec2.keys())])
    denominator = math.sqrt(sum_vec) * math.sqrt(sum_vec2)

    if not denominator:
        return 0.0
    else:
        return float(numerator) / denominator


def vector_from_text(text):
    words = WORD.findall(text)
    return Counter(words)


vector1 = vector_from_text(f1)
vector2 = vector_from_text(f2)

cosine = COS(vector1, vector2)

print("COSINE:", cosine)
