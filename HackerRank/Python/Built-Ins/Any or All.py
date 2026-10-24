n = int(input())
l = input().split()
print(all(int(i) > 0 for i in l) & any(i == i[::-1] for i in l))
