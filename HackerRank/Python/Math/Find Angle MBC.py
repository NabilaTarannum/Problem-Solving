import math

a = int(input())
b = int(input())
theta = math.degrees(math.acos(b / math.sqrt(a**2 + b**2)))
print(f"{round(theta)}{chr(176)}")
