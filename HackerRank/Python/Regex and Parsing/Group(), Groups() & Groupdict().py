import re

print(
    (lambda m: m.group(1) if m else -1)(re.search(r"([a-zA-Z0-9])\1", input().strip()))
)
