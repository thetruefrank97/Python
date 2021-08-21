fruit = {
    "orange": "a sweet orange, citrus fruit",
    "apple" : "good for making cider",
    "lemon": "a sour, yellow citrus fruit",
    "grape" : "a small, sweet fruit grwoing in bunches",
    "lime" : "a sour, green citrus fruit"
}

print(fruit)
while True:
    dict_key = input("please enter a fruit: ")
    if dict_key == "quit":
        break
    if dict_key in fruit:
        description = fruit.get(dict_key)
        print(description)
    else:
        print("we dont have a " + dict_key)

for i in range(10):
    for snack in fruit:
        print(snack + " is " + fruit[snack])
    print("-" * 40)

ordered_keys = list(fruit.keys())
ordered_keys.sort()
for f in ordered_keys:
    print(f + " _ " + fruit[f])


fruit_keys = fruit.keys()
fruit["tomato"] = "not nice with ice cream"
print(fruit_keys)


