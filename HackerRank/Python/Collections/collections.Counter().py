from collections import Counter


n = int(input())
stock = list(map(int, input().split()))
Dict = Counter(stock)

x = int(input())
p = 0

for _ in range(x):
    size, price = map(int, input().split())
    if Dict[size] > 0:
        Dict[size] -= 1
        p += price

print(p)
