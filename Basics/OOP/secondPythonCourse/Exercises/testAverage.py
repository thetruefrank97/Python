# Write a program that asks the user to enter five test scores. The prgram should display a letter grade for each score
# and the average test score. Write the following functions in the program:
#
# calc_average - this function should accept five test scores as arguments and return the average of the scores.
#
# determine_grade - This function should accept a test score as an argument and return a letter grade for the score based
# on the following grading scale:
#
#         Score            Letter Grade
#         90 - 100             A
#         80 - 89              B
#         70 - 79              C
#         60 - 69              D
#         Below 60             F


def calcAverage(score1, score2, score3 , score4, score5):
    average = (score1 + score2 + score3 + score4) / 5
    return average


def determineGrade(userScore):
    if userScore < 60:
        return "F"
    elif userScore < 70:
        return "D"
    elif userScore < 80:
        return "C"
    elif userScore < 90:
        return "B"
    else:
        return "A"


def askScores():
    score1 = float(input("Please enter score 1: "))
    score2 = float(input("Please enter score 2: "))
    score3 = float(input("Please enter score 3: "))
    score4 = float(input("Please enter score 4: "))
    score5 = float(input("Please enter score 5: "))

    return score1, score2, score3, score4, score5


def printTableOfResults(score1, score2, score3, score4, score5):
    print("Score\tLetter Grade\n" )
    print(str(score1) + "\t" + determineGrade(score1) \
          + "\t" + str(score2) + "\t" + determineGrade(score2) + \
         "\t" +  str(score3) + "\t" + determineGrade(score3)  \
          + "\t" + str(score4) + "\t" + determineGrade(score4) \
           + "\t" + str(score5) + "\t" + determineGrade(score5))


def main():
    score1, score2, score3, score4, score5 = askScores()
    print(printTableOfResults(score1, score2, score3, score4, score5))


main()


