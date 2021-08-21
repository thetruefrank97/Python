# Write a program that calculates the amount of money a person earn
# over a period of time if his or her salary is one penny the first day,
# two pennies the second day, and continues to double each day. The program
# should ask the user for the number of days. Display a table showing what the
# salary was for each day, and then show the total pay at the end of the period.
# The output should be displayed in a dollar amount, not the number of pennies

numberOfDaysWorked = int(input("Please enter how many days you worked: "))
payPerDay = 0.01
totalNumberOfPennies = 0

print("Day\tSalary\n-----\t-------")
for currentDay in range(numberOfDaysWorked):
    penniesForTheDay = 2 ** currentDay
    totalNumberOfPennies = totalNumberOfPennies + penniesForTheDay
    print(currentDay + 1, "\t", penniesForTheDay)

totalPay = totalNumberOfPennies * payPerDay
print("\ntotalPay: $", totalPay)