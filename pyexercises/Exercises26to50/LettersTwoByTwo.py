import string


def lettersTwoByTwo():
    with open("letters.txt", "w") as file:
        for letters1, letters2 in zip(string.ascii_lowercase[0::2], string.ascii_lowercase[1::2]):
            file.write(letters1 + letters2 + "\n")


lettersTwoByTwo()
