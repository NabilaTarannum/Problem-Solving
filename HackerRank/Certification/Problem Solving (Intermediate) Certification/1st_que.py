#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countPairs' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#


def countPairs(arr):
    # Write your code here
    B = 12
    M = 1 << B
    freq = [0] * M
    for x in arr:
        freq[x] += 1

    ordered = 0
    for k in range(B):
        bit = 1 << k
        S = [freq[v] if v & bit else 0 for v in range(M)]
        for j in range(B):
            for s in range(M):
                if s >> j & 1:
                    S[s] += S[s ^ (1 << j)]
        for a in range(M):
            if freq[a] and a & bit:
                ordered += freq[a] * S[(M - 1) ^ (a ^ bit)]

    self_pairs = sum(freq[1 << k] for k in range(B))
    return (ordered - self_pairs) // 2


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    arr_count = int(input().strip())

    arr = []

    for _ in range(arr_count):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = countPairs(arr)

    fptr.write(str(result) + "\n")

    fptr.close()
