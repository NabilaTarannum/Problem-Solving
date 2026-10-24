N = int(input())

storage = map(int, input().split())
storage = sorted(storage)

for i in range(len(storage)):
    if i == len(storage) - 1:
        print(storage[i])

    elif storage[i] not in [storage[i - 1], storage[i + 1]]:
        print(storage[i])
        break
