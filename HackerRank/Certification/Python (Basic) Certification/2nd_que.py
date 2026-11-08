#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'numCells' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY grid as parameter.
#


def numCells(grid):
    # Write your code here
    if not grid or not grid[0]:
        return 0

    n = len(grid)
    m = len(grid[0])
    dominant_count = 0

    directions = [
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (0, -1),
        (0, 1),
        (1, -1),
        (1, 0),
        (1, 1),
    ]

    for r in range(n):
        for c in range(m):
            current_val = grid[r][c]
            is_dominant = True

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] >= current_val:
                    is_dominant = False
                    break

            if is_dominant:
                dominant_count += 1

    return dominant_count


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    grid_rows = int(input().strip())
    grid_columns = int(input().strip())

    grid = []

    for _ in range(grid_rows):
        grid.append(list(map(int, input().rstrip().split())))

    result = numCells(grid)

    fptr.write(str(result) + "\n")

    fptr.close()
