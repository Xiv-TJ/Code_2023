import random
def rock(rock, paper, scissors):
    ai_choice = random.choice(["Rock", "Paper", "Scissors"])
    print(f"Your opponent dealt {ai_choice}!")
    if ai_choice == "Rock":
        print("It's a tie!")
    elif ai_choice == "Paper":
        print("You lost. Try again!")
    else:
        print("You won!")
def paper(rock, paper, scissors):
    ai_choice = random.choice(["Rock", "Paper", "Scissors"])
    print(f"Your opponent dealt {ai_choice}!")
    if ai_choice == "Rock":
        print("You won!")
    elif ai_choice == "Paper":
        print("It's a tie!")
    else:
        print("You lost. Try again!")
def scissors(rock, paper, scissors):
    ai_choice = random.choice(["Rock", "Paper", "Scissors"])
    print(f"Your opponent dealt {ai_choice}!")
    if ai_choice == "Rock":
        print("You lost. Try again!")
    elif ai_choice == "Paper":
        print("You won!")
    else:
        print("It's a tie!")
print("It's time to play Rock, Paper, Scissors! Are you ready?")
choice = input("What will be your move? ")
if choice == "Rock":
    rock(rock, paper, scissors)
elif choice == "Paper":
    paper(rock, paper, scissors)
elif choice == "Scissors":
    scissors(rock, paper, scissors)
else:
    print("Looks like you don't want to take this game seriously.")