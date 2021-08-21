# Simple Dictionary
import string
from pprint import pprint

dict = {
    "a": 1,
    "b": 2
}

# Accessing dictionary items
print(dict["b"])

print()

# Dictionary items sum up
sum = dict["a"] + dict["b"]
print(sum)

print()

# Explain this key error
d = {
    "Name": "John",
    "Surname": "Smith"
}

print(d["Surname"])

print()

# Add new dictionary key
d = {"a": 1, "b": 2}
d["c"] = 3
print(d)

print()


# Apply function to dictionary items
def sumDictionaryValues(dict):
    sum = 0
    for i in dict:
        sum += dict[i]
    print(sum)


sumDictionaryValues(d)

print()


# Dictionary filtering
def dictionaryFiltering(dict):
    for key, value in list(dict.items()):
        if value > 1:
            del dict[key]
    print(dict)


dictionaryFiltering(d)

print()


# Create  a dictionary for keys a, b, c where each key has as a value a list from 1 to 20, 11 to 20, and 21 to 30
# respectively  and print out
def newDict():
    new_dict = {
        "a": list(range(1, 20)),
        "b": list(range(11, 20)),
        "c": list(range(21, 30))
    }
    pprint(new_dict)


newDict()

print()


# Multi level indexing: Access the third value of key b
def accessThirdValueFromAKey():
    new_dict = {
        "a": list(range(1, 20)),
        "b": list(range(11, 20)),
        "c": list(range(21, 30))
    }
    pprint(new_dict["b"][2])


accessThirdValueFromAKey()


print()


# Iterate dictionary
def iterateThroughDictionary():
    new_dict = {
        "a": list(range(1, 20)),
        "b": list(range(11, 20)),
        "c": list(range(21, 30))
    }

    for key, value in new_dict.items():
        pprint("{} has value {}".format(key, value))


iterateThroughDictionary()


print()


# Print alphabet
def printAlphabet():
    alphabet = {}
    for letter in string.ascii_lowercase:
        alphabet[letter] = letter
    pprint(alphabet)


printAlphabet()


