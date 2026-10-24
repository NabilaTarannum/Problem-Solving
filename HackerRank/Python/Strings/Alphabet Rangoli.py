def print_rangoli(size):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    pattern = []

    for i in range(size):
        row = "-".join(
            alphabet[size - 1 : size - i - 1 : -1] + alphabet[size - i - 1 : size]
        )
        pattern.append(row.center(4 * size - 3, "-"))

    print("\n".join(pattern + pattern[-2::-1]))


if __name__ == "__main__":
    n = int(input())
    print_rangoli(n)
