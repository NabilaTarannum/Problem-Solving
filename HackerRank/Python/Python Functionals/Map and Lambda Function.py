cube = lambda x: x**3  # complete the lambda function


def fibonacci(n):
    # return a list of fibonacci numbers
    storage = [0, 1]
    [storage.append(storage[-1] + storage[-2]) for _ in range(2, n)]
    return storage[:n]


if __name__ == "__main__":
    n = int(input())
    print(list(map(cube, fibonacci(n))))
