from itertools import product

K, M = map(int, input().split())
N = [list(map(int, input().split()))[1:] for _ in range(K)]

print(max(sum(x**2 for x in i) % M for i in product(*N)))

