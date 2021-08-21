# At one college, the tuition for a fulltime student is $8000 per semester.
# It has been announced that the tuition will increase by 3% each year for
# the next 5 years. Write a program with a loop that displays the projected semester
# tuition amount for the next 5 years.

currentTuition = 8000

print("Year", "\t", "Current tuition")
for currentYear in range(1, 6):
    currentTuition = currentTuition + ((3/100) * currentTuition)
    print(currentYear, "\t\t", format(currentTuition, ".2f"))
