from itertools import permutations
from math import inf

def main():
    prog = list(map(int, input().split(",")))
    combos = permutations([0, 1, 2, 3, 4])
    max_output = -inf
    for c in combos:
        in0 = 0
        for i in range(5):
            in0 = compute(prog, c[i], in0)
        if in0 > max_output:
            max_output = in0
            max_input = c
    print(max_output)
    print(max_input)

def compute(prog, in1, in2):
    mem = prog[:]
    first_input = True
    i = 0
    while i < len(mem):
        op = str(mem[i])
        if op[-1] in "125678":
            if len(op) <= 2:
                op1 = mem[mem[i + 1]]
                op2 = mem[mem[i + 2]]
            elif len(op) == 3:
                op1 = mem[mem[i + 1]] if op[-3] == '0' else mem[i + 1]
                op2 = mem[mem[i + 2]]
            else:
                op1 = mem[mem[i + 1]] if op[-3] == '0' else mem[i + 1]
                op2 = mem[mem[i + 2]] if op[-4] == '0' else mem[i + 2]
            if op[-1] in "12":
                mem[mem[i + 3]] = op1 + op2 if op[-1] == '1' else op1 * op2
                i += 4
            elif op[-1] in "78":
                mem[mem[i + 3]] = 1 if int(op1) < int(op2) else 0
                mem[mem[i + 3]] = int(op1 < op2) if op[-1] == '7' else int(op1 == op2)
                i += 4
            else:
                jump = op1 != 0 if op[-1] == '5' else op1 == 0
                i = op2 if jump else i + 3
        elif op[-1] == '3':
            mem[mem[i + 1]] = in1 if first_input else in2
            first_input = False
            i += 2
        elif op[-1] == '4':
            op1 = mem[mem[i + 1]] if len(op) == 1 or (len(op) > 1 and op[-3] == '0') else mem[i + 1]
            return op1
            i += 2
        elif op[-2:] == "99":
            break

if __name__ == "__main__":
    main()
