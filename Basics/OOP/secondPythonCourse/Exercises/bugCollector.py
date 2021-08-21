# A bug collector collects bugs everyday for five days. Write a program that keep a running total of the number of
# bugs collected during the five days. The lopp should ask for the number of bugs collected for each day,
# and when the loop is finished, the program should display the total number of bugs collected.


totalDays = 5
totalNumberOfBugs = 0

for currentDay in range(1, totalDays + 1):
    bugsCollected = int(input("How many bugs were collected on day " +  \
                              str(currentDay) + ": "))
    totalNumberOfBugs = totalNumberOfBugs + bugsCollected
print("The total number of bugs collected for all", totalDays, "days is", totalNumberOfBugs)
