import json
from DoubleLinkedList_MB import *

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
#   Linked list for Activities
def json_to_activites_linked_list(activities_data):
    ActivitiesDLL = DoubleLinkedList()
    for elem in activities_data:
        temp = Activities(elem, activities_data[elem])
        ActivitiesDLL.addLast(temp)
    return ActivitiesDLL
#   Linked list for Food
def json_to_food_linked_list(food_data):
    FoodDLL = DoubleLinkedList()
    for elem in food_data:
        temp = Food(elem, food_data[elem])
        FoodDLL.addLast(temp)
    return FoodDLL
#   Linked list for Meals
def json_to_meal_linked_list(meal_data):
    MealDLL = DoubleLinkedList()
    for elem in meal_data:
        temp = Meal(elem, meal_data[elem])
        MealDLL.addLast(temp)
    return MealDLL

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
def BurnedCalories(ActivitiesDLL):
    #   Prints options of weight categories
    def OptionsOfWeights(ActivitiesDLL):
        for place in range(1, len(ActivitiesDLL.HeadValue.DataValue.value) + 1):
            print(place, ") ", ActivitiesDLL.HeadValue.DataValue.value[place - 1])

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
    def TakingExtraExercisesOut(ActivitiesDLL, done_exercise, weight_option):
        list_of_exercises = []
        list_of_calories = []
        while ActivitiesDLL.HeadValue is not None:
            for i in done_exercise:
                if i == ActivitiesDLL.HeadValue.DataValue.name:
                    list_of_exercises.append(i)
                    list_of_calories.append(ActivitiesDLL.HeadValue.DataValue.value[weight_option])
            ActivitiesDLL.HeadValue = ActivitiesDLL.HeadValue.NextValue
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
    def burned():
        OptionsOfWeights(ActivitiesDLL)
        weight_option = ChooseAnOption()
        done_exercise = AskForDoneExercise()
        list_of_extras, list_of_calories = TakingExtraExercisesOut(ActivitiesDLL, done_exercise, weight_option)
        lengths_of_trainings = AskForSpentTime(done_exercise, list_of_extras)
        calories_burned = CalculatingBurnedCalories(list_of_calories, done_exercise, list_of_extras, lengths_of_trainings)
        PrintAndSaveTheResultOfBurnedCalories(calories_burned, list_of_extras)

    burned()

#   Calculation of consumed calories
def ConsumedCalories(FoodDLL):
    #   User inputs eaten foods
    def AskingForEatenFoods():
        food = input("Write what you ate for breakfast separated by commas: ")
        return food.split(",")

    #   Parse eaten food to see which are present in our Food data
    #   Get calories for food present in Food data
    #   From eaten food get list of extra food
    def TakingExtraFoodsOut(FoodDLL, foods):
        list_of_food = []
        list_of_calories = []
        while FoodDLL.HeadValue is not None:
            for i in foods:
                if i == FoodDLL.HeadValue.DataValue.name:
                    list_of_food.append(i)
                    list_of_calories.append(FoodDLL.HeadValue.DataValue.value)
            FoodDLL.HeadValue = FoodDLL.HeadValue.NextValue
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
        list_of_extras, list_of_calories = TakingExtraFoodsOut(FoodDLL, foods)
        amounts = AskingForAmountsOfEatenFoods(foods, list_of_extras)
        consumed_calories = CalculatingConsumedCalories(list_of_calories, foods, list_of_extras, amounts)
        PrintAndSaveTheResultOfConsumedCalories(consumed_calories, list_of_extras)

    consumed()

#   Choosing meal plan
def MealPlans(MealDLL):
    #   User chooses meal category
    def ChoseAMealType(MealDLL):
        for place in range(1, len(MealDLL.HeadValue.DataValue.value) + 1):
            print(place, ") ", MealDLL.HeadValue.DataValue.value[place - 1])
        question = int(input("Please choose one of the meal plans by its number: "))
        return question - 1

    #   Print the chosen meal
    def PrintAndSaveTheScheduleOfMeal(MealDLL, question):
        print("Your plan!!!\n")
        meal = ""

        MealDLL.HeadValue = MealDLL.HeadValue.NextValue
        while MealDLL.HeadValue is not None:
            meal = meal + MealDLL.HeadValue.DataValue.name + ": \n" + MealDLL.HeadValue.DataValue.value[question] + "\n"
            MealDLL.HeadValue = MealDLL.HeadValue.NextValue

        with open("meal_result.txt", "a") as m:
            m.write(meal)
        print(meal)

    #   Execution of meal type choice
    def meals():
        question = ChoseAMealType(MealDLL)
        PrintAndSaveTheScheduleOfMeal(MealDLL, question)

    meals()

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
    ActivitiesDLL = json_to_activites_linked_list(activities_data)
    FoodDLL = json_to_food_linked_list(food_data)
    MealDLL = json_to_meal_linked_list(meal_data)
    question = CalculateBurnedOrConsumedCalories()
    if question == "burned":
        BurnedCalories(ActivitiesDLL)
    elif question == "consumed":
        ConsumedCalories(FoodDLL)

    while True:
        ActivitiesDLL = json_to_activites_linked_list(activities_data)
        FoodDLL = json_to_food_linked_list(food_data)
        MealDLL = json_to_meal_linked_list(meal_data)
        next_question = ExtraOptions()
        if next_question == "1":
            BurnedCalories(ActivitiesDLL)
        elif next_question == "2":
            ConsumedCalories(FoodDLL)
        elif next_question == "3":
            MealPlans(MealDLL)
        elif next_question == "4":
            print("You chose to exit.")
            break

main()
