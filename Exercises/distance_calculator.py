def is_float(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

def feet_to_inches(distance):
    return round(distance * 12, 2)

def feet_to_yards(distance):
    return round(distance / 3, 2)

def feet_to_miles(distance):
    return round(distance / 5280, 2)

def convert_feet(distance):
    print(distance, "ft, is ", feet_to_inches(distance), "inches, or, ", feet_to_yards(distance), " yards, or ", feet_to_miles(distance), "miles.")

user_input = input("Enter a value in feet > ")
while is_float(user_input) == False:
    print("Invalid input")
    user_input = input("Enter a value in feet > ")
convert_feet(float(user_input))
