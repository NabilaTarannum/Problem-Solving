# -*- coding: utf-8 -*-

"""
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
"""

a, b, c = [float(s) for s in input().split()]

if (a + b > c) and (a + c > b) and (b + c > a):
    p = a + b + c
    print("Perimetro = {:.1f}".format(p))
else:
    p = 1 / 2 * (a + b) * c
    print("Area = {:.1f}".format(p))
