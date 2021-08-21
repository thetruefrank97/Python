# Please write a function that calculates liquid volume in a sphere using the following formula.
# The radius r  is always 10, so consider making it a default parameter.

def liquidVolumeCalculator(h, r=10):
    PI = 3.14
    liquidVolume = ((4*PI*r**3)/3) - (PI * h ** 2 * (3 * r - h) / 3)
    return liquidVolume


print(liquidVolumeCalculator(2))
