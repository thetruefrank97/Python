from datetime import datetime


def calculateYourBirthYear():
    age = int(input("Please enter your current age: "))
    yearOfBirth = datetime.now().year - age
    print("We think you were born in {}".format(yearOfBirth))


calculateYourBirthYear()