# -*- coding: utf-8 -*-

"""
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
"""

a, b, c = [int(s) for s in input().split()]
test = [a, b, c]
sort = sorted(test)
print(*sort, sep="\n")
print("")
print(*test, sep="\n")
