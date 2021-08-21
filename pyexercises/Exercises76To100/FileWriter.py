

def fileWriter():
    file = open("user_data.txt", "a+")

    while True:
        line = input("Please enter some text: ")
        if line == "SAVE":
            file.close()
            file = open("user_data_save_close.txt", "a+")
        elif line == "CLOSE":
            file.close()
            break
        else:
            file.write(line + "\n")


fileWriter()
