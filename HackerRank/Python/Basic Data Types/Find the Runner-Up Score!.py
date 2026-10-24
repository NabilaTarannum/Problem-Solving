if __name__ == "__main__":
    n = int(input())
    arr = sorted(map(int, input().split()))
    print(arr[(arr.index(max(arr))) - 1])
