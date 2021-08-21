def is_palindrome(string):
    backwards = string[::-1]
    return backwards.casefold() == string.casefold()


def palindrome_sentence(sentence):
    string = ""
    for char in sentence:
        if char.isalnum():
            string += char

    backwards = string[::-1]
    return backwards.casefold() == string.casefold()


word = input("Please enter a word to check: ")
if palindrome_sentence(word):
    print("'{}' is a palindrome".format(word))
else:
    print("'{}' is not a palindrome".format(word))

