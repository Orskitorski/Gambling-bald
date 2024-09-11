import random

isPlaying = True
money = 100

while isPlaying:

    betIsCorrect = False
    guessIsCorrect = False
    yesOrNoIsCorrect = False

    while betIsCorrect == False:
        bet = int(input("How much do you want to bet?"))
        if bet > money:
            print("You dont have that much money")
        else:
            betIsCorrect = True
            money -= bet
            print(money)


    computerDice = random.randrange(1, 6)
    print("The computer rolled a: " , computerDice)

    while guessIsCorrect == False:
        guess = input("Do you want to guess higher '+', lower '-' or equal? '='")
        if guess != "+" or guess != "-" or guess != "=":
            print("You can only guess '+' , '-' or '='")
        else:
            guessIsCorrect = True


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


    while yesOrNoIsCorrect == False:
        yesOrNo = input("Do you want to play again? y/n")
        if yesOrNo != "y" or guess != "n":
            print("Answer only with 'y' or 'n' stupid")
        else:
            yesOrNoIsCorrect = True

    if yesOrNo == ("n"):
        isPlaying = False
    elif yesOrNo == ("y"):
        isPlaying = True



