# write a program that uses nested loops to draw this pattern:
#
#   ********
#   *******
#   ******
#   *****
#   ****
#   ***
#   **
#   *


for currentRow in range(7, 0, -1):
    for currentColumn in range(currentRow, 0, -1):
        print("*", end="")
    print()
