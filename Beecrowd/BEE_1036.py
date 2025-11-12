# -*- coding: utf-8 -*-

"""
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
"""

from math import sqrt


A, B, C = [float(s) for s in input().split()]
calc = (B * B) - (4 * (A) * (C))

if calc > 0 and A != 0:
    calc = sqrt(calc)
    x = (-B + calc) / (2 * A)
    y = (-B - calc) / (2 * A)
    print("R1 = {:.5f}".format(x))
    print("R2 = {:.5f}".format(y))
else:
    print("Impossivel calcular")
