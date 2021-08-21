# A prime number is a number that is only evenly divisible by itself and 1. For example the number 5 is prime
# because it can only be evenly divided by 1 and 5. The number 6, however, is not a prime because it can be divided
# evenly by 1, 2, 3, and 6. Write a boolean function named is_prime which takes an integer as an argument and returns
# true if the argument is a prime number, or false otherwise. Use the function in a program that prompts the user to enter
# a number and then displays a message indicating whether the number is prime.


def is_prime(number):
    evenDivisions = 0
    if number <= 1:
        return False
    for currentNumber in range(1, number + 1):
        if number % currentNumber == 0:
            evenDivisions = evenDivisions + 1
            if evenDivisions > 2:
                return False
    return True


def main():
    number = int(input("Please enter a number: "))
    if is_prime(number):
        print("The number is a prime number")
    else:
        print("The number is not a prime number")


main()
