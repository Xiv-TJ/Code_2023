import random
def apple(): 
    return ["It's probably the most famous.", "It's usually a nice juice"]
def orange(): 
    return ["People usually don't eat the peel", "It's somewhat acidic."]
def banana(): 
    return ["The shape is the most unique.", "You slowly peel it as you it it, usually."]
def strawberry(): 
    return ["It's shaped like a triangle.", "It has leaves on top of it."]
def mango(): 
    return ["It's usually very sweet.", "It's only found on the equator."]
def pineapple(): 
    return ["People hate this on pizza.", "It's quite prickly."]
def durian(): 
    return ["This is banned in Singapore", "It's quite spiky."]
def grape(): 
    return ["It's quite small.", "There are red and green variants."]
def blueberry(): 
    return ["It's blue.", "It's quite small."]
def raisin(): 
    return ["It's not that moist.", "It it usually packed tightly on small packets."]
print("Welcome to the guessing game! In this, you'll be asked to guess fruits by asking questions! If you manage to guess the fruit, you win!")
fruits = {"apple": apple, "orange": orange, "banana": banana, "strawberry": strawberry, "mango": mango, "pineapple": pineapple, "durian": durian, "grape": grape, "blueberry": blueberry, "raisin": raisin}
chosen_fruit = random.choice(list(fruits.keys()))
hint_functions = fruits[chosen_fruit]
while True:
    guess = input("What is the fruit?")
    if guess != chosen_fruit:
        hints = hint_functions()
        hint = random.choice(hints)
        print(f"Incorrect! Here's a hint! The fruit {hint}")
    else:
        print("You have guessed the fruit!")
        break