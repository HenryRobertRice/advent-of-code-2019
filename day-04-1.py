def main():
    n = 0
    for i in range(271973, 785962):
        if is_valid(i):
            n += 1
    print(n)

def is_valid(i):
    i = str(i)
    has_double = False
    for j in range(1, len(i)):
        if i[j] == i[j - 1]:
            has_double = True
        if i[j] < i[j - 1]:
            return False
    return has_double

if __name__ == "__main__":
    main()
