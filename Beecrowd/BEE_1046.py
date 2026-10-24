# -*- coding: utf-8 -*-

"""
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
"""

a, b = [int(s) for s in input().split()]

if a < b:
    print(f"O JOGO DUROU {b - a} HORA(S)".format(a, b))
else:
    print(f"O JOGO DUROU {b + 24 - a} HORA(S)".format(a, b))
