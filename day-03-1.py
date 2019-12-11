board = [['.' for i in range(12648)] for j in range(8806)]
dirs = {'R': [0, 1], 'L': [0, -1], 'U': [-1, 0], 'D': [1, 0]}
w1 = input().split(',')
w2 = input().split(',')
coords = [1775, 9377]
maxh, minh, maxv, minv = 0, 0, 0, 0
for w in w1:
    for i in range(int(w[1:])):
        coords[0] += dirs[w[0]][0]
        coords[1] += dirs[w[0]][1]
        board[coords[0]][coords[1]] = '1'
distances = []
coords = [1775, 9377]
for w in w2:
    for i in range(int(w[1:])):
        coords[0] += dirs[w[0]][0]
        coords[1] += dirs[w[0]][1]
        if board[coords[0]][coords[1]] == '1':
            distances.append(abs(coords[0] - 1775) + abs(coords[1] - 9377))
print(min(distances))
