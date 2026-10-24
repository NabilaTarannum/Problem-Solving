import re

for _ in range(int(input())):
    N = input().strip()
    if (
        N.isalnum()
        and len(N) == 10
        and re.search(r"(.*[A-Z]){2,}", N)
        and re.search(r"(.*[0-9]){3,}", N)
        and not re.search(r".*(.).*\1", N)
    ):
        print("Valid")
    else:
        print("Invalid")
