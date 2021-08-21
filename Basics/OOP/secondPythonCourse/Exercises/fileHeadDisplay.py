# Write a program that asks the user for the name of a file. The program should display only the first five
# lines of the files contents. If the file contains less than five lines, it should display the files entire contents

def main():
    maximumLinesToRead = 5
    linesRead = 0

    userFileName = input("Please enter the name of a file: ")

    readfile = open(userFileName, "r")

    line = readfile.readline()
    linesRead = linesRead + 1

    while line != "" and linesRead <= maximumLinesToRead:
        print(line.rstrip("\n"))
        line = readfile.readline()
        linesRead += 1

    readfile.close()

main()
