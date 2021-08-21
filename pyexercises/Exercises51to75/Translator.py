
def translation():
    word = input("Please enter a word: ").lower()
    d = dict(weather="clima", earth="terra", rain="chuva")
    if word == "weather":
        print(d["weather"])
    elif word == "earth":
        print(d["earth"])
    elif word == "rain":
        print(d["rain"])
    else:
        print("That word could not be found")


translation()