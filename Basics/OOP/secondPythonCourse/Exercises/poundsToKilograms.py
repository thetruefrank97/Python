# Pounds to kilograms
#
# One pound is equivalent to 0.454 kilograms. Write a program that asks
# the user to enter the mass of an object in pounds and then calculates and displays
# the mass of the object in kilograms.

ONE_POUND_TO_KILOGRAMS = 0.454

userInput = float(input("Please enter a number to convert to kilograms: "))

userPoundsToKilograms = userInput * ONE_POUND_TO_KILOGRAMS

print(userInput, " pounds converted to kilograms is", format(userPoundsToKilograms, ".2f"))
