import math
f1 = "Język programowania python jest super"
f2 = "Język programowania javascript odraża mnie"
f3 = [f1 + ' ' + f2]
list_f1 = [f1]
list_f2 = [f2]


def TFIDF(base):
    TF = []
    for document in base:
        dic = {}
        for word in document.split():
            if word in dic:
                dic[word] += 1
            else:
                dic[word] = 1
    for word, freq in dic.items():
        print(word, freq)
        dic[word] = freq/len(document.split())
    TF.append(dic)

    IDF = {}
    for word in dic:
        IDF[word] = 1 + math.log(1 + 2) / (1 + freq)

    SUM = []
    for freq in dic:
        values = dic[freq] * IDF[freq]
        SUM.append(values)
    return TF, IDF, SUM


print(TFIDF(list_f1))
print('\n')
print(TFIDF(list_f2))
print('\n')
print(TFIDF(f3))
