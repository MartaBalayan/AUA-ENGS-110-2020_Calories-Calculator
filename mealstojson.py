import json

meals = {
    "plans": ["1200 Cal Plan", "1500 Cal Plan", "2000 Cal Plan"],
    "Breakfast": ["All-bran cereal (125) 1.5oz\n\tMilk (50 calories) half cup\n\tBanana (90c) 3.5oz",
                  "Granola (120) 1 oz\n\tGreek yogurt (120)cup\n\tBlueberries (40) 2.5oz",
                  "Buttered toast(150)2oz\n\tEgg (80) 1 large\n\tBanana (90) 3.5oz\n\tAlmonds (170)0.5oz"],
    "First Snack": ["Cucumber (30) 8 oz\n\tAvocado dip (50)0.5oz", "Orange (70) 5 oz",
                    "Greek yogurt (120)cup\n\tBlueberries (40) 2.5oz"],
    "Lunch": ["Grilled cheese with tomato (300) (114 calories of Cheddar Cheese, (1 slice (0.5oz)), 147 calories of Bread, whole wheat (including toast) prepared from recipe, (2 slice, thin (3-3/4&quot; x 5&quot; x 3/8&quot;)), 18 calories of Butter, salted, (2.5 grams), 8 calories of Red Ripe Tomatoes (2.5 slice,thin/small), 13 calories of Pepper, black, (5 grams) 0 calories of Salt, (5 grams))\n\tBroccoli (50) cup",
              "Chicken andvegetable soup (300) 2 cups\n\tBread (100) 1.3oz",
              "Grilled chicken (225) 3.5 oz\n\tGrilled vegetables (125)2 cups\n\tPasta (185) 5oz"],
    "Second Snack": ["Walnuts (100) 0.5 oz", "Apple (75) 5 oz\n\tPeanut butter (75) 0.5oz",
                     "Hummus (50) 1oz\n\tBaby carrots (35)3.5oz\n\tCrackers (65)0.5oz"],
    "Dinner": ["Grilled Chicken (200)3.25oz\n\tBrussel sprouts (100)8oz\n\tQuinoa (105)3oz",
               "Steak (375) 5oz\n\tMashed potatoes (150)6oz\n\tAsparagus (75)3 cup",
               "Grilled salmon (225) 3oz\n\tBrown rice (175)5.5oz\n\tGreen beans (100) 18oz\n\tWalnuts (165) 1oz"]
}

with open("meal_types.json", "w") as json_file:
    json.dump(meals, json_file)