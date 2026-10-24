import re

print(
    *(
        m := re.findall(
            r"(?<=[qwrtypsdfghjklzxcvbnm])([aeiou]{2,})(?=[qwrtypsdfghjklzxcvbnm])",
            input().strip(),
            re.I,
        )
    )
    or [-1],
    sep="\n",
)
