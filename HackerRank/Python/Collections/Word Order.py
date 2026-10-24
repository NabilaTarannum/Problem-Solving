from collections import Counter

N = int(input())
words = [input() for _ in range(N)]
d = Counter(words)

print(len(d))
print(*d.values())
