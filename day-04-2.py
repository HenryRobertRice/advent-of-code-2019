def main():
    n = 0
    for i in range(271973, 785962):
        if is_valid(i):
            n += 1
    print(n)

def is_valid(i):
    i = str(i)
    doubles = dict()
    for j in range(1, len(i)):
        if i[j] == i[j - 1]:
            if i[j] in doubles:
                doubles[i[j]] = -1
            else:
                doubles[i[j]] = 1
        if i[j] < i[j - 1]:
            return False
    return 1 in doubles.values()

if __name__ == "__main__":
    main()
