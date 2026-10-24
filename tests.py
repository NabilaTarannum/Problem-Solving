def adjust_thermostat(temp, target):
    if temp > target:
        return ("cool")
    elif temp == target:
        return ("hold")
    elif temp < target:
        return ("heat")
    return


print(adjust_thermostat(68, 72))
print(adjust_thermostat(75, 72))
print(adjust_thermostat(72, 72))
