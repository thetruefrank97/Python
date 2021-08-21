# In physics, an object that is in motion is said to have kinetic energy. The following forula can be
# used  to determine a moving objects kinetic energy:
#
# KE = 1/2 x m * v(squared)
#
# The variables in the formula are as follows: KE is the kinetic energy, m is the objects mass
# in kilograms, and v is the objects velocity in meters per second. Write a function named
# kinetic_energy that accepts an objects mass(in kilograms) and velocity(in meters per second) as
# arguments. The function should return the amount of kinetic energy that the object has.
# Write a program that asks the user to enter the values for mass and velocity, and then calls
# the kinetic_energy function to get the objects kinetic energy
import math


def kinetic_energy(mass, velocity):
    KE = 1/2 * mass * math.pow(velocity, 2)
    return KE

def main():
    mass = float(input("Please enter the mass in kilograms: "))
    velocity = float(input("Please enter the velocity in meters per second: "))

    print("The kinetic energy of the object is " + format(kinetic_energy(mass, velocity), ".2f"))


main()