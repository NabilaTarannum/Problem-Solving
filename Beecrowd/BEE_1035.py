# -*- coding: utf-8 -*-

"""
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
"""

A, B, C, D = [int(s) for s in input().split()]

if (B > C and D > A) and (C + D > A + B) and ((C and D) > 0) and ((A % 2) == 0):
    print("Valores aceitos")
else:
    print("Valores nao aceitos")
