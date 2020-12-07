import json
from HashMap_MB import *

#   Loads json for 3 data files
def json_load():
    with open('Data_Activities.json') as json_file:
        activities_data = json.load(json_file)

    with open("Data_Food.json") as json_file:
        food_data = json.load(json_file)

    with open("Data_Meal_Types.json") as json_file:
        meal_data = json.load(json_file)

    return activities_data, food_data, meal_data

#   Converts 3 json files to double linked lists
def json_to_hashmap(activities_data, food_data, meal_data):
    ActivitiesHash = HashMap()
    for elem in activities_data:
        ActivitiesHash.put(elem,Activities(elem, activities_data[elem]))

    FoodHash = HashMap()
    for elem in food_data:
        FoodHash.put(elem,Food(elem, food_data[elem]))

    MealHash = HashMap()
    for elem in meal_data:
        MealHash.put(elem,Meal(elem, meal_data[elem]))

    return ActivitiesHash, FoodHash, MealHash

#   Create class for entry of our Activity data
class Activities:
    def __init__(self, name, value):
        self.name = name
        self.value = value

#   Create class for entry of our Food data
class Food:
    def __init__(self, name, value):
        self.name = name
        self.value = value

#   Create class for entry of our Meal data
class Meal:
    def __init__(self, name, value):
        self.name = name
        self.value = value

#   Calculation of burned calories
def BurnedCalories(ActivitiesHash):
    #   Prints options of weight categories
    def OptionsOfWeights(ActivitiesHash):
        options = ActivitiesHash.get("weight")
        for place in range(1, len(options) + 1):
            print(place, ") ", options[place - 1])
    
    #   User chooses his weight category
    def ChooseAnOption():
        return int(input("Please choose your weight number from the list above: ")) - 1

    #   User inputs done exercises
    def AskForDoneExercise():
        exercises = input("Write what exercises have you done, separated by commas: ")
        return exercises.split(",")

    #   Parse done exercises to see which are present in our Activities data
    #   Get calories for exercises present in Activites data
    #   From done exercises get list of extra exercises
    def TakingExtraExercisesOut(ActivitiesHash, done_exercise, weight_option):
        list_of_exercises = []
        list_of_calories = []
        for i in done_exercise:
            if ActivitiesHash.get(i) is not None:
                list_of_exercises.append(i)
                list_of_calories.append(ActivitiesHash.get(i)[weight_option])
        list_of_extras = set(done_exercise) - set(list_of_exercises)
        return  list_of_extras, list_of_calories

    #   User inputs time he spent doing the exercises
    def AskForSpentTime(done_exercise, list_of_extras):
        time = input("Write times spent in each exercise separated by commas: ")
        time = time.split(",")
        for exercise in list_of_extras:
            if exercise in done_exercise:
                del time[done_exercise.index(exercise)]
        return time

    #   Calculating burned calories
    def CalculatingBurnedCalories(list_of_calories, done_exercise, list_of_extras, lengths_of_trainings):
        calories_burned = 0
        for i in list_of_extras:
            done_exercise.remove(i)
        for i in range(0, len(done_exercise)):
            calories_burned = calories_burned + list_of_calories[i] * float(lengths_of_trainings[i])
        return calories_burned

    # Print extra exercises and burned calories and write it in .txt file
    def PrintAndSaveTheResultOfBurnedCalories(calories_burned, list_of_extras):
        if len(list_of_extras) > 0:
            str_ = ", ".join(list_of_extras)
            result = f"Sorry, but {str_} is/are not in our list, but you burned {calories_burned} calories from others!!\n"
        else:
            result = f"You burned {calories_burned} calories!!\n"

        with open("burned_result.txt", "a") as b:
            b.write(result)
        print(result)

    #   Execution of burned calories calculation
    def burned(ActivitiesHash):
        OptionsOfWeights(ActivitiesHash)
        weight_option = ChooseAnOption()
        done_exercise = AskForDoneExercise()
        list_of_extras, list_of_calories = TakingExtraExercisesOut(ActivitiesHash, done_exercise, weight_option)
        lengths_of_trainings = AskForSpentTime(done_exercise, list_of_extras)
        calories_burned = CalculatingBurnedCalories(list_of_calories, done_exercise, list_of_extras, lengths_of_trainings)
        PrintAndSaveTheResultOfBurnedCalories(calories_burned, list_of_extras)

    burned(ActivitiesHash)

#   Calculation of consumed calories
def ConsumedCalories(FoodHash):
    def AskingForEatenFoods():
        food = input("Write what you ate for breakfast separated by commas: ")
        return food.split(",")

    def TakingExtraFoodsOut(FoodHash, foods):
        list_of_food = []
        list_of_calories = []
        for i in foods:
            if FoodHash.get(i) is not None:
                list_of_food.append(i)
                list_of_calories.append(FoodHash.get(i))
        list_of_extras = set(foods) - set(list_of_food)
        return list_of_extras, list_of_calories

    #   User inputs amount of eaten food
    def AskingForAmountsOfEatenFoods(foods, list_of_extras):
        amount = input("Amount of each food, separated by commas: ")
        amount = amount.split(",")
        for food in list_of_extras:
            if food in foods:
                del amount[foods.index(food)]
        return amount

    #   Calculating consumed calories
    def CalculatingConsumedCalories(list_of_calories, foods, foods_out_of_data, amounts):
        calories = 0
        for i in foods_out_of_data:
            foods.remove(i)
        for i in range(0, len(foods)):
            calories = calories + list_of_calories[i] * (float(amounts[i]) / 100)
        return calories

    # Print extra food and consumed calories and write it in .txt file
    def PrintAndSaveTheResultOfConsumedCalories(consumed_calories, foods_out_of_data):
        if len(foods_out_of_data) > 0:
            str_ = ", ".join(foods_out_of_data)
            result = f"Sorry, but {str_} is/are not in our list, but you consumed {consumed_calories} calories from others!!\n"
        else:
            result = f"You consumed {consumed_calories} calories!!\n"

        with open("consumed_result.txt", "a") as c:
            c.write(result)
        print(result)

    #   Execution of consumed calories calculation
    def consumed():
        foods = AskingForEatenFoods()
        list_of_extras, list_of_calories = TakingExtraFoodsOut(FoodHash, foods)
        amounts = AskingForAmountsOfEatenFoods(foods, list_of_extras)
        consumed_calories = CalculatingConsumedCalories(list_of_calories, foods, list_of_extras, amounts)
        PrintAndSaveTheResultOfConsumedCalories(consumed_calories, list_of_extras)

    consumed()

#   Choosing meal plan
def MealPlans(MealHash):
    #   User chooses meal category
    def ChoseAMealType(MealHash):
        options = MealHash.get("plans")
        for place in range(1, len(options) + 1):
            print(place, ") ", options[place - 1])
        question = int(input("Please choose one of the meal plans by its number: "))
        return question - 1

    #   Print the chosen meal
    def PrintAndSaveTheScheduleOfMeal(MealHash, question):
        print("Your plan!!!\n")
        meal = ""

        for elem in MealHash._hashtable:
            if elem != None:
                for i in range(len(elem)):
                    if elem[i].name != "plans":
                        meal = meal + elem[i].name + ": \n" + elem[i].value[question] + "\n"

        with open("meal_result.txt", "a") as m:
            m.write(meal)
        print(meal)

    #   Execution of meal type choice
    def meals(MealHash):
        question = ChoseAMealType(MealHash)
        PrintAndSaveTheScheduleOfMeal(MealHash, question)

    meals(MealHash)

#   Asks user to choose between consumed and burned options
def CalculateBurnedOrConsumedCalories():
    question = input("Calculate how much calories you burned or consumed?: ").lower()
    while (question != "burned" and question != "consumed"):
        print("There is no such option.")
        question = CalculateBurnedOrConsumedCalories()
    return question

#   Recursive part where user can run program as much as he wants
def ExtraOptions():
    print(
        "1) Calculate how much calories you burned?\n"
        "2) Calculate how much calories you consumed?\n"
        "3) Choose one of the meal types.\n"
        "4) Exit")
    chosen = input("Please choose one of the options by their number: ")
    while (chosen != "1" and chosen != "2" and chosen != "3" and chosen != "4"):
        print("There is no such option.")
        chosen = input("Please choose one of the options by their number: ")
    return chosen

#   Main function which executes the whole program
def main():
    activities_data, food_data, meal_data = json_load()
    ActivitiesHash, FoodHash, MealHash = json_to_hashmap(activities_data, food_data, meal_data)
    question = CalculateBurnedOrConsumedCalories()

    if question == "burned":
        BurnedCalories(ActivitiesHash)
    elif question == "consumed":
        ConsumedCalories(FoodHash)

    while True:
        ActivitiesHash, FoodHash, MealHash = json_to_hashmap(activities_data, food_data, meal_data)
        next_question = ExtraOptions()
        if next_question == "1":
            BurnedCalories(ActivitiesHash)
        elif next_question == "2":
            ConsumedCalories(FoodHash)
        elif next_question == "3":
            MealPlans(MealHash)
        elif next_question == "4":
            print("You chose to exit.")
            break

main()
