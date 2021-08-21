# height exercise
ht_inches = float(input("Enter the height in inches: "))
ft = ht_inches
inches = ht_inches % 12
print(ft, "feet", inches, "inches")

# Temperature exercise
tc = int(input("Enter the temperature in Celsius : "))
tf = tc * 1.8 + 32
print("Temperature in Fahrenheit is ", tf)

# Student grade calculation exercise
name = input("Enter name : ")
marks_maths = int(input("Enter marks in maths : "))
marks_physics = int(input("Enter marks in physics : "))
marks_biology = int(input("Enter marks in biology : "))
total_marks = marks_maths + marks_physics + marks_biology
percentage = (total_marks / 300) * 100
print(name, percentage)


# BMI index
height = float(input("Enter your height in cms : "))
weight = float(input("Enter your weight in kgs : "))
height = height * 0.01
bmi = weight / (height * height)
print("Your body mass index is : ", bmi)


# Circumference and area exercise
PI = 3.141519
r = float(input("Enter radius of the circle : "))
area = PI * r * r
circumference = 2 * PI * r
print("Area is : ", area)
print("Cirucumference is : ", circumference)




