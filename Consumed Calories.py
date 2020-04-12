import json

with open("C:/Users/MARTA1/.PyCharmCE2019.3/config/scratches/Marta.json") as json_file:
    data = json.load(json_file)

food = input("Write what you ate for breakfast separated by commas: ")
amount = input("Amount of each food, separated by commas: ")
food_list = food.split(",")
amount_list = amount.split(",")

calories = 0

for i in range(0, len(food_list)):
    calories = calories + data[food_list[i]] * (float(amount_list[i]) / 100)

consumed = f"You consumed {calories} calories!!\n"
with open("s.txt","a") as e:
    e.write(consumed)
print(consumed)