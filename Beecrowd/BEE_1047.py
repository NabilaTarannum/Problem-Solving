# -*- coding: utf-8 -*-

"""
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
"""


def calculate_game_duration(ih, im, fh, fm):
    start = ih * 60 + im
    end = fh * 60 + fm
    if end <= start:
        end += 24 * 60
    duration = end - start
    return divmod(duration, 60)


def main():
    ih, im, fh, fm = map(int, input().split())
    h, m = calculate_game_duration(ih, im, fh, fm)
    print(f"O JOGO DUROU {h} HORA(S) E {m} MINUTO(S)")


if __name__ == "__main__":
    main()
