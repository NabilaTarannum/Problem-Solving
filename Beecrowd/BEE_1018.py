# -*- coding: utf-8 -*-

"""
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
"""

value = int(input())
print(value)
notes = [100, 50, 20, 10, 5, 2, 1]


for note_ in notes:
    div = value / note_
    mod = value % note_
    print(f"{int(div)} nota(s) de R$ {note_},00")
    value = mod

# another example - 

value = int(input())
notes = [100, 50, 20, 10, 5, 2, 1]

print(value)
for note in notes:
    count = value // note
    value %= note
    print(f"{count} nota(s) de R$ {note},00")
