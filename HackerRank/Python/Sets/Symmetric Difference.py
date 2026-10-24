_, m = input(), set(map(int, input().split()))
_, n = input(), set(map(int, input().split()))
print(*sorted(m ^ n), sep="\n")
