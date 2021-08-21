
def displayLinesThatDontStartWithAHashtag():
    with open("data.txt", "r") as f:
        for line in f:
            if not line.startswith("#"):
                print(line, end="")


def displayFirst5Lines():
    with open("data.txt", "r") as f:
        for i in range(5):
            print(f.readline(), end="")


def displayLast5Lines():
    with open("data.txt","r") as f:
        for line in f.readlines()[-5::]:
            print(line, end="")


def copyContentsOfOneFileToAnother():
    with open("data.txt", "r") as f1:
        with open("new.txt", "w") as f2:
            f2.write(f1.read().replace(" ", "-"))


def copy_file(source, destination):
    f1 = open(source, "r")
    f2 = open(destination, "w")

    while True:
        s = f1.read(100)
        if s == "":
            break
        f2.write(s)
    f1.close()
    f2.close()


def compareFilesOneByOne():
    with open("data.txt", "r") as f1:
        with open("data1.txt", "r") as f2:
            count = 1
            while True:
                line1 = f1.readline()
                line2 = f2.readline()
                if line1 != line2:
                    print("Lines differ at line", count)
                    break
                if line1 == "":
                    print("Files are same")
                    break
                count += 1


def main():
    displayLinesThatDontStartWithAHashtag()
    print("\n")
    displayFirst5Lines()
    print("\n")
    displayLast5Lines()
    copyContentsOfOneFileToAnother()
    print()
    copy_file("data.txt", "data1.txt")
    print("\n")
    compareFilesOneByOne()





main()
