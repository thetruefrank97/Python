data = [3,5,9,8]
numbers = [2, 4, 6, 7, 9, 10]


for number in data:
    print(number)

even_count = 0
for number in numbers:
    if number % 2 == 0:
        even_count = even_count + 1
print(even_count)

message = "Hello World"

emessage = ""

for ch in message:
    emessage = emessage + chr(ord(ch) + 1)
print(emessage)

dmessage = ""
for ch in emessage:
    dmessage = dmessage + chr(ord(ch) - 1)
print(dmessage)