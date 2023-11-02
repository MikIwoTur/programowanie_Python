import math

# za pomocą map
print(list(map(lambda x: math.sqrt(x) % 2 == 0, range(20))))

# za pomoca filter
print(list(filter(lambda x: math.sqrt(x) % 2 == 0, range(20))))

# lista skladana
pierw_X = []
for x in range(20):
    if (math.sqrt(x) % 2 == 0):
        pierw_X.append(x)

print(pierw_X)
