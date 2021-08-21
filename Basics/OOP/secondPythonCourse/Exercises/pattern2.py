# Write a program that uses nested loops to draw this pattern
#
#     ##
#     # #
#     #  #
#     #   #
#     #    #
for row in range(6):
    print("#",end="", sep="")
    for spaces in range(row):
        print(" ", end="", sep="")
    print("#", sep="")
