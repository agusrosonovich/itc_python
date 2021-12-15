import random
import numpy as np

print("     _______________,,.")
print("    /_____________.;;'/|")
print('   |"____  _______;;;]/')
print("   | || //'         ;")
print("   | ||//'          ;")
print("   | |//'           ;)")
print("   |  /'            $")
print("   | ||             $)")
print("   | ||             $")
print("   | ||            ,^.")
print("   | ||            | |")
print("   | ||            `.'")
print("   | ||")
print("   | ||")
print("   | ||")
print("   | ||")
print("   | ||   _________________________")
print("   | ||  /                        4")
print("   | || /                        /|")
print("   | ||/           _____        / /")
print("   | ||           /|___/       / /|")
print("   | ||          / |  /       / /||")
print("   |_|/         /  | /       / / ||")
print('  /             """""       / /| ||"')
print(" /                         / / | ||")
print("/                         / /  | ||")
print('""""""""""""""""""""""""""|/   | ||')
print("__________________________f|   | |")
print("| ||                    | ||")
print("| ||                    | ||")
print("| ||                    | ||")
print("| ||                    | ||")
print("| ||                    | ||")
print("| |                     | |")


def random_word(list_of_words):  # Get one of the words in the list
    word = random.choice(list_of_words)
    return word.upper()


global guesses
guesses = 10
game_finished = False
print("WELCOME TO HANGMAN")
list_of_words = ["Dalmatian", "Kit", "Usher", "Pothole", "Exercise", "Final", "Passport", "Cyclone", "Poetry",
                 "Hammock"]
hidden_word = random_word(list_of_words)
hidden_word2 = list(hidden_word)
hidden_word2 = np.array(hidden_word2)  # Used to make a np array
stars = list(hidden_word)
for i in range(len(stars)):  # Create the list with the right amount of stars
    stars[i] = "*"
stars = np.array(stars)

while not game_finished or guesses > 0:
    print("You have " + str(guesses) + " left")
    print("This is your word")
    print(stars)

    guess = input("What is your guess ").upper()  # Here i check that the input is correct
    if len(guess) != 1:
        print("You have to enter only 1 letter, try again ")
        guess = input().upper()
    elif guess not in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
        print("You have to enter a letter, try again")
        guess = input().upper()
    if guess not in hidden_word:
        guesses -= 1

    result = np.where(hidden_word2 == guess)
    stars[result] = guess

    if guesses == 0:
        print("You are run out of guesses, you loose")
        game_finished = True
    if "*" not in stars:
        print(stars)
        print("You just complete the word, congratulations!!")
        game_finished = True
        break
