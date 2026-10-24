storage = set(input().split())
N = int(input())
output = True

for _ in range(N):
    storage2 = set(input().split())
    if not storage2.issubset(storage) or len(storage2) >= len(storage):
        output = False
        break

print(output)
