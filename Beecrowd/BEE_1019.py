# -*- coding: utf-8 -*-

"""
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
"""

value = int(input())

hour = value // 3600
minute = (value % 3600) // 60
second = (value % 3600) % 60

print(f"{hour}:{minute}:{second}")
