food = {
    "Whole milk": "73",
    "Almond milk": "30",
    "Greek yogurt fat free": "120",
    "Sour cream, light": "16",
    "Egg": "75",
    "Egg white": "16",
    "Blue cheese": "119",
    "Cream cheese": "51",
    "Almonds": "170",
    "Peanuts": "166",
    "Black beans": "113",
    "Chickpeas": "105",
    "Atlantic salmon": "175",
    "Chicken Deli": "20",
    "Broccoli": "7",
    "Corn": "59",
    "Watermelon": "11",
    "Avocado": "48",
    "Oatmeal": "77",
    "Ranch": "73"
    }
    
first = input("Enter your first selection: ")
second = input("Enter your second selection: ")


if first == "Watermelon" or second == "Whole milk":
    raise ValueError("You cannot combine Watermelon with milk.")
elif first == "Whole milk" or second == "Watermelon":
    raise ValueError("You cannot combine Watermelon with milk.")
elif first not in food and second not in food:
    print("One or both of your selections are not in the list.")
else:
    if first in food and second in food: 
        total_calories = int(food[first]) + int(food[second])
    print (f"The total calories are: {total_calories}")

    