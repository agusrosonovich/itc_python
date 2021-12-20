def digit_test(number):
    if (len(number) == 4 or len(number) == 6) and number.isdigit():
        return True
    return False


print(digit_test("1234"))
print(digit_test("as15"))
print(digit_test("12345"))


def calculator(operation, number1, number2):
    if operation == "+":
        return number1+number2
    elif operation == "-":
        return number1-number2
    elif operation == "*":
        return number1*number2
    elif operation == "/":
        return number1/number2
    else:
        print("invalid operation")


print(calculator("+", 3, 4))
print(calculator("-", 3, 4))
print(calculator("*", 3, 4))
print(calculator("/", 3, 4))




