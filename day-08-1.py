from math import inf

picture = input()
min_0 = inf
for i in range(100):
    layer = picture[i * 150:i * 150 + 150]
    temp = layer.count('0')
    if temp < min_0:
        min_0 = temp
        output = layer.count('1') * layer.count('2')
print(output)
