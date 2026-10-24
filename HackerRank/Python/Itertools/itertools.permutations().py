from itertools import permutations

s, k = input().split()
k = int(k)

for word in sorted(permutations(s, k)):
    print("".join(word))
