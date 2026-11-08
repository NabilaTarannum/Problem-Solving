#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maxSubarrayValue' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#


def maxSubarrayValue(arr):
    # Write your code here
    max_val = 0
    current_sum = 0
    current_max = 0
    current_min = 0

    for i in range(len(arr)):
        if i % 2 == 0:
            current_sum += arr[i]
        else:
            current_sum -= arr[i]

        val1 = current_sum - current_min
        val2 = current_max - current_sum

        max_val = max(max_val, val1 * val1, val2 * val2)

        current_max = max(current_max, current_sum)
        current_min = min(current_min, current_sum)

    return max_val


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    arr_count = int(input().strip())

    arr = []

    for _ in range(arr_count):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = maxSubarrayValue(arr)

    fptr.write(str(result) + "\n")

    fptr.close()
