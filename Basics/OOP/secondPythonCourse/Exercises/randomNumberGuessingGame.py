# Write a program that generates a random number in the range of 1 through 100, and asks the user to guess
# what the number is. If the users guess is higher than the random number, the program should display "Too high, try again"
# If the users guess is lower than the random number, the program should display "Too low, try again". If the user guesses
# the number, the application should congratulate the user and then generate a new random number so the game can start over.
#
# Optional enhancement: Enhance the game so it keeps count of the number of guesses that the user makes. When the user
# correctly guesses the random number, the program should display the number og guesses.


import random


def generateRandomNumber():
    randomNumber = random.randint(1, 100)
    return randomNumber


def askUserForNumber(message = "Guess the number: "):
    userNumber = int(input(message))
    return userNumber


def checkUserNumber(userNumber, randomNumber):
    if userNumber > randomNumber:
        return "Too high"
    elif userNumber < randomNumber:
        return "Too low"
    else:
        return "You guessed the number pal"


def main():
    userCongratulated = False
    letsStart = True

    while userCongratulated or letsStart:
        randomNumber = generateRandomNumber()
        print("For testing purposes, random number: ", randomNumber)
        userNumber = askUserForNumber()
        message = checkUserNumber(userNumber, randomNumber)

        while message != "You guessed the number pal":
            print(message)
            userNumber = askUserForNumber("Try again: ")
            message = checkUserNumber(userNumber, randomNumber)

    print(message)
    userCongratulated = True


main()