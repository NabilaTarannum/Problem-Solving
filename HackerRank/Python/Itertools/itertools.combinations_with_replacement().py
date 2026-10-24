from itertools import combinations_with_replacement

char, N = input().split()
N = int(N)

for i in combinations_with_replacement(sorted(char), N):
    print("".join(i))
