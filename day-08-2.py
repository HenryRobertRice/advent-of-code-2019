from math import inf
output_chars = {'0': '█', '1': ' ', '2': ' '}
picture = list(input())
min_0 = inf
frame = picture[0:150]
for i in range(1, 100):
    layer = picture[i * 150:i * 150 + 150]
    for j in range(150):
        if frame[j] == '2' and layer[j] != '2':
            frame[j] = layer[j]
for i in range(6):
    print("".join(output_chars[f] for f in frame[i * 25:i * 25 + 25]))
print(output)
