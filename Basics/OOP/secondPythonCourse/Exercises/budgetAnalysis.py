# Write a program that asks a user to enter the amount that he or she has budgeted
# for a month. A loop should then prompt the user to enter each of his or her expenses
# for the month and keep running total. When the loop finishes, the program should display
# the amount that the user is over or under budget.

budget = float(input("Please enter how much you have budgeted for the month: "))
totalExpenses = 0

for day in range(1, 31):
    expenses = float(input("Please enter your expense for day " + str(day) + ": "))
    totalExpenses = totalExpenses + expenses

if totalExpenses > budget:
    print("You are well over your budget homie")
else:
    print("You are fine homie")

