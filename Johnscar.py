import random
import colorterminal
import time
import os

isPlaying = True

while isPlaying:

    print(colorterminal.ColorText.BLUE + 'Welcome to' + colorterminal.ColorText.PURPLE + ' Gambling-Bald' + colorterminal.ColorText.BLUE + '!!!')

    print()
    print(colorterminal.ColorText.WHITE + 'How much do you want to bet?')
    bet = int(input(colorterminal.ColorText.WHITE))
    
    time.sleep(0.2)
    os.system('cls||clear')
    print("|")
    time.sleep(0.2)
    os.system('cls||clear')
    print("⟋")
    time.sleep(0.2)
    os.system('cls||clear')
    print("―")
    time.sleep(0.2)
    os.system('cls||clear')
    print("⟍")
    time.sleep(0.2)
    os.system('cls||clear')
    print("|")
    time.sleep(0.2)
    os.system('cls||clear')
    print("⟋")
    time.sleep(0.2)
    os.system('cls||clear')
    print("―")
    time.sleep(0.2)
    os.system('cls||clear')
    print("⟍")
    os.system('cls||clear')

    computerDice = random.randrange(1, 6)

    print("The computer rolled a: " , colorterminal.ColorText.PURPLE + str(computerDice))

    print()
    print(colorterminal.ColorText.WHITE + "Do you want to guess higher " + colorterminal.ColorText.RED + "+" +  colorterminal.ColorText.WHITE + ", lower " + colorterminal.ColorText.BLUE + "-" + colorterminal.ColorText.WHITE + " or equal? " + colorterminal.ColorText.GREEN + "=")
    guess = input(colorterminal.ColorText.WHITE)

    time.sleep(0.2)
    os.system('cls||clear')
    print("|")
    time.sleep(0.2)
    os.system('cls||clear')
    print("⟋")
    time.sleep(0.2)
    os.system('cls||clear')
    print("―")
    time.sleep(0.2)
    os.system('cls||clear')
    print("⟍")
    time.sleep(0.2)
    os.system('cls||clear')
    print("|")
    time.sleep(0.2)
    os.system('cls||clear')
    print("⟋")
    time.sleep(0.2)
    os.system('cls||clear')
    print("―")
    time.sleep(0.2)
    os.system('cls||clear')
    print("⟍")
    os.system('cls||clear')

    playerDice = random.randrange(1, 6)
    print("You rolled a: " , colorterminal.ColorText.PURPLE + str(playerDice))
    print(colorterminal.ColorText.WHITE)

    if int(playerDice) > int(computerDice) and guess == "+":
        winAmount = int(bet) * (int(playerDice) - int(computerDice))
        print("You won: " , colorterminal.ColorText.YELLOW + str(winAmount))
    elif int(playerDice) < int(computerDice) and guess == "-":
        winAmount = int(bet) * (int(computerDice) - int(playerDice))
        print("You won: " , colorterminal.ColorText.YELLOW + str(winAmount))
    elif int(playerDice) == int(computerDice) and guess == "=":
        winAmount = int(bet) * 10000
        print("You won: " , colorterminal.ColorText.YELLOW + str(winAmount))
    else:
        print(colorterminal.ColorText.RED + "You lose fucker")

    print()

    yesOrNo = input(colorterminal.ColorText.BEREZOVY + "Do you want to play again? y/n")
    if yesOrNo == ("n"):
        isPlaying = False
    else:
        isPlaying = True