def wordCounter(filepath):
    word_counter = 0
    with open(filepath, "r")  as file:
        string = file.read()
        string_list = string.split(" ")

    for i in string_list:
        word_counter += 1
    print(word_counter)


wordCounter("words1.txt")

