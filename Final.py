import json


# =====================================================================================================
def BurnedCalories():
    def DataOfWeightAndExercises():
        with open("burned_data.json") as json_file:
            return json.load(json_file)

    def OptionsOfWeights(dict_):
        for place in range(1, len(dict_["weight"]) + 1):
            print(place, ") ", dict_["weight"][place - 1])

    def ChooseAnOption():
        return int(input("PLease choose your weight number from the list above: ")) - 1

    def AskForDoneExercise():
        exercises = input("Write what exercises have you done, separated by commas: ")
        return exercises.split(",")

    def TakingExtraExercisesOut(dict_, ls):
        list_of_extras = []
        for i in ls:
            if i not in dict_:
                list_of_extras.append(i)
        return list_of_extras

    def AskForSpentTime(LS, ls):
        time = input("Write times spent in each exercise separated by commas: ")
        time = time.split(",")
        for exercise in ls:
            if exercise in LS:
                del time[LS.index(exercise)]
        return time

    def CalculatingBurnedCalories(dict_, all_, extras, place, time):
        calories_burned = 0
        for i in extras:
            all_.remove(i)
        for i in range(0, len(all_)):
            calories_burned = calories_burned + dict_[all_[i]][place] * float(time[i])
        return calories_burned

    def PrintAndSaveTheResultOfBurnedCalories(number, exercise):
        if len(exercise) > 0:
            str_ = ", ".join(exercise)
            result = f"Sorry, but {str_} is/are not in our list, but you burned {number} calories from others!!\n"
        else:
            result = f"You burned {number} calories!!\n"

        with open("burned_result.txt", "a") as b:
            b.write(result)
        print(result)

    def burned():
        dict_of_weight_and_exercises = DataOfWeightAndExercises()
        OptionsOfWeights(dict_of_weight_and_exercises)
        weight_option = ChooseAnOption()
        done_exercise = AskForDoneExercise()
        exercises_out_of_data = TakingExtraExercisesOut(dict_of_weight_and_exercises, done_exercise)
        lengths_of_trainings = AskForSpentTime(done_exercise, exercises_out_of_data)
        burned_calories = CalculatingBurnedCalories(dict_of_weight_and_exercises, done_exercise, exercises_out_of_data,
                                                    weight_option, lengths_of_trainings)
        PrintAndSaveTheResultOfBurnedCalories(burned_calories, exercises_out_of_data)

    burned()


# ====================================================================================================
def ConsumedCalories():
    def DataOfMealsAndCalories():
        with open("consumed_data.json") as json_file:
            return json.load(json_file)

    def AskingForEatenFoods():
        food = input("Write what you ate for breakfast separated by commas: ")
        return food.split(",")

    def TakingExtraFoodsOut(dict_, ls):
        list_of_extras = []
        for i in ls:
            if i not in dict_:
                list_of_extras.append(i)
        return list_of_extras

    def AskingForAmountsOfEatenFoods(LS, ls):
        amount = input("Amount of each food, separated by commas: ")
        amount = amount.split(",")
        for food in ls:
            if food in LS:
                del amount[LS.index(food)]
        return amount

    def CalculatingConsumedCalories(dict_, all_, extras, amount):
        calories = 0
        for i in extras:
            all_.remove(i)
        for i in range(0, len(all_)):
            calories = calories + dict_[all_[i]] * (float(amount[i]) / 100)
        return calories

    def PrintAndSaveTheResultOfConsumedCalories(number, food):
        if len(food) > 0:
            str_ = ", ".join(food)
            result = f"Sorry, but {str_} is/are not in our list, but you consumed {number} calories from others!!\n"
        else:
            result = f"You consumed {number} calories!!\n"

        with open("consumed_result.txt", "a") as c:
            c.write(result)
        print(result)

    def consumed():
        dict_of_products = DataOfMealsAndCalories()
        foods = AskingForEatenFoods()
        foods_out_of_data = TakingExtraFoodsOut(dict_of_products, foods)
        amounts = AskingForAmountsOfEatenFoods(foods, foods_out_of_data)
        consumed_calories = CalculatingConsumedCalories(dict_of_products, foods, foods_out_of_data, amounts)
        PrintAndSaveTheResultOfConsumedCalories(consumed_calories, foods_out_of_data)

    consumed()


# =====================================================================================================
def MealPlans():
    def DataOfMeals():
        with open("meal_types.json") as json_file:
            return json.load(json_file)

    def ChoseAMealType(dict_, key):
        for i in dict_[key]:
            print(dict_[key].index(i) + 1, ")", i)
        question = int(input("Please choose one of the meal plans by its number: "))
        return question - 1

    def PrintAndSaveTheScheduleOfMeal(dict_, extra, number):
        print("Your plan!!!\n")
        meal = ""
        for key in dict_:
            if key != extra:
                meal = meal + key + ": " + dict_[key][number] + "\n"

        with open("meal_result.txt", "a") as m:
            m.write(meal)
        print(meal)

    def meals():
        dict_of_meals = DataOfMeals()
        question = ChoseAMealType(dict_of_meals, "plans")
        PrintAndSaveTheScheduleOfMeal(dict_of_meals, "plans", question)

    meals()


# ======================================================================================================
def CalculateBurnedOrConsumedCalories():
    question = input("Calculate how much calories you burned or consumed?: ").lower()
    while (question != "burned" and question != "consumed"):
        print("There is no such option.")
        question = CalculateBurnedOrConsumedCalories()
    return question


def ExtraOptions():
    print(
        "1) Calculate how much calories you burned?\n2) Calculate how much calories you consumed?\n3) Choose one of the meal types.\n4) Exit")
    chosen = input("Please choose one of the options by their number: ")
    while (chosen != "1" and chosen != "2" and chosen != "3" and chosen != "4"):
        print("There is no such option.")
        chosen = input("Please choose one of the options by their number: ")
    return chosen


# ======================================================================================================
def main():
    question = CalculateBurnedOrConsumedCalories()
    if question == "burned":
        BurnedCalories()
    elif question == "consumed":
        ConsumedCalories()

    while True:
        next_question = ExtraOptions()
        if next_question == "1":
            BurnedCalories()
        elif next_question == "2":
            ConsumedCalories()
        elif next_question == "3":
            MealPlans()
        elif next_question == "4":
            print("You chose to exit.")
            break


main()

