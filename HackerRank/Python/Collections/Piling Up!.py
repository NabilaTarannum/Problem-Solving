from collections import deque

for _ in range(int(input())):
    input()
    d = deque(map(int, input().split()))
    max_elem = float("inf")
    flag = "Yes"
    while d:
        curr = d.popleft() if d[0] >= d[-1] else d.pop()
        if curr > max_elem:
            flag = "No"
            break
        max_elem = curr
    print(flag)
