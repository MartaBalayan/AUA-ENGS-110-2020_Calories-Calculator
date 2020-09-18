class Consumed():
    def __init__(self, food1, amount1, food2, amount2):
        self.food1 = food1
        self.amount1 = amount1
        self.food2 = food2
        self.amount2 = amount2

    def consumed_cal(self):
        calories_consumed = {"milk": 50,
                             "granola": 120,
                             "yogurt": 120,
                             "blueberries": 40,
                             "buttered toast": 150,
                             "egg": 80,
                             "almonds": 170,
                             "apple": 59,
                             "banana": 151,
                             "grapes": 100,
                             "orange": 53,
                             "peach": 67,
                             "strawberry": 53,
                             "broccoli": 45,
                             "carrots": 50,
                             "cucumber": 17,
                             "lettuce": 5,
                             "tomato": 22,
                             "white bread": 75,
                             "cheeseburger": 285,
                             "hamburger": 250,
                             "potato": 130,
                             "beer": 154,
                             "coca-cola": 150,
                             "orange juice": 111,
                             "cheddar cheese": 113,
                             "chicken breast": 142,
                             "chocolate cookie": 59,
                             "spaghetti": 221,
                             "muesli": 390,
                             "rice": 200,
                             "pizza": 290,
                             "waffles": 130}
        consumed = calories_consumed[self.food1] * (float(self.amount1) / 100) + calories_consumed[self.food2] * (
                    float(self.amount2) / 100)
        print(f"You consumed {consumed} calories.")


class Burned():
    def __init__(self, weight, exercise1, time1, exercise2, time2):
        self.weight = weight
        self.exercise1 = exercise1
        self.time1 = time1
        self.exercise2 = exercise2
        self.time2 = time2

    def burned_cal(self):
        calories_burned = {"walking": [215, 267, 319], "baseball": [289, 359, 428], "swimming": [397, 492, 587],
                           "tennis": [397, 492, 587],
                           "running": [624, 773, 923], "bicycling": [454, 562, 671], "football": [399, 494, 588],
                           "basketball": [340, 422, 503]}
        if self.weight <= 56:
            i = 0
        elif 56 < self.weight <= 70:
            i = 1
        else:
            i = 2

        burned = calories_burned[self.exercise1][i] * float(self.time1) + calories_burned[self.exercise2][i] * float(
            self.time2)
        print(f"You burned {burned} calories.")


class Meals():
    def __init__(self, plan):
        self.plan = plan

    def meal_plan(self):
        meals = {
            "Breakfast": ["All-bran cereal (125) 1.5oz\n\tMilk (50 calories) half cup\n\tBanana (90c) 3.5oz",
                          "Granola (120) 1 oz\n\tGreek yogurt (120)cup\n\tBlueberries (40) 2.5oz",
                          "Buttered toast(150)2oz\n\tEgg (80) 1 large\n\tBanana (90) 3.5oz\n\tAlmonds (170)0.5oz"],
            "First Snack": ["Cucumber (30) 8 oz\n\tAvocado dip (50)0.5oz", "Orange (70) 5 oz",
                            "Greek yogurt (120)cup\n\tBlueberries (40) 2.5oz"],
            "Lunch": [
                "Grilled cheese with tomato (300) (114 calories of Cheddar Cheese, (1 slice (0.5oz)), 147 calories of Bread, whole wheat (including toast) prepared from recipe, (2 slice, thin (3-3/4&quot; x 5&quot; x 3/8&quot;)), 18 calories of Butter, salted, (2.5 grams), 8 calories of Red Ripe Tomatoes (2.5 slice,thin/small), 13 calories of Pepper, black, (5 grams) 0 calories of Salt, (5 grams))\n\tBroccoli (50) cup",
                "Chicken andvegetable soup (300) 2 cups\n\tBread (100) 1.3oz",
                "Grilled chicken (225) 3.5 oz\n\tGrilled vegetables (125)2 cups\n\tPasta (185) 5oz"],
            "Second Snack": ["Walnuts (100) 0.5 oz", "Apple (75) 5 oz\n\tPeanut butter (75) 0.5oz",
                             "Hummus (50) 1oz\n\tBaby carrots (35)3.5oz\n\tCrackers (65)0.5oz"],
            "Dinner": ["Grilled Chicken (200)3.25oz\n\tBrussel sprouts (100)8oz\n\tQuinoa (105)3oz",
                       "Steak (375) 5oz\n\tMashed potatoes (150)6oz\n\tAsparagus (75)3 cup",
                       "Grilled salmon (225) 3oz\n\tBrown rice (175)5.5oz\n\tGreen beans (100) 18oz\n\tWalnuts (165) 1oz"]
        }

        if self.plan == 1200:
            j = 0
        elif self.plan == 1500:
            j = 1
        elif self.plan == 1700:
            j = 3

        for key in meals:
            print(meals[key][j])


cons1 = Consumed("pizza", 100, "waffles", 30)
cons1.consumed_cal()
burn1 = Burned(65, "running", 1, "football", 0.5)
burn1.burned_cal()
meal1 = Meals(1500)
meal1.meal_plan()
