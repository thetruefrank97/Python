# Create a program that generates a password of 6 random alphanumeric characters in the range

import random


def randomCharacters():
    characters = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
    chosen = random.sample(characters, 6)
    password = " ".join(chosen)
    print(password)


randomCharacters()