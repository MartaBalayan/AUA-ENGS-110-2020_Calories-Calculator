import json

with open("C:/Users/MARTA1/.PyCharmCE2019.3/config/scratches/data.json") as json_file:
    data = json.load(json_file)

for place in range(1, len(data["weight"]) + 1):
    print(place, ") ", data["weight"][place - 1])

weight_number = int(input("PLease choose your weight number from the list above: "))
index = weight_number - 1

exercise = input("Which exercise have you done? ")

hour = float(input("How many hours have you trained? "))

burned = data[exercise][index] * hour
result = f"You burned {burned} calories!!!\n"

with open("result.txt", "a") as r:
    r.write(result)
print(result)
