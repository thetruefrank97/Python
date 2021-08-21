# In this chapter, you saw an example of how you write an algorithm that determines
# whether a number is even or odd. Write a program that generates 100 random numbers
# and keeps a count of how many of those random numbers are even and how many of them
# are odd.

import random


def generateRandomNumber():
    randomNumber = random.randint(1, 10)
    return randomNumber


def isEven(number):
    if number % 2 == 0:
        return True
    else:
        return False


def printResults(numberOfEvenNumbers, numberOfOddNumbers):
    print("Out of a hundred, there were this number of even numbers {} and this number of odd numbers {}"
          .format(numberOfEvenNumbers, numberOfOddNumbers))


def main():
    evenNumbers = 0
    oddNumbers = 0
    for currentIteration in range(1, 101):
        randomNumber = generateRandomNumber()
        if isEven(randomNumber):
            evenNumbers += 1
        else:
            oddNumbers += 1

    printResults(evenNumbers, oddNumbers)


main()
