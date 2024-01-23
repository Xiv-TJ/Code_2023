import time
def reading(cookbook):
    for food, instructions in cookbook.items():
        time.sleep(2)
        print(f"Dish: {food}. \nInstructions: {instructions}")
cookbook = {"Coca-Cola Buttered Shrimp": "Place butter in warm pan and cook shrimp. Afterwards, add about a cup or two of coca-cola, depending on the portion. Then, it is ready!",
            "A Hearty Brekkie": "Cook some rice. Fry some egg, and spam/bacon. Boil some spinach. Then, add them all together!",
            "Breaded Eggs": "Toast a couple slices of bread. Then, crack some eggs on said bread. Alternatively, you can cut a hole through the bread and fry egg inside said hole."}
while True:
    print("Welcome to the Family Cookbook!")
    time.sleep(3)
    print("In this cookbook, you can read our recipes, or add new ones if you are a family member.")
    time.sleep(3)
    choice = input("Do you want to read the cookbook, or add a recipe? Alternatively, you can leave by stating 'Exit'. ")
    if choice.lower() == "read":
        reading(cookbook)
    elif choice.lower() == "add":
        food = input("What is the food item you want to add?: ")
        instructions = input("How do you cook this food item?: ")
        cookbook[food] = instructions
        print("Your recipe has been added!")
    elif choice.lower() == "exit":
        print("Thank you for reading the Cookbook!")
        break
    else:
        print("Invalid option.")
        continue
    