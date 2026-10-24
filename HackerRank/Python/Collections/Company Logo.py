#!/bin/python3

import math
import os
import random
import re
import sys
import collections


if __name__ == "__main__":
    s = input().strip()
    s_counter = sorted(collections.Counter(s).items(), key=lambda x: (-x[1], x[0]))[:3]
    for char, count in s_counter:
        print(char, count)
