# When an object is falling because of gravity, the following formula can be used to
# determine the distance the object falls in a specific time period:
#
# d = 1/2 g t(squared)
#
# The variables in the formula are as follows: d is the distance in meters,
# g is 9.8, and t is the amount of time, in seconds, that the objects has been
# falling. Write a function named fallind_distance that accepts an objects
# falling time(in seconds) as an argument. The function should return the distance,
# in meters, that the object has fallen during that time interval. Write a program that
# calls the function in a loop that passes the values 1 through 10 as arguments and displays the return
# value.

def falling_distance(fallingTime):
    gravity = 9.8
    distance = (1/2) * gravity * fallingTime**2
    return distance

def main():
    print("Time\tFalling Distance")
    for currentTime in range(1, 11):
        print(currentTime, "\t\t", format(falling_distance(currentTime), ".2f"))

main()