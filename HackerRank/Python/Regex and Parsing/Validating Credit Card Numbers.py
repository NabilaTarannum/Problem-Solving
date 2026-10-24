import re

for _ in range(int(input())):
    S = input().strip()
    if re.match(r"^[456]\d{3}(-?)\d{4}\1\d{4}\1\d{4}$", S) and not re.search(
        r"(\d)\1{3,}", S.replace("-", "")
    ):
        print("Valid")
    else:
        print("Invalid")
