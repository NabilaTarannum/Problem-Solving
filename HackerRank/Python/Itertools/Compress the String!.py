from itertools import groupby

for i, j in groupby(map(int, input().strip())):
    print((len(list(j)), i), end=" ")
