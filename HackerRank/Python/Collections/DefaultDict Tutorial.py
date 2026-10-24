from collections import defaultdict


n, m = map(int, input().split())

a = defaultdict(list)
for i in range(1, n + 1):
    a[input()].append(i)

for _ in range(m):
    key = input()
    if key in a:
        print(" ".join(map(str, a[key])))
    else:
        print(-1)
