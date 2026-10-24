# -*- coding: utf-8 -*-

"""
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
"""

N_1, N_2, N_3, N_4 = [float(s) for s in input().split()]
weights = [2, 3, 4, 1]

value = (N_1 * 2 + N_2 * 3 + N_3 * 4 + N_4) / 10
print("Media: {:.1f}".format(value))

if value >= 7.0:
    print("Aluno aprovado.")
elif value >= 5.0:
    print("Aluno em exame.")
    last = float(input())
    print("Nota do exame: %.1f" % last)
    if last + value / 2.0 > 5.0:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    print("Media final: %.1f" % ((last + value) / 2.0))
else:
    print("Aluno reprovado.")
