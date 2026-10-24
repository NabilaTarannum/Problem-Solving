N1 = int(input())
storage1 = set(input().split())

N2 = int(input())
storage2 = set(input().split())

print(len(storage2.intersection(storage1)))
