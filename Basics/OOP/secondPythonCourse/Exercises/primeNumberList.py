# This exercise assumes that you have already written the is_prime function
# in programming Exercise 17. Write another program that displays all of the prime
# numbers form 1 to 100. The program should have a lopp that calls the is_prime function

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
    for currentNumber in range(1, 101):
        if is_prime(currentNumber):
            print(currentNumber, end=" ")


main()



