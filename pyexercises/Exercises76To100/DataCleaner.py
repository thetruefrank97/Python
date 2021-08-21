
with open("countries_raw.txt", "r") as file:
    content = file.readlines()


content = [i.strip("\n") for i in content if "\n" in i]
content = [i for i in content if i != ""]
content = [i for i in content if len(i) != 1]


with open("countries_clean.txt", "w") as file:
    for i in content:
        file.write(i+"\n")
