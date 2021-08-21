# Land calculation
#
# One acre of land is equivalent to 43,560 square feet. Write a program that asks the user
# to enter the total square feet in a tract of land and calculates the number of acres in the tract.
#
# Hint: Divide the amount entered by 43, 560 to get the number of acres.

oneAcreOfLandSize = 43560
userTotalSquareFeet = int(input("Please enter the total amount of square feet: "))

numberOfAcres = (userTotalSquareFeet / oneAcreOfLandSize) * 1

print("Number of acres: " + format(numberOfAcres, ".2f"))




