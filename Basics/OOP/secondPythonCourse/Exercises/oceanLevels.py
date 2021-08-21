# Assuming the oceans level is currently rising at about 1.6 millimeters per year,
# create an application that displays the number of millimeters that the ocean will
# have risen each year for the next 25 years.

#
# if 1 year = 1.6 millimeters
# then 0.5 years = ?
print("Year\t", "Sea Level Rise\n")
for currentYear in range(1, 26):
    seaLevelRise = currentYear * 1.6
    print(currentYear, "\t\t",  format(seaLevelRise, ".2f"))
