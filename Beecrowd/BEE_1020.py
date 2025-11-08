# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

value = int(input())

year = value // 365
month = (value - year * 365) // 30
day = (value - year * 365 - month * 30)

print(f"{year} ano(s)\n{month} mes(es)\n{day} dia(s)")

