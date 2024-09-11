import random

isPlaying = True

while isPlaying:

    bet = int(input("How much do you want to bet?"))

    computerDice = random.randrange(1, 6)
    print("The computer rolled a: " , computerDice)

    guess = input("Do you want to guess higher '+', lower '-' or equal? '='")

    values = ("-", "+", "=")

    if guess != "+" or guess != "-" or guess != "=":
        print("")

    playerDice = random.randrange(1, 6)
    print("You rolled a: " , playerDice)

    if int(playerDice) > int(computerDice) and guess == "+":
        winAmount = int(bet) * (int(playerDice) - int(computerDice))
        print("You won: " , winAmount)
    elif int(playerDice) < int(computerDice) and guess == "-":
        winAmount = int(bet) * (int(computerDice) - int(playerDice))
        print("You won: " , winAmount)
    elif int(playerDice) == int(computerDice) and guess == "=":
        winAmount = int(bet) * 10000
        print("You won: " , winAmount)
    else:
        print("You lose fucker")

    yesOrNo = input("Do you want to play again? y/n")
    if yesOrNo == ("n"):
        isPlaying = False
    else:
        isPlaying = True
    