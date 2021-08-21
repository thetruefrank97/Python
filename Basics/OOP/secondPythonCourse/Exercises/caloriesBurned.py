# Running on a particular treadmill you burn 4.2 calories per minute. Write a program that uses a loop
# to display the number of calories burned after 10, 15, 20, 25, and 30 minutes.

caloriesBurnedPerMinute = 4.2
for numberOfMinutes in range(10, 31, 5):
    numberOfCaloriesBurned = (numberOfMinutes / 1) * caloriesBurnedPerMinute
    print("You will burn", numberOfCaloriesBurned, "calories in", numberOfMinutes, "minutes")