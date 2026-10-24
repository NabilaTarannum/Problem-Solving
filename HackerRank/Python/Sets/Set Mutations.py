len_set = int(input())
storage = set(map(int, input().split()))

for _ in range(int(input())):
    op, *temp = input().split()
    temp_storage = set(map(int, input().split()))
    getattr(storage, op)(temp_storage)

print(sum(storage))
