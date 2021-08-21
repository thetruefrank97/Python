# There are three seating categories at a stadium. For a softball game,
# Class A seats cost $20, Class B seats cost $15, and Class C seats cost $10.
# Write a program that asks how many tickets for each class of seats were sold, and then
# displays the amount of income generated from ticket sales.

def calculateClassATicketSales(classATicketBought):
    classASales = classATicketBought * 20
    return classASales


def calculateClassBTicketSales(classBTicketBought):
    classBSales = classBTicketBought * 15
    return classBSales


def calculateClassCTicketSales(classCTicketBought):
    classCSales = classCTicketBought * 10
    return classCSales


def calculateTotalSales(classASales, classBSales, classCSales):
    totalSales = classASales + classBSales + classCSales
    return totalSales


def printSalesReport(classASales, classBSales, classCSales, totalSales):
    print("\nClass A Sales: $" + format(classASales, ",.2f"), \
          "Class B Sales: $" + format(classBSales, ",.2f"), \
          "Class C Sales: $" + format(classCSales, ",.2f"), \
          "Total sales: $" + format(totalSales, ",.2f"), sep="\n")


def main():
    classATicketsBought = int(input("How many tickets were bought for class A: "))
    classBTicketsBought = int(input("How many tickets were bought for class B: "))
    classCTicketsBought = int(input("How many tickets were bought for class C: "))

    classASales = calculateClassATicketSales(classATicketsBought)
    classBSales = calculateClassBTicketSales(classBTicketsBought)
    classCSales = calculateClassCTicketSales(classCTicketsBought)

    totalSales = calculateTotalSales(classASales, classBSales, classCSales)

    printSalesReport(classASales, classBSales, classCSales, totalSales)


main()




