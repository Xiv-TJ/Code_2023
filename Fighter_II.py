import random
inventory = []
options = []
def game_over():
    print("You lost.")
def winner():
    print("You won!")
print("Today is a great day! \nIt's the day of the Quail Convention! \nIt's time to go! \nHowever, your tickets have been stolen by a girl named Tracy. \nNo matter! You'll get them back, with the help of items and your skills! \nLet's get to work!")
while True:
    print(f"Your Inventory: {inventory}")
    choice1 = input("You now lay by a grassy plain. \nYou can either go to; \nA.Your house, \nB.A nearby pond, \nC.A nearby store. or; \nD.Comfront Tracy. \nYou can also go to the concert once you get your ticket back with E, or give up with F. \nWhat do you do? ")
    if choice1 == "B":
        choice2 = input("You find a park bench by a pond. Do you; \nA.Go back, or; \nB.Investigate the park bench? ")
        if choice2 == "A":
            print("You shrug, before going back.")
            continue
        elif choice2 == "B":
            if "B" in options:
                print("You've already checked the park bench.")
            else:
                options.append("B")
                print("Looking at the park bench, you find a pair of glasses. You take it, and you go back.")
                inventory.append("Glasses")
                continue
        else:
            print("...no.")
            continue
    elif choice1 == "A":
        if "A" in options:
            print("You already talked with Father.")
        else:
            options.append("A")
            print("You walk up to your house, where you fathr sits. \nYou walk towards him, as he sighs. \n'Have you seen my glasses anywhere? I haven't been able to find them!'")
            if "Glasses" in inventory:
                print("You nod your head, giving the glasses to Father. \nHe smiles, before giving you a cookie as a reward. \nYou leave the house, happy.")
                inventory.append("Cookie")
                inventory.remove("Glasses")
                continue
            else:
                print("You shake your head, and Father sighs. \nYOu leave the house.")
                continue
    elif choice1 == "C":
        if "C" in options:
            print("You already went to the store. You have to go back.")
        else:
            options.append("C")
            print("You walk up to Luthor, who was selling some kind of enhancement pill. \nYou ask if you can use them, to which Luthor nods away. \n'I'm not making profits here, so I need you to pay for this here.' \nYou check your pockets. Nothing inside. \nLuthor sighs/+. \n'Maybe I can give them to you if you solve my riddles.'")
            riddles = {"What has four legs but no head?": "Table",
                       "You are trapped in a room with three doors. One has electrified water on the bottom, the second has a lion that hasn't ate for 10 weeks, and the last, a mafia guy trying to kill you. WHich one do you pick to survive?": "Door 2",
                       "What has 2 hands but cannot clap?": "Clock",
                       "I am a odd number. Take a letter away, and I become even. What number am I?": "7",
                       "What has a neck but no head?": "Bottle"}
            questions = random.sample(list(riddles.items()), k=1)
            for (riddles, answers) in questions:
                print(riddles)
                guess = input("What is the answer? ")
                if guess == answers:
                    print("You got it! And for doing so, you get the pills! Nice!")
                    inventory.append("Pills")
                    break
                else:
                    print("Unfourtunately, you got it wrong. You can't get the pills, and you leave.")
                    break
    elif choice1 == "D":
        print("You walk up to Tracy, who was holding your tickets. \nShe eyed you, before shrugged. \n'Oh, you want them back, don't you?' \nYou nod your head. Tracy scoffed. \n'Then take them from me.")
        print("Tracy wants to fight!")
        your_hp = 12
        tracy_hp = 15
        your_attack = 4
        tracy_attack = 2
        your_defense = 2
        tracy_defense = 3
        your_attacks = ["A. Punch", "B. Back Away", "C. Stance", "D. Inventory"]
        tracy_attacks = ["Punch", "Recover", "Item Throw", "Back Away"]
        while your_hp > 0 and tracy_hp > 0:
            print(f"Your HP: {your_hp}. \nTracy's HP: {tracy_hp}.")
            print(f"Your Inventory: {inventory}")
            move = input(f"Choose your move; {your_attacks}")
            if move == "A":
                result = your_attack - tracy_attack
                tracy_hp -= result
                print(f"You dealt {result}HP to Tracy!")
            elif move == "B":
                your_defense += 1
                print("Your defense increased by 1!")
            elif move == "C":
                your_attack += 1
                print("Your attack has increased by 1!")
            elif move == "D":
                print(f"You have: {inventory}")
                use = input("Which would you like to use? ")
                if use == "Cookie":
                    if "Cookie" not in inventory:
                        print("You don't have a cookie in your inventory.")
                        continue
                    else:
                        inventory.remove("Cookie")
                        your_hp += 3
                        print("Your HP had increased by 3!")
                        continue
                elif use == "Pills":
                    if "Pills" not in inventory:
                        print("You don't have pills in your inventory.")
                        continue
                    else:
                        inventory.append("Pills")
                        your_defense += 2
                        your_attack += 2
                        print("Your Defense and Offence have increased by 2!")
                        continue
            else:
                print("Get your head in the game!")
            tracy_move = random.choice(tracy_attacks)
            if tracy_move == "Punch":
                results = tracy_attack - your_defense
                your_hp -= results
                print(f"You lost {results}HP!")
            elif tracy_move == "Recover":
                tracy_hp += 1
                print("Tracy recovered 1HP!")
            elif tracy_move == "Item Throw":
                your_hp -= 2
                print("You lost 2HP!")
            else:
                tracy_attack += 1
                print("Tracy's attack increased by 1!")
            if your_hp <= 0:
                print("You fall to the floor, in pain. \nTracy laughs, as she runs away with the tickets. \nYou sigh, having been beaten.")
                break
            if tracy_hp <= 0:
                print("Tracy falls to the floor, injured. \nYou snatch your tickets away from Tracy's hands, as you leave.")
                inventory.append("Ticket")
                break
    elif choice1 == "E":
        print("You walk up to the stadium, as a bouncer stops you. \n'Do you have a ticket?'")
        if "Ticket" in inventory:
            print("You give the ticket to the bouncer, and he lets you in. \nYou have the best time of your life.")
            winner()
            break
        else:
            print("The bouncer doesn't let you in, and you go back.")
    elif choice1 == "F":
        print("You walk back to your bedroom, where you just go sleep.")
        game_over()
        break
            
                        
        
                
        
        