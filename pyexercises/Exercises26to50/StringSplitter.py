
def stringSplitter():
    wordCounter = 0
    string = input("Please enter a sentence: ")
    string_list = string.split(" ")
    for i in string_list:
        wordCounter += 1
    print(wordCounter)


stringSplitter()
