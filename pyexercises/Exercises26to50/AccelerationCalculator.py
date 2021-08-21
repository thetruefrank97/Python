# Create a function that calculates acceleration given initial velocity v1, final velocity v2, start time t1, and end time t2.
# The formula for acceleration is: a = (V2 - V1)/(T2 - T1)

def accelerationCalculation(V1, V2, T1, T2):
    acceleration = (V2 - V1)/(T2 - T1)
    print(acceleration)


accelerationCalculation(0, 10, 0, 20)
