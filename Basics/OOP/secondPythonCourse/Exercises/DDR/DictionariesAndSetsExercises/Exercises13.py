
def iterateDictionaryInReverseSortedOrder(dict):
    for fruit in reversed(sorted(dict.keys())):
        print(fruit, dict[fruit])


def capitalizeEachStringOfAList(List):
    for i, word in enumerate(List):
        List[i] = word.capitalize()
    print(List)


def oddAndEvenNumbers(List):
    for i, number in enumerate(List):
        if number % 2 == 0:
            List[i] = List[i] / 2
        else:
            List[i] = List[i] * 2
    print(List)


def printSortedListWithoutDuplicates(List):
    for number in sorted(set(List)):
        print(number, end=" ")


def keysWithTheirFactorials():
    factorial = {}
    factorial[0] = 1
    for i in range(1, 8):
        factorial[i] = i * factorial[i - 1]
    print(factorial, end=" ")


def removeNthOccurrenceOfItem():
    L = [11, 23, 31, 4, 23, 45, 11, 23, 79, 23, 81, 43, 23]
    n = 3
    item = 23
    count = 0
    for i, num in enumerate(L):
        if num == item:
            count += 1
        if count == n:
            L.pop(i)
            break
    print(L)


def uniqueCityNames():
    D = {'Sam': 'Paris', 'Tom': 'London', 'Bob': 'Paris', 'Dev': 'Bareilly', 'Tim': 'Paris', 'Raj': 'London'}
    for city in set(D.values()):
        print(city.upper())


def encryptedMessage():
    message = "Hello World"
    encryptedMessage = ""
    for i, ch in enumerate(message):
        if i%2 == 0:
            encryptedMessage += chr(ord(ch) + 1)
        else:
            encryptedMessage += chr(ord(ch) - 1)
    print(encryptedMessage)

    dmessage = ""
    for i, ch in enumerate(encryptedMessage):
        if i%2 == 0:
            dmessage += chr(ord(ch) - 1)
        else:
            dmessage += chr(ord(ch) + 1)
    print(dmessage)


def encryptStringsOfList():
    L = ['this', 'that', 'here', 'there']
    # encrypt
    for i, word in enumerate(L):
        new_word = ""
        for ch in word:
            new_word += chr(ord(ch) + 1)
        L[i] = new_word
    print(L)

    # decrypt
    for i, word in enumerate(L):
        new_word = ""
        for ch in word:
            new_word += chr(ord(ch) - 1)
        L[i] = new_word
    print(L)


def listContainingDuplicateValues():
    L = [2, 9, 3, 4, 1, 2, 5, 7, 8, 3, 6]
    prev = None
    for item in sorted(L):
        if prev == item:
            print("A duplicate found")
            break
        prev = item
    else:
        print("No duplicates")


def main():
    D = {'apple': 210, 'banana': 100, 'grapes': 90, 'mango': 250, 'cherry': 225, 'guava': 80}
    L = ['this', 'that', 'the', 'hello world']
    listA = [15, 2, 4, 3, 8, 9]
    LL = [2, 4, 1, 6, 7, 8, 9, 7, 1, 2, 6]
    iterateDictionaryInReverseSortedOrder(D)
    print("\n")
    capitalizeEachStringOfAList(L)
    print("\n")
    oddAndEvenNumbers(listA)
    print("\n")
    printSortedListWithoutDuplicates(LL)
    print("\n")
    keysWithTheirFactorials()
    print("\n")
    removeNthOccurrenceOfItem()
    print("\n")
    uniqueCityNames()
    print("\n")
    encryptedMessage()
    print("\n")
    encryptStringsOfList()
    print("\n")
    encryptStringsOfList()
    print("\n")
    listContainingDuplicateValues()


main()
