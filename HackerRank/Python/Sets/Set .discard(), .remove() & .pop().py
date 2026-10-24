# Language : python3
n, s = int(input()), set(map(int, input().split()))
for _ in range(int(input())):
    cmd, *args = input().split()
    getattr(s, cmd)(*map(int, args) if args else [])
print(sum(s))
