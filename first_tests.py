from first import calculate, grid, find_string_pattern


def calculate_test():
    print(calculate("2 + 2"))
    print(calculate("2 - 2"))
    print(calculate("2 * 2"))
    print(calculate("2 / 2"))
    print(calculate("qwe + 2"))
    print(calculate("2 qwe 2"))
    print(calculate("2 * qwe"))
    print(calculate("qwe"))
    print(calculate("2 / 0"))


def grid_test():
    grid(3, 4, 2)
    grid(3, 3, 3)
    grid(1, 3, 3)
    grid(1, 3, 1)


def find_string_pattern_test():
    print(find_string_pattern("ABAB", "CDCD"))
    print(find_string_pattern("ABCBA", "BCDCB"))
    print(find_string_pattern("FFGG", "CDCD"))
    print(find_string_pattern("FFFF", "ABCD"))


if __name__ == '__main__':
    calculate_test()
    grid_test()
    find_string_pattern_test()
