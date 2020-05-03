import json

calories_burned = {"weight":["Up to 56kg", "From 56kg up to 70kg", "More than 70kg"], "walking":[215, 267, 319], "baseball":[289, 359, 428], "swimming":[397, 492, 587],
                   "tennis":[397, 492, 587], "running":[624, 773, 923], "bicycling":[454, 562, 671], "football":[399, 494, 588], "basketball":[340, 422, 503]}

with open("burned_data.json", "w") as json_file:
    json.dump(calories_burned, json_file)

















