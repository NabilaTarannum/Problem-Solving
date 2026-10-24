def count_substring(string, sub_string):

    s = len(string)
    s1 = len(sub_string)
    s2 = 0

    for i in range(s - s1 + 1):
        if string[i : (i + s1)] == sub_string:
            s2 = s2 + 1

    return s2


if __name__ == "__main__":
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
