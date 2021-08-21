def numberOfOccurrences(numbers):
    occurrences = 0
    numberToFind = 55
    for number in numbers:
        if number == numberToFind:
            occurrences += 1
    print("the amount of times the number {} is in the list is: {}".format(numberToFind, occurrences))


def numberOfIndex(numbers):
    numberToFind = 55
    index = 0
    for number in numbers:
        if number == numberToFind:
            index = numbers.index(number)
    print("The first occurence of the number {} is found in the position {}".format(numberToFind, index))


def lastOcurrenceIndex(numbers):
    numberToFind = 55
    numbers.reverse()
    number = numbers.index(numberToFind)
    numbers.reverse()
    print("The last occurence of the number {} is found in the position {}".format(numberToFind,
                                                                                   len(numbers) - number - 1))


def firstOcurrenceFromIndex4To9(numbers):
    newList = numbers[4:10]
    numberToFind = 55
    index = 0
    for number in newList:
        if number == numberToFind:
            index = newList.index(number)
    print("The first occurrence of the number {} in this portion of the list is in the position {}".format(numberToFind, \
                                                                                                           index))


def smallestElementIndex(numbers):
    print(numbers.index(min(numbers)))


def replaceLargestElementInList(numbers):
    numbers[numbers.index(max(numbers))] = 1000
    print(numbers)


def listWithThreeLargestNumbers(numbers):
    newList = sorted(numbers)[-3:]
    print(newList)


def sumSmallestElementsInList(numbers):
    newList = sorted(numbers)[0:5]
    sum = 0
    for number in newList:
        sum = sum + newList[newList.index(number)]
    print("The sum of the smallest elements in the list is {}".format(sum))


def minimumValueFirstHalfOfList(numbers):
    newList = numbers[0:(int(len(numbers)/2))]
    minimumValue = sorted(newList)[0]
    print("The minimum value in the first half of the list is {}".format(minimumValue))


def main():
    numbers = [12, 32, 55, 67, 3, 55, 68, 22, 55, 89, 55, 1, 19, 32]
    numberOfOccurrences(numbers)
    print()
    numberOfIndex(numbers)
    print()
    lastOcurrenceIndex(numbers)
    print()
    firstOcurrenceFromIndex4To9(numbers)
    print()
    smallestElementIndex(numbers)
    print()
    replaceLargestElementInList(numbers)
    print()
    listWithThreeLargestNumbers(numbers)
    print()
    sumSmallestElementsInList(numbers)
    print()
    minimumValueFirstHalfOfList(numbers)


main()
