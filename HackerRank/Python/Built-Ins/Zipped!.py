n, x = map(int, input().split())
sheet = [list(map(float, input().split())) for _ in range(x)]
print(*[sum(i) / len(i) for i in zip(*sheet)], sep="\n")
