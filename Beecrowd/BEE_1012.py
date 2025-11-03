# -*- coding: utf-8 -*-

"""
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
"""

A, B, C = [float(s) for s in input().split()]

triangle = (1 / 2) * (A * C)
radius = 3.14159 * C**2
trapezium = (1 / 2) * C * (A + B)
square = (B) ** 2
rectangle = A * B

print("TRIANGULO: {:.3f}".format(triangle))
print("CIRCULO: {:.3f}".format(radius))
print("TRAPEZIO: {:.3f}".format(trapezium))
print("QUADRADO: {:.3f}".format(square))
print("RETANGULO: {:.3f}".format(rectangle))
