import random

bet = int(input("How much do you want to bet?"))

computerDice = random.randrange(1, 6)
print("The computer rolled a: " , computerDice)

guess = input("Do you want to guess higher '+', lower '-' or equal? '='")

values = ("-", "+", "=")

if guess != "+" or guess != "-" or guess != "=":
    print("")

playerDice = random.randrange(1, 6)
print("You rolled a: " , playerDice)

if playerDice > computerDice and guess == "+":
    winAmount = bet * (6 - int (computerDice) + 1)
    print("You won!!!")
    print (winAmount)
elif playerDice < computerDice and guess == "-":
    winAmount = bet * (0 +  int (computerDice) + 1)
    print("You won!!!")
    print (winAmount)
elif playerDice == computerDice and guess == "=":
    winAmount = bet * 10000
    print("You won!!!")
    print (winAmount)
else:
    print("You lose fucker")
    