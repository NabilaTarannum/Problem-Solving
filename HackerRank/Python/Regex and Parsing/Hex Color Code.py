import re

for _ in range(int(input())):
    s = input()
    if len(s.split()) > 1 and "{" not in s:
        [print(i) for i in re.findall(r"#[a-fA-F0-9]{3,6}", s)]
