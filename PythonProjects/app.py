import json
from difflib import get_close_matches


data = json.load(open("data.json"))


def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys())) > 0:
        yn = input("Did you mean {} instead? Enter Y if yes, or N if no: ".format(get_close_matches(word, data.keys())[0]))
        if yn == "Y":
            return data[get_close_matches(word, data.keys())[0]]
        elif yn == "N":
            return "The word doesnt exist. Please double check it"
        else:
            return "We didnt understand your query"
    else:
        return "The word doesnt exist. Please double check it."


word = input("Enter word: ")

output = (translate(word))

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)


