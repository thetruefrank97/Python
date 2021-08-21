# Write a program that gives a simple maths quizzes. The program should display
# two random numbers that are to be added, such as:
#                 247
#                 + 129
# The program should allow the student to enter the answer. If the answer is correct, a message
# of congratulations should be displayed. If the answer is incorrect, a message showing the correct
# answer should be displayed.

import random

randomNumber1 = random.randint(1, 250)
randomNumber2 = random.randint(1, 250)


def askQuestion():
    global randomNumber1
    global randomNumber2
    userAnswer = int(input("What is " + str(randomNumber1) + " + " + str(randomNumber2) + " ?: "))
    return userAnswer


def checkAnswer(userAnswer):
    global randomNumber1
    global randomNumber2
    correctAnswer = randomNumber1 + randomNumber2
    if userAnswer == correctAnswer:
        print("Congratulations!")
    else:
        print("You are a moron")


def main():
    userAnswer = askQuestion()
    checkAnswer(userAnswer)


main()
