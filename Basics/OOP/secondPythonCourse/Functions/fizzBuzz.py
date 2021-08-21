def fizzBuzz(n: int) -> str:
    if n % 15 == 0:
        return "fizz buzz"
    elif n % 3 == 0:
        return "fizz"
    elif n % 5 == 0:
        return "buzz"
    else:
        return str(n)


input("Play Fizz Buzz. Press ENTER to start")
print()

next_number = 0
while next_number < 99:
    next_number += 1
    print(fizzBuzz(next_number))
    next_number += 1
    correct_answer = fizzBuzz(next_number)
    players_answer = input("Your go: ")
    if players_answer != correct_answer:
        print("You lose, the correct answer was {}".format(correct_answer))
        break
else:
    print("Well done, your reached {}".format(next_number))


# x = 1
# while x < 100:
#     print(fizzBuzz(x))
#     x += 1

# for i in range(1, 101):
#     print(fizzBuzz(i))
