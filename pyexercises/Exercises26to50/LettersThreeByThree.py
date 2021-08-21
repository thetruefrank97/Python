import string


def lettersThreeByThree():
    with open("letterThreeByThree.txt", "w") as file:
        for x, y , z in zip(string.ascii_lowercase[0::3], string.ascii_lowercase[1::3], string.ascii_lowercase[2::3]):
            file.write(x + y + z + "\n")


lettersThreeByThree()