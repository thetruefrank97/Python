# Assume that a file containing a series of integers is named numbers.txt and
# exists on the computers disk. Write a program that displays all of the numbers in the file

def main():
    numbersFile = open("numbers.txt", "r")

    line = numbersFile.readline()

    while line != "":
        print(line.rstrip("\n"))
        line = numbersFile.readline()

main()
