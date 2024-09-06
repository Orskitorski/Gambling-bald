import random

computerDice = random.randrange(1, 6)
print("The computer rolled a: " , computerDice)

bet = input("How much do you want to bet?")

guess = input("Do you want to guess higher '+', lower '-' or equal? '='")

values = ("-", "+", "=")

if guess != "+" or guess != "-" or guess != "=":
    print("")

playerDice = random.randrange(1, 6)
print("You rolled a: " , playerDice)

if playerDice > computerDice and guess == "+":
    winAmount = int (bet * ((6 - computerDice) + 1))
    print("not fag")
    print (winAmount)
elif playerDice < computerDice and guess == "-":
    winAmount = int (bet * ((6 - computerDice) + 1))
    print("not fag")
    print (winAmount)
elif playerDice == computerDice and guess == "=":
    winAmount = int (bet * ((6 - computerDice) + 1))
    print("not fag")
    print (winAmount)
else:
    print("fag")
    