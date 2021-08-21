def twoStringsByInput():
    s1 = input("please enter the first string: ")
    s2 = input("Please enter the second string: ")
    commonCharacters = list(set(s1) & set(s2))
    return commonCharacters


def commonWords():
    string1 = "Life has no remote, get up and change it yourself"
    string2 = "Life has no ctrl+z"
    commonWords = set(string1.split(" ")) & set(string2.split(" "))
    return commonWords


def uniqueItemsInAList(List):
    return len(set(List))


def filterDuplicates(List):
    newList = list(set(List))
    return newList


def vowelsAndConsonants():
    text = input("Enter a string: ")
    vowels = set("aeiou")
    consonants = set('bcdfghjklmnpqrstvwxyz')
    v = vowels & (set(text))
    c = consonants & (set(text))
    return v, c


def orderNeutralEqualityTest(L1, L2):
    if set(L1) == set(L2):
        return "These two lists are equal"
    else:
        return "They arent equal"


def elementsNotInEveryList():
    L1 = [1, 2, 3, 7]
    L2 = [2, 3, 4, 5]
    newlist = []
    newlist = set(L1) - set(L2)
    return newlist


def commonCharactersInThreeStrings(s1, s2, s3):
    return set(s1) & set(s2) & set(s3)


def main():
    L1 = [1, 2, 3, 4]
    L2 = [2, 3, 1, 4]
    list = ["Hello", "War", "Worlds", "Saiyan", "Vegeta", "Nappa", "Vegeta", "Nappa"]
    L = [12, 44, 46, 32, 12, 43, 55, 86, 43]
    s1 = "Broly"
    s2 = "Goku"
    s3 = "Vegeta"
    print(twoStringsByInput())
    print()
    print(commonWords())
    print()
    print(uniqueItemsInAList(list))
    print()
    print(sorted(filterDuplicates(L)))
    print()
    print(vowelsAndConsonants())
    print()
    print(orderNeutralEqualityTest(L1, L2))
    print()
    print(elementsNotInEveryList())
    print()
    print(commonCharactersInThreeStrings(s1, s2, s3))
    print()


main()

