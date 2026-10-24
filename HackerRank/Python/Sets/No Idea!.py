m, n = map(int, input().split())
storage = list(map(int, input().split()))
A = set(map(int, input().split()))
B = set(map(int, input().split()))

print(sum((i in A) - (i in B) for i in storage))
