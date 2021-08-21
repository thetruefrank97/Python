n = 1
while n <= 10:
    print("Hello " * n)
    n = n + 2
print("World")


L = [1, 4, 5, 2, 3, 9, 7, 8, 9, 1]
n = 2
while n in L:
    L.remove(n)
print(L)

name = input(f"Enter your name in title case : ")
while not name.istitle():
    print("Wrong input")
    name = input(f"Enter your name in title case : ")
print(name)


fruit_prices = {
    "apple": 210,
    "banana": 100,
    "grapes":90
}

done = False

while not done:
    fruit = input("Enter fruit name : ")
    price = int(input("Enter price : "))
    fruit_prices[fruit] = price
    if input("Want to enter more(y/n) ") == "n":
        done = True

print(fruit_prices)



