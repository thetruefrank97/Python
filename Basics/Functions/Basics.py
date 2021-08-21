# def Greet(name):
#     print("Your name is : ", name)
#
#
# name = input("Enter your name : ")
# Greet(name)


# def print_blank_lines(n):
#     for i in range(n):
#         print("ha", end="")
#
#
# print_blank_lines(40)


# def simple_interest(p, r, t):
#     si = (p*r*t)/100
#     return si
#
#
# principal = 2000
# rate = 5
# time = 4
#
# interest = simple_interest(principal,rate,time)
#
# amount = principal + interest
#
# print(amount)


def func(a, b):
    s = a+b
    d = a-b
    p = a+b
    return s, d, p


def max_min_avg(L):
    return max(L),min(L),sum(L)/len(L)


marks = [92, 76, 98, 67, 88, 92, 89]

annual_rain = [11, 2, 23, 11, 9, 2, 1, 23, 13, 3, 11, 20]

maxmarks,minmarks,avgmarks = max_min_avg(marks)

max_rain,min_rain, avg_rain = max_min_avg(annual_rain)

print(maxmarks,minmarks,avgmarks)

print(max_rain,min_rain,avg_rain)



