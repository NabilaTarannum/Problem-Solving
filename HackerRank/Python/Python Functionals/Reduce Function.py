from fractions import Fraction
from functools import reduce


def product(fracs):
    t = t = reduce(
        Fraction.__mul__, fracs
    )  # complete this line with a reduce statement
    return t.numerator, t.denominator


# sourcery skip: for-append-to-extend, list-comprehension
if __name__ == "__main__":
    fracs = []
    for _ in range(int(input())):
        fracs.append(Fraction(*map(int, input().split())))
    result = product(fracs)
    print(*result)
