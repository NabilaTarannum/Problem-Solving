# -*- coding: utf-8 -*-

"""
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
"""

code, item = [int(s) for s in input().split()]

if code == 1:
    x = item * 4.00
elif code == 2:
    x = item * 4.50
elif code == 3:
    x = item * 5.00
elif code == 4:
    x = item * 2.00
elif code == 5:
    x = item * 1.50

print("Total: R$ %.2f" % x)
