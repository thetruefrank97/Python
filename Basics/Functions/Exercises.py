numbers = [10, 20, 30, 40]


# Exercise 1
# def multiply_entries(L, a):
#     for i in range(len(L)):
#         L[i] = L[i]*a
#
#
# multiply_entries(numbers, 4)
# print(numbers)


#  Exercise 2
# def sum_digits(n):
#     s = 0
#     while n != 0:
#         s = s + n % 10
#         n //= 10
#     return s
#
#
# print(sum_digits(4567))

# Exercise 3
# def do_nothing():
#     pass
#
#
# do_nothing()

#  Exercise 4
# def number_vowels_consonants(s):
#     vowels = 0
#     consonants = 0
#     for ch in s:
#         if ch.isalpha():
#             if ch.lower() in "aeiou":
#                 vowels = vowels + 1
#             else:
#                 consonants = consonants + 1
#     return vowels, consonants
#
#
# text = "Hello World"
# v, w = number_vowels_consonants(text)
# print(v, w)

# Exercise 5
def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
        else:
            return True


# print(is_prime(4))
# print(is_prime(5))


# Exercise 6
# def factorial(n):
#     factorial = 1
#     while n > 0:
#         factorial = factorial * n
#         n = n - 1
#     return factorial
#
#
# print(factorial(4))


# Exercise 7
# def calculcator(a,b):
#     x = a + b
#     y = a - b
#     z = a * b
#     return x, y, z
#
#
# print(calculcator(4, 6))


#  Exercise 8
# def find(data, value):
#     for item in data:
#         if item == value:
#             return True
#     return False
#
#
# print(find(numbers, 6))

# Exercise 9
# def fizzbuzz(value):
#     if value % 3 == 0:
#         return "Fizz"
#     elif value % 5 == 0:
#         return "Buzz"
#     elif value % 3 == 0 and value % 5 == 0:
#         return "FizzBuzz"
#     return value
#
#
# def func(x):
#     for i in range(1, x+1):
#         print(fizzbuzz(i))
#
#
# func(50)


#  Exercise 10
# def integers_list(data):
#     even = 0
#     odd = 0
#     for number in data:
#         if number % 2 == 0:
#             even = even + 1
#         else:
#             odd = odd + 1
#     return even, odd
#
#
# print(integers_list(numbers))


def twin_primes(x, y):
    tp = []
    for i in range(x, y + 1):
        if is_prime(i) and is_prime(i + 2):
            tp.append((i, i + 2))
    return tp


print(twin_primes(10, 70))
