from itertools import product

A = map(int, input().split())
B = map(int, input().split())
output = product(A, B)
print(*output)
