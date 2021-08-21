
def addOneHundred(numbers):
    numbers.append(100)
    print(numbers)


def addTwoHundredAtBeginning(numbers):
    numbers[0] = 200
    print(numbers)


def addOneHundredFifty(numbers):
    numbers[3] = 150
    print(numbers)


def addNumbersToList(numbers):
     newNumbers = [12, 13, 14, 15]
     numbers.append(newNumbers)


def deleteElement(numbers):
    del numbers[4]
    print(numbers)


def deleteLastElement(numbers):
    del numbers[:-1]
    print(numbers)


def deleteFifthElement(numbers):
    del numbers[5]
    print(numbers)


def deleteFirstElement(numbers):
    del numbers[0]
    print(numbers)


def deleteAllElements(numbers):
    numbers.clear()
    print(numbers)


def deleteLastThreeElements(list):
    del list[-3:]


def main():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8]
    listA = [20, 30, 40, 50, 60, 70]

    addOneHundred(numbers)
    print()
    addTwoHundredAtBeginning(numbers)
    print()
    addOneHundredFifty(numbers)
    print()
    addNumbersToList(numbers)
    print()
    deleteElement(numbers)
    print()
    deleteLastElement(numbers)
    print()
    deleteFirstElement(numbers)
    print()
    deleteAllElements(numbers)
    print()
    deleteFifthElement(listA)
    print()


main()