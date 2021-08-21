def advancedWordCounter(filepath):
    with open(filepath, "r") as file:
        text = file.read()
    text.replace(",", " ")
    string_list = text.split(" ")
    print(len(string_list))


advancedWordCounter("words2.txt")
