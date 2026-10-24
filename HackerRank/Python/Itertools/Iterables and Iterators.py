from itertools import combinations

N = int(input())
char = input().split()
K = int(input())

print(sum("a" in i for i in combinations(char, K)) / len(list(combinations(char, K))))
