prog = list(map(int, input().split(",")))
i = 0
while i < len(prog):
    op = str(prog[i])
    if op[-1] in "125678":
        if len(op) <= 2:
            op1 = prog[prog[i + 1]]
            op2 = prog[prog[i + 2]]
        elif len(op) == 3:
            op1 = prog[prog[i + 1]] if op[-3] == '0' else prog[i + 1]
            op2 = prog[prog[i + 2]]
        else:
            op1 = prog[prog[i + 1]] if op[-3] == '0' else prog[i + 1]
            op2 = prog[prog[i + 2]] if op[-4] == '0' else prog[i + 2]
        if op[-1] in "12":
            prog[prog[i + 3]] = op1 + op2 if op[-1] == '1' else op1 * op2
            i += 4
        elif op[-1] in "78":
            prog[prog[i + 3]] = 1 if int(op1) < int(op2) else 0
            prog[prog[i + 3]] = int(op1 < op2) if op[-1] == '7' else int(op1 == op2)
            i += 4
        else:
            jump = op1 != 0 if op[-1] == '5' else op1 == 0
            i = op2 if jump else i + 3
    elif op[-1] == '3':
        prog[prog[i + 1]] = int(input())
        i += 2
    elif op[-1] == '4':
        op1 = prog[prog[i + 1]] if len(op) == 1 or (len(op) > 1 and op[-3] == '0') else prog[i + 1]
        print(op1)
        i += 2
    elif op[-2:] == "99":
        break
