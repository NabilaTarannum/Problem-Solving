# -*- coding: utf-8 -*-

"""
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
"""

x1, y1 = [float(s) for s in input().split()]
x2, y2 = [float(s) for s in input().split()]

distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

print("{:.4f}".format(distance))
