# Run in Python >= 3.10

# 1.1
def calculate(string):
    import math

    try:
        a_s, s, b_s = string.split()
        a = float(a_s)
        b = float(b_s)
    except ValueError as e:
        print(e)
        return math.nan

    if s == "+":
        return a + b
    if s == "-":
        return a - b
    if s == "*":
        return a * b
    if s == "/":
        try:
            return a / b
        except ArithmeticError as e:
            print(e)
            return math.inf

    return math.nan


# 1.13
def find_string_pattern(str1, str2):
    if len(str1) != len(str2):
        return False

    n = len(str1)
    cmp = {}

    for i in range(0, n):
        a = str1[i]
        b = str2[i]

        if a in cmp:
            if cmp[a] == b:
                continue
            else:
                return False
        else:
            cmp[a] = b

    return True


# 1.2
def grid(rows, columns, size):
    s = "#"
    d = " "

    r1 = s * (columns * size + columns + 1)
    r2 = (s + d * size) * columns + s

    for i in range(0, rows):
        print(r1)
        for j in range(0, size):
            print(r2)
    print(r1)
