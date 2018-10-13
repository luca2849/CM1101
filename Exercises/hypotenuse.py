import math
def calculate_hypotenuse(base, height):
    hypot = math.sqrt((base**2)+(height**2))
    return "\n" + str(round(hypot, 2))
print("Welcome to the hypotenuse calculator")
base = int(input("Please enter the base length of the triangle > "))
height = int(input("Please enter the height of the triangle > "))

print(calculate_hypotenuse(base, height))
