value = int(float(input()) * 100)

notes = [10000, 5000, 2000, 1000, 500, 200]
coins = [100, 50, 25, 10, 5, 1]

print("NOTAS:")
for note in notes:
    count = value // note
    print(f"{count} nota(s) de R$ {note / 100:.2f}")
    value %= note

print("MOEDAS:")
for coin in coins:
    count = value // coin
    print(f"{count} moeda(s) de R$ {coin / 100:.2f}")
    value %= coin
