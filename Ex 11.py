import math


def calculate_bmi(weight, height):
    bmi = weight / pow(height, 2)
    return bmi


persona_1 = {"name": "", "age": 0, "weight": 0, "height": 0, "BMI": 0}
persona_2 = {"name": "", "age": 0, "weight": 0, "height": 0, "BMI": 0}

personas = [persona_1, persona_2]

for persona in personas:
    persona["name"] = input("Insert name ")

    persona["age"] = input("Insert age ")
    # while not age.isdigit():
    # persona["age"] = input("You did not submit a number. What is your age")

    persona["weight"] = input("Insert weight ")
    # while not weight.isdigit():
    #  persona["weight"] = input("You did not submit a number. What is your weight")

    persona["height"] = input("Insert height ")
    # while not height.isdigit():
    # persona["height"] = input("You did not submit a number. What is your height")
    persona["BMI"] = calculate_bmi(int(persona["weight"]), int(persona["height"]))
    # int(persona["weight"])/pow(int(persona["height"]), 2)

    del persona["weight"]
    del persona["height"]


print(personas)
print("")
