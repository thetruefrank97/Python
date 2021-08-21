# write a program that displays a table of the Celsius temperatures 0 through 20
# and their fahrentheit equivalents. The formula for converting a temperature
# from celsius to fahrenheit is
#
# F = (9/5)C + 32
# Where F is the Fahrenheit temperature and C is the Celsius temperature. Your
# program must use a loop to display the table.

print("Celsius temperature\tFahrentheit Equivalent")
for currentCelsiusTemperature in range(21):
    fahrenheitTemperatureEquivalent = (9 / 5) * currentCelsiusTemperature + 32
    print(currentCelsiusTemperature, "\t\t\t\t\t", format(fahrenheitTemperatureEquivalent, ".2f"))

