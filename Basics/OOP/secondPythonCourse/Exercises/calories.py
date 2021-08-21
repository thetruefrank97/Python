# A nutritionist who works for a fitness club helps memebers by evaluating their diets. As part
# of her evaluation, she asks memebers for the number of fat grams and carbohydrate grams that they
# consumed in a day. Then, she calculates the number of calories that result from the fat, using the
# following formula:
#
# calories from fat = fat grams x 9
#
# Next, she calculates the number of calories that result from the carbohydrates, using the following
# formula:
#
# calories from carbs = carb grams x 4
#
# The nutritionist asks you to write a program that will make these calculations.


def calculateCaloriesFromFat(fatGrams):
    caloriesFromFat = fatGrams * 9
    return caloriesFromFat


def calculateCaloriesFromCarbohydrates(carbGrams):
    caloriesFromCarbs = carbGrams * 4
    return caloriesFromCarbs


def main():
    userFatGrams = float(input("What are your number of fat grams: "))
    userCarbohydrateGrams = float(input("What are your number of carbohydrate grams: "))

    caloriesFromFat = calculateCaloriesFromFat(userFatGrams)
    caloriesFromCarbs = calculateCaloriesFromCarbohydrates(userCarbohydrateGrams)

    print("\nCalories from Fat: {}".format(caloriesFromFat, ".2f"), \
          "Calories from carbs: {}".format(caloriesFromCarbs, ".2f"), sep="\n")


main()
