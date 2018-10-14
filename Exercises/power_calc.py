def calculate(number, power):
    total = 0
    for x in range(0, power):
        total += number**x
    return total + number**power

number = input("number >> ")
power = input("power >> ")

print(calculate(int(number), int(power)))
