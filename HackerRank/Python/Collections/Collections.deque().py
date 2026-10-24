from collections import deque

storage = deque()
for _ in range(int(input())):
    cmd = input().split()
    getattr(storage, cmd[0])(*cmd[1:])

print(*storage)
