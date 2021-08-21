# Write a program that will ask the user to enter the amount of a purchase.
# The progam should then compute the state and county sales. Assume the state sales is
# 5 percent and the county sales tax is 2.5 percent. The program should display the amount
# of the purchase, the state sales tax, the county sales tax, the total sales tax, and the total
# of the sales(which is the sum of the amount of purchase plus the total sales tax).
#
# Hint: Use the value 0.025 to represent 2.5 percent, and 0.05 to represent 5 percent.

userAmountOfPurchase = float(input("Please enter the amount of purchase: "))

stateTax = 0.05 * userAmountOfPurchase

countyTax = 0.025 * userAmountOfPurchase

totalTax = stateTax + countyTax

totalSale = userAmountOfPurchase + totalTax

print("Amount of purchase $" + format(userAmountOfPurchase, ",.2f"),
      "State tax: $" + format(stateTax, ",.2f"),
      "County tax: $" + format(countyTax, ",.2f"),
      "total tax: $" + format(totalTax, ",.2f"),
      "total: $" + format(totalSale, ",.2f"), sep="\n")
