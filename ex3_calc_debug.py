import math
prohibited = ('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')


def calculator():
    f_num = input('What is the first number? ')
    while f_num in prohibited:
        f_num = input("You cant use letters. What is the first number? ")
    f_num = float(f_num)
    operation = input('''
What operation would you like to complete? Please enter the wanted option:
===========================
***************************
===========================
+\t\t| addition
-\t\t| subtraction
*\t\t| multiplication
/\t\t| division
sqrt\t| squareroot
pi/\t\t| Divide number with pi
pi*\t\t| Multiply number with pi
fact\t| Factorial calculation of the number
===========================
***************************
===========================

Enter requested operator: ''')

    if operation.lower() == 'fact':
        print("{}'s factorial is {}".format(f_num, math.factorial(f_num)))
    elif operation.lower() == 'sqrt':
        print('{} square root = '.format(f_num), end='')
        print(math.sqrt(f_num))
    elif operation.lower() == 'pi/':
        print('{} / pi = '.format(f_num), end='')
        print(f_num / math.pi)
    elif operation.lower() == 'pi*':
        print('{} * pi = '.format(f_num), end='')
        print(f_num * math.pi)
    elif operation == '+' or operation == '-' or operation == '*' or operation == '/':
        l_num = input('Please enter the second number: ')
        while l_num in prohibited:
            l_num = input("You cant use letters. What is the second number? ")
        l_num = int(l_num)
        if operation == '+':
            print('{} + {} = '.format(f_num, l_num), end='')
            print(f_num + l_num)
        elif operation == '-':
            print('{} - {} = '.format(f_num, l_num), end='')
            print(f_num - l_num)
        elif operation == '*':
            print('{} * {} = '.format(f_num, l_num), end='')
            print(f_num * l_num)
        elif operation == '/':
            print('{} / {} = '.format(f_num, l_num), end='')
            print(f_num / l_num)
    else:
        print('You have not typed a valid operator, please run the program again.')
        again()


def again():
    calc_again = input('''
Do you want to calculate again?
Please type Y for YES or N for NO.
ENTER HERE:  ''')

    if calc_again.upper() == 'N':
        print('See you later.')
    elif calc_again.upper() == 'Y':
        calculator()
    else:
        again()


calculator()
