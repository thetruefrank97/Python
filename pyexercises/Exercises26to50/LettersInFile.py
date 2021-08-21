import string


def lettersInAFile():
    with open("new.txt", "w") as file:
        for letter in string.ascii_lowercase:
            file.write(letter + "\n")


lettersInAFile()
