# Write a program with a loop that asks the user to enter a series of positive numbers.
# The user should enter a negative number to signal the end of the series. After all the
# positive numbers have been entered, the program should display their sum.

userNumber = float(input("Please enter the first number or a negative number to quit: "))
total = 0

while userNumber > -1:
    total = total + userNumber
    userNumber = float(input("Please enter the next number or a negative number to quit: "))
print("The sum of all the numbers you entered is", total)
