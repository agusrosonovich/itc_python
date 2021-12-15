import random


def ronda():
    global money
    player_selection = 0
    player_card = random.randint(1, 12)
    pc_card = random.randint(1, 12)
    global bet
    print("Your card is " + str(player_card) + " and my card is " + str(pc_card))
    if player_card-pc_card > 0:
        money = money + bet
        print("You won " + str(bet) + " and now you have " + str(money))
        print("1. Play another round")
        print("2. Leave with my money :-)")
        player_selection = int(input("What would you like to do? "))
        if player_selection == 1:
            player_bet()
        elif player_selection == 2:
            print("You have " + str(money) + ". Thank you for playing")

    else:
        money -= bet
        print("You lost " + str(bet) + " and now you have " + str(money))
        if money == 0:
            print("You are broke... Bye Bye")
        else:
            print("Don't worry you can play again")
            player_bet()


def player_bet():
    global money
    global bet
    bet = input("Place your bet for the next round: 1 to " + str(money) + ": ")
    bet = int(bet)
    if bet > money:
        print("I said between 1 to " + str(money) + "And you typed " + str(bet) +" ")
        print("I don't play with liars!! Bye ")
    else:
        ronda()
        money -= bet


print("###################### Welcome To WAR ######################")
global money
global bet
money = 50
name = input("Enter your name: ")
print("Hello " + name + " You currently have " + str(money))
player_bet()








