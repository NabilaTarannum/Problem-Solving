#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'transformSentence' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING sentence as parameter.
#


def transformSentence(sentence):
    # Write your code here
    words = sentence.split(" ")
    transformed_words = []

    for word in words:
        new_word = word[0]

        for i in range(1, len(word)):
            current_char = word[i]
            prev_char = word[i - 1]

            c_lower = current_char.lower()
            p_lower = prev_char.lower()

            if p_lower < c_lower:
                new_word += current_char.upper()
            elif c_lower < p_lower:
                new_word += current_char.lower()
            else:
                new_word += current_char

        transformed_words.append(new_word)

    return " ".join(transformed_words)


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    sentence = input()

    result = transformSentence(sentence)

    fptr.write(result + "\n")

    fptr.close()
