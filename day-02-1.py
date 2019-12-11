prog = list(map(int, input().split(",")))
prog[1] = 12
prog[2] = 2
i = 0
while i < len(prog):
    if prog[i] == 99:
        break
    elif prog[i] == 1:
        prog[prog[i + 3]] = prog[prog[i + 1]] + prog[prog[i + 2]]
    else:
        prog[prog[i + 3]] = prog[prog[i + 1]] * prog[prog[i + 2]]
    i += 4
print(prog[0])
