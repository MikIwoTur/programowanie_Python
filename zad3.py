n = range(20)
i = range(30)

result = sum(i != n for n, i in zip(n, i))

print(result)