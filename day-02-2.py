prog = list(map(int, input().split(",")))
for noun in range(100):
    for verb in range(100):
        mem = prog[:]
        mem[1] = noun
        mem[2] = verb
        i = 0
        while i < len(mem):
            if mem[i] == 99:
                break
            elif mem[i] == 1:
                mem[mem[i + 3]] = mem[mem[i + 1]] + mem[mem[i + 2]]
            else:
                mem[mem[i + 3]] = mem[mem[i + 1]] * mem[mem[i + 2]]
            i += 4
        if mem[0] == 19690720:
            print("%d" % (100 * noun + verb))
            break
    else:
        continue
    break
