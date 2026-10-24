from collections import OrderedDict

N = int(input())
d = OrderedDict()
for _ in range(N):
    *itemName, itemPrice = input().split()
    d[" ".join(itemName)] = d.get(" ".join(itemName), 0) + int(itemPrice)

print(*[f"{k} {v}" for k, v in d.items()], sep="\n")
