numbers = [12,32,55,67,3,55,68,22,55,89,55,1,19,32]

# Exercise 1
print(numbers.count(55))

# Exercise 2
print(numbers.index(55))


# Exercise 3
# print(list(reversed(numbers)).index(55)-1)
print(len(numbers) - list(reversed(numbers)).index(55) - 1)

# Exercise 4
List = numbers[4:9]
print(numbers.index(55, 4, 10))

# Exercise 5
print(numbers.index(min(numbers)))


# Exercise 6
largest = numbers.index(max(numbers))
numbers[largest] = 777
print(numbers)

# Exercise 7
newList = sorted(numbers)[-3:]
print(newList)

# Exercise 8
print(sum(sorted(numbers)[:5]))


# Exercise 9
x = min(numbers[:len(numbers)//2])
print(x)

# Exercise 10
