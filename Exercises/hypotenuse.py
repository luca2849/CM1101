import math
def calculate_hypotenuse(base, height):
    hypot = math.sqrt((base**2)+(height**2))
    return "\n" + str(round(hypot, 2))

def is_float(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

print("Welcome to the hypotenuse calculator")

base = input("Please enter the base length of the triangle > ")

while is_float(base) != True:
    print("Input must be numeric")
    base = input("Please enter the base length of the triangle > ")


height = input("Please enter the height of the triangle > ")
height_type = type(height)
while is_float(height) != True:
    print("Input must be numeric")
    height = input("Please enter the height of the triangle > ")



print(calculate_hypotenuse(float(base), float(height)))
