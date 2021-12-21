"""import logging

logging.basicConfig(level=logging.INFO)

logging.debug("In the Moria Mountain")
logging.info("Balrog is here!")
logging.warning("you shall not pass")
"""
# https://www.w3resource.com/python-exercises/python-conditional-statements-and-loop-exercises.php

# exercise 7

datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class":'V', "section":'A'}]

for i in datalist:
    print(i, "is type", type(i))

# exercise 8

for i in range(6):
    if i == 3 or i == 6:
        continue
    print(i)

# exercise 10

for i in range(1,51):
    if i%3==0 and i%5==0:
        print("fizzbuzz")
    elif i%3==0:
        print("fizz")
    elif i%5==0:
        print("buzz")
    else:
        print(i)

# exercise 10

data2 = "Python 3.2"
letters = 0
digits = 0
for i in data2:
    if i.isnumeric():
        digits += 1
    elif i.isalpha():
        letters += 1
    else:
        continue

print("number of letter", letters)
print("number of digits", digits)

# exercise 31


def dog_age_in_dogs_years(number):
    age=0
    if number==1 or number==2:
        age=number*10.5
    elif number<0:
        number2=int(input("enter valid naumber"))
        dog_age_in_dogs_years(number2)

    else:
        age= 21+(number-2)*4

    return age


dog_age_in_human = input("input a dog's age in human years")
print("age in dog's age= ",dog_age_in_dogs_years(int(dog_age_in_human)))



