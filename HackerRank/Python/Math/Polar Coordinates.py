import cmath

num = complex(input().strip())

magnitude, phase = cmath.polar(num)

print(f"{magnitude}\n{phase}")
