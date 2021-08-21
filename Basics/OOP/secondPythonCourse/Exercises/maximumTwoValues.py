# Write a function named max that accepts two integer values as arguments and returns
# the value that is the greater of the two. For example if 7 and 12 are passed as arguments to the
# function, the function should return 12. Use the function in a program that prompts the user to
# enter two integer values. The program should display the value that is the greater of the two.

firstValue = int(input("Please enter the first number: "))
secondValue = int(input("Please enter the second number: "))


def max(firstValue, secondValue):
    if firstValue > secondValue:
        print("The value {} is greater".format(firstValue))
        return firstValue
    else:
        print("The value {} is greater".format(secondValue))
        return secondValue


def main():
    max(firstValue, secondValue)


main()