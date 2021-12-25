password = input("Choose your password: ")
correct_password = input("Confirm your password: ")
its_true = password == correct_password
print("The password is correct: " + str(its_true))


name = "John"
singer = "Lennon"
president = "Kennedy"
actor = "Travolta"
last_name=[singer,president,actor]
available_choices = [0, 1, 2]
who = int(input("Which famous person are you talking about? 0 for the singer, 1 for the president and 2 for the actor: "))
if who not in available_choices:
    who = int(input("Select 0,1,2"))
name += " " + last_name[who]
print(name)


def is_long_string(word):
    return len(word) >= 10


def print_string(word):
    if is_long_string(word):
        print(word + " is a long string")
    else:
        print(word + " is a normal string")


def judge(word1, word2):
    if len(word1)>len(word2):
        print_string(word1)
    elif len(word1) == len(word2):
        print("The two words have the same length" )
    else:
        print_string(word2)


word1 = input("Please enter the first word: ")
word2 = input("Please enter the second word: ")

judge(word1, word2)
