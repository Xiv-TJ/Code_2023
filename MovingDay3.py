import random
import sys
def game_over():
    print("You lost the game.")
    sys.exit()
def good_ending():
    print("You saved Ginna!")
    sys.exit()
def best_ending():
    print("You saved Ginna, and got yourself a new friend!")
    sys.exit()
strength = 1
mental = 1
inventory = []
party = []
selected_characters = []
teddy_bear = []
print("'HELP ME!' Ginna screamed, as a bully, Ted, took her away. \nAs the person having seen Ginna been taken away by Ted, it is up to you, Arlo, to save her. \nHaving moved recently, and not knowing of the customs, your strength and mentality are... limited. \nNot to worry, however, With the help of clasmates, you can train to become stronger and smarter! \nLet's get to work!")
while True:
    choice = input("Do you want to go to the Cafeteria or the Classroom? ")
    if choice == "Cafeteria":
        while True:
            print(f"Your stats: {strength}, {mental}.")
            print(f"Invetory: {inventory}.")
            print(f"Fighting Party: {party}.")
            print("Entering the Cafeteria, you find three classmates; Tommy, the friendy jock, Keeper, a hippie, and Lila, the normal girl.")
            choice1 = input("Do you interact with Tommy, Keeper or Lila? ")
            if choice1 == "Tommy":
                if "Tommy" in selected_characters:
                    print("You have already interacted with Tommy enough.")
                else:
                    selected_characters.append("Tommy")
                    print("You approach Tommy, asking for help to beat Ted. \nHe smiles. \n'Finally, someone brave enough to fight Ted! Arlo, if you want to beat him, you gotta learn how to dodge!' \n'I show you, eh?'")
                    interactions = 20
                    hp = 12
                    for _ in range(interactions):
                        print(f"You have {interactions} interations left!")
                        dodge = input("Do you dodge \n1: Left or \n2: Right? ")
                        punch = ["Left", "Right"]
                        tommy_attack = random.choice(punch)
                        if dodge == "1":
                            print("You have chosen to dodge left!")
                            if tommy_attack == "Left":
                                print("You have been hit!")
                                hp -= 1
                            else:
                                print("You have successfully dodged the attack!")
                        elif dodge == "2":
                            print("You have chosen to dodge right!")
                            if tommy_attack == "Right":
                                print("You have been hit!")
                                hp -= 1
                            else:
                                print("You have successfully dodged the attack!")
                        else:
                            print("Take this seriously!")
                            continue
                        if hp <= 0:
                            print("Tommy sighed. \n'Sorry, man. Today just ain't the day.'")
                            game_over()
                        else:
                            print(f"Your health is {hp}!")
                        interactions -= 1
                        if interactions == 0:
                            print("Tommy sighed. \n'Wow! You even made me tired!'")
                            strength += 1
                            break
            elif choice1 == "Keeper":
                print("You talk to Keeper, asking him if he knows where Ted is.")
                if strength == 3 and mental == 3:
                    if "Keeper" in party:
                        print("Keeper nodded his head, as you and Keeper make your way to the playground. \nThere, you find Ted messing with Ginna. \nYou stand your ground. \n'Let her go!' \nTed chuckled. \m'Make me, coward!'")
                        your_hp = 15
                        keeper_hp = 15
                        ted_hp = 30
                        your_defense = 3
                        keeper_defense = 3
                        ted_defense= 2
                        your_offense = 4
                        keeper_offense = 2
                        ted_offense = 6
                        your_attacks = ["Punch", "Position", "Memory", "Recover"]
                        keeper_attacks = ["Music", "Motivate", "Calming", "Item Throw"]
                        ted_attacks = ["Punch", "Taunt", "Insult"]
                        while your_hp > 0 and keeper_hp > 0 and ted_hp > 0:
                            print(f"HP: You:{your_hp}, Keeper:{keeper_hp}, Ted:{ted_hp}")
                            print("Your turn to attack:")
                            for i, attack in enumerate(your_attacks, start=1):
                                print(f"{i}. {attack}")
                            move = input("Choose your attack: ")
                            if move == "Punch":
                                punch = your_offense - ted_defense
                                ted_hp -= punch
                                if punch > 0:
                                    print(f"You have dealt {punch}HP!")
                                else:
                                    print("The attack is ineffective!")
                            elif move == "Position":
                                print("Your defense has raised by 1!")
                                your_defense += 1
                            elif move == "Memory":
                                print("Your offense has increased by 1!")
                                your_offense += 1
                            elif move == "Recover":
                                print("You have recovered 2HP!")
                                your_hp += 2
                            else:
                                print("Get your head in the game!")
                            print("Keeper's turn to attack!")
                            for i, attack in enumerate(keeper_attacks, start=1):
                                print(f"{i}. {attack}")
                            keeper_move = random.choice(keeper_attacks)
                            print(f"Keeper's move is {keeper_move}!")
                            if keeper_move == "Music":
                                print("Both Keeper and Your HP raised by 1!")
                                keeper_hp += 1
                                your_hp += 1
                            elif keeper_move == "Motivate":
                                print("Both Keeper and Your offense has increased by 1!")
                                keeper_defense += 1
                                your_offense += 1
                            elif keeper_move == "Calming":
                                print("Your defense has increased by 1!")
                                your_defense += 1
                            else:
                                attack = keeper_offense - ted_defense
                                ted_hp -= attack
                                if attack > 0:
                                    print(f"Keeper has dealt {attack}HP!")
                                else:
                                    print("The attack is ineffective!")
                            print("Ted's turn to attack:")
                            for i, attack in enumerate(ted_attacks, start=1):
                                print(f"{i}. {attack}")
                            ted_move = random.choice(ted_attacks)
                            if ted_move == "Punch":
                                target = random.choice(["You", "Keeper"])
                                if target == "You":
                                    print("Ted will attack you!")
                                    bossattack = ted_offense - your_defense
                                    your_hp -= bossattack
                                    if bossattack > 0:
                                        print(f"Ted has dealt {bossattack}HP to you!")
                                    else:
                                        print("The attack is ineffective!")
                                else:
                                    print("Ted will attack Keeper!")
                                    bossattack = ted_offense - keeper_defense
                                    keeper_hp -= bossattack
                                    if bossattack > 0:
                                        print(f"Ted has dealt {bossattack}HP to Keeper!")
                                    else:
                                        print("The attack is ineffective!")
                            elif ted_move == "Taunt":
                                print("You and Keeper's defense has decreased by 1!")
                                your_defense -= 1
                                keeper_defense -= 1
                            else:
                                print("You and Keeper's offense has decreased by 1!")
                                your_offense -= 1
                                keeper_offense -= 1
                        if your_hp <= 0:
                            while True:
                                print("You are down! You cannot play anymore!")
                                print("Keeper's turn to attack!")
                                for i, attack in enumerate(keeper_attacks, start=1):
                                    print(f"{i}. {attack}")
                                keeper_move = random.choice(keeper_attacks)
                                print(f"Keeper's move is {keeper_move}!")
                                if keeper_move == "Music":
                                    print("Both Keeper and Your HP raised by 1!")
                                    keeper_hp += 1
                                elif keeper_move == "Motivate":
                                    print("Both Keeper and Your offense has increased by 1!")
                                    keeper_offense += 1
                                elif keeper_move == "Calming":
                                    print("Your defense has increased by 1!")
                                    your_defense += 1
                                else:
                                    attack = keeper_offense - ted_defense
                                    ted_hp - attack
                                    if attack > 0:
                                        print(f"Keeper has dealt {attack}HP!")
                                    else:
                                        print("The attack is ineffective!")
                                print("Ted's turn to attack:")
                                for i, attack in enumerate(ted_attacks, start=1):
                                    print(f"{i}. {attack}")
                                ted_move = random.choice(ted_attacks)
                                if ted_move == "Punch":
                                    bossattack = ted_offense - keeper_defense
                                    keeper_hp - bossattack
                                    if bossattack > 0:
                                        print(f"Ted has dealt {bossattack}HP to Keeper!")
                                    else:
                                        print("The attack is ineffective!")
                                elif ted_move == "Taunt":
                                    print("Keeper's defense has decreased by 1!")
                                    keeper_defense -= 1
                                else:
                                    print("Keeper's offense has decreased by 1!")
                                    keeper_offense -= 1
                        if keeper_hp <= 0:
                            while True:
                                print("Keeper has been downed! He cannot play anymore!")
                                print(f"HP: You:{your_hp}, Keeper:{keeper_hp}, Ted:{ted_hp}")
                                print("Your turn to attack:")
                                for i, attack in enumerate(your_attacks, start=1):
                                    print(f"{i}. {attack}")
                                move = input("Choose your attack: ")
                                if move == "Punch":
                                    punch = your_offense - ted_defense
                                    ted_hp -= punch
                                    if punch > 0:
                                        print(f"You have dealt {punch}HP!")
                                    else:
                                        print("The attack is ineffective!")
                                elif move == "Position":
                                    print("Your defense has raised by 1!")
                                    your_defense += 1
                                elif move == "Memory":
                                    print("Your offense has increased by 1!")
                                    your_offense += 1
                                elif move == "Recover":
                                    print("You have recovered 2HP!")
                                    your_hp += 2
                                else:
                                    print("Get your head in the game!")
                                print("Ted's turn to attack:")
                                for i, attack in enumerate(ted_attacks, start=1):
                                    print(f"{i}. {attack}")
                                ted_move = random.choice(ted_attacks)
                                if ted_move == "Punch":
                                    bossattack = ted_offense - your_defense
                                    your_hp -= bossattack
                                    if bossattack > 0:
                                        print(f"Ted has dealt {bossattack}HP to you!")
                                    else:
                                        print("The attack is ineffective!")
                                elif ted_move == "Taunt":
                                    print("You and Keeper's defense has decreased by 1!")
                                    your_defense -= 1
                                else:
                                    print("Your offense has decreased by 1!")
                                    your_offense -= 1
                        if your_hp <= 0 and keeper_hp <= 0:
                            print("Ted would chuckle, as he eyed both you and Keeper. \n'Told ya guys. Never mess with the big dog.'")
                            game_over()
                        if ted_hp <= 0:
                            print("Ted falls to the ground, injured and in pain. \nBoth you and Keeper cheer, as Ginna runs towards you. \nYou smile.")
                            best_ending()
                    else:
                        print("Keeper tells you he saw Ted at the playground. \nYou walk over there, seeing Ted messing with Ginna. \n'Let her go!' you say. \nTed chuckles. \n'You have to get through me first, weakling!")
                        your_hp = 15
                        ted_hp = 20
                        your_offense = 5
                        ted_offense = 6
                        your_defense = 2
                        ted_defense = 1
                        your_attacks = ["Punch", "Position", "Memory", "Recover"]
                        ted_attacks = ["Punch", "Taunt", "Insult"]
                        while your_hp > 0 and ted_hp > 0:
                            print(f"HP: You:{your_hp}, Ted:{ted_hp}")
                            print("Your turn to attack:")
                            for i, attack in enumerate(your_attacks, start=1):
                                print(f"{i}. {attack}")
                            move = input("Choose your attack: ")
                            if move == "Punch":
                                punch = your_offense - ted_defense
                                ted_hp -= punch
                                if punch > 0:
                                    print(f"You have dealt {punch}HP!")
                                else:
                                    print("The attack is ineffective!")
                            elif move == "Position":
                                print("Your defense has raised by 1!")
                                your_defense += 1
                            elif move == "Memory":
                                print("Your offense has increased by 1!")
                                your_offense += 1
                            elif move == "Recover":
                                print("You have recovered 2HP!")
                                your_hp += 2
                            else:
                                print("Get your head in the game!")
                            print("Ted's turn to attack:")
                            for i, attack in enumerate(ted_attacks, start=1):
                                print(f"{i}. {attack}")
                            ted_move = random.choice(ted_attacks)
                            if ted_move == "Punch":
                                bossattack = ted_offense - your_defense
                                your_hp -= bossattack
                                if bossattack > 0:
                                    print(f"Ted has dealt {bossattack}HP to you!")
                                else:
                                    print("The attack is ineffective!")
                            elif ted_move == "Taunt":
                                print("You and Keeper's defense has decreased by 1!")
                                your_defense -= 1
                            else:
                                print("Your offense has decreased by 1!")
                                your_offense -= 1
                        if your_hp <= 0:
                            print("Ted would chuckle, as he eyed you. \n'Told ya guys. Never mess with the big dog.'")
                            game_over()
                        if ted_hp <= 0:
                            print("Ted falls to the ground, injured and in pain. \nYou cheer, as Ginna runs towards you. \nYou smile.")
                            good_ending()
                else:
                    print("Keeper would raise an eyebrow. \n'If you want to fight Ted, train a bit more, k?'")
                    continue
            elif choice1 == "Lila":
                if "Lila" in selected_characters:
                    print("You have already interacted with Lila enough.")
                else:
                    selected_characters.append("Lila")
                    print("You approach Lila, asking her to help out. \nYou would state, \n'I need help. Please assist me in defeating Ted.' \nShe would rub her head. \n'I can try to help you out mentally. I suppose.' \nShe would blink. \n'Just because you moved, doesn't mean you cannot make new friends.' \nYou would blink.")
                    help = {"C!": "C", "D!": "D", "Q!": "Q", "H!": "H", "A!": "A", "S!": "S", "L!": "L", "R!": "R", "I!": "I", "F!": "F"}
                    assistance = random.sample(list(help.items()), k=7)
                    acceptance = 0
                    for (letter, type) in assistance:
                        print(letter)
                        hope = input("Type! ")
                        if hope == type:
                            print("Your breath speeds up. You blink more often.")
                            acceptance += 1
                        else:
                            print("You shake your head. You will not accept it... yet.")
                        if acceptance == 6:
                            print("You sob, falling to the floor. \n'It's not fair... why do I move, while my other friends stay...?' \nLila sighs. \n'It will be okay, Arlo. Youll make new friends soon... hopefully...'")
                            print("'Here, take a teddy bear along with you. Maybe it can help you out.'")
                            inventory.append("Teddy Bear")
                            mental += 1
                            break
                        else:
                            print("No... Not just yet...")
                    if acceptance != 6:
                        print("You run off. \nNo, you don't want to hear this.")
                        game_over()
            elif choice1 == "Back":
                break
            elif choice1 == "Cheat":
                strength += 2
                mental += 2
                party.append("Keeper")
                continue
            else:
                print("Ginna is in danger as of now! We have to take this seriously!")
                continue
    elif choice == "Classroom":
        while True:
            print("As you speed your way down the hall, you are met with a hall monitor. \n'Diaz, I ned to go to the classroom! Can you please make way?!' \nDiaz shook her head. \n'Sorry, Arlo, but you need a hall pass first.' \nYou sigh.")
            choice2 = input("Do you try to get a hall pass, or be sneaky? Or do you simply wish to go back? ")
            if choice2 == "Back":
                break
            if choice2 == "Sneaky":
                print("You try to sneak your way around Diaz, but she captures you and takes you to the principal's office.")
                game_over()
            elif choice2 == "Hall Pass":
                print("You find Keeper with a hall pass. \n'Keeper, I need to go find people in the class! Can I come with you?!' \nUnfortunately, Keeper is a bit demanding. \n'Gimme an offer I can't 'fuse!'")
                choice3 = input("Do you give Keeper $50 or origami? ")
                if choice3 == "$50":
                    print("Keeper refused to let you go with him, thinking money is the root of all evil.")
                    game_over()
                elif choice3 == "Origami":
                    print("Keeper, with a big smile, allowed you to follow him. You have made it to the classroom.")
                    while True:
                        print("In the classroom, there are three students; Alfed, the kind muscle to a gang, Keeper, the hippie, and Jolie, the booksmart girl.")
                        print(f"Your stats: {strength}, {mental}.")
                        print(f"Inventory: {inventory}.")
                        print(f"Fighting Party: {party}.")
                        choice4 = input("Do you talk with Alfed, Keeper or Jolie? Or do you simply wish to go back? ")
                        if choice4 == "Alfed":
                            if "Alfed" in selected_characters:
                                print("You have already interacted with Alfed enough.")
                                continue
                            else:
                                selected_characters.append("Alfed")
                                print("You approach Alfed, determined. \n'Alfie! I need your help to defeat Ted!' \nAlfed smiles. \n'About time someone stepped up to that jerk. You come for punch? You got to deliver it perfectly, or it will be too weak or strong. Weak, enemy won't be stunned. Strong, you'll lose too much energy. Let's get to work.'")
                                attempts = 20
                                alfed_psi = random.randint(1, 100)
                                while attempts > 0:
                                    try:
                                        your_psi = int(input("Alfed asks you to punch a book. How hard do you punch it from 1 to 100PSI? "))
                                        if 1 <= your_psi <= 100:
                                            print(f"You punch the book at {your_psi}PSI!")
                                        if your_psi < alfed_psi:
                                            print("The punch is too weak. Try again.")
                                        elif your_psi > alfed_psi:
                                            print("The punch is too strong. Try again.")
                                        else:
                                            print("Alfed chuckled. \n'That was perfect!' \nThe two of you chuckle.")
                                            strength += 1
                                            break
                                    except ValueError:
                                        print("Please enter a valid number.")
                                    attempts -= 1
                                    if attempts == 0:
                                        print("Exhausted, you fall to the floor. \nAlfed sighs. \n'It just isn't you day, huh?")
                                        game_over()
                        elif choice4 == "Keeper":
                            print("You walk up to Keeper, who was trying to find something. \n'Sorry! Can't talk, bruv! Trying to find my teddy bear! Don't ask!")
                            if "Teddy Bear" in inventory:
                                print("You give the teddy bear Lila gave you to Keeper. \nHe smiles. \n'How did you get this... how can I repay you...?' \nYou say you need to fight Ted. \nHe agrees to fight alongside you.")
                                party.append("Keeper")
                                inventory.remove("Teddy Bear")
                            else:
                                print("You walk away silently.")
                        elif choice4 == "Jolie":
                            if "Jolie" in selected_characters:
                                print("You have interacted with Jolie enough.")
                                continue
                            else:
                                selected_characters.append("Jolie")
                                print("You walk over to Jolie. \n'Jolie! Can you help me fight against Ted?' \nShe would sigh. \n'Another poor soul thinking they can defeat Ted. I'll help you, but only mentally.'")
                                print("You will be given a mini-test. \nThe passing mark is 80%.")
                                while True:
                                    questions = {
                                        "What is 10 x 10?": "100",
                                        "What is 8 + 8?": "16",
                                        "What is 6 x 7?": "42",
                                        "What is 9 x 11?": "99",
                                        "What is 80 / 4?": "20",
                                        "What is 90 / 6?": "15",
                                        "What is 54 / 9?": "6",
                                        "What is 11 - 13?": "-2",
                                        "What is 7 - 5?": "2",
                                        "What is 16 + 89?": "105"
                                    }
                                    chosen_questions = random.sample(list(questions.items()), k=5)
                                    score = 0
                                    for (questions, solutions) in chosen_questions:
                                        print(questions)
                                        answer = input("What is your answer? ")
                                        if answer == solutions:
                                            print("Jolie nodded her head.")
                                            score += 1
                                        else:
                                            print("Jolie shook her head.")
                                    percentage = score * 20
                                    if percentage >= 80:
                                        print("Jolie smiled. \n'It seems as if you are smart enough to know how to fight Ted. I salute you and I hope you survive, or win, perhaps.'")
                                        mental += 1
                                        break
                                    else:
                                        print("Jolie looked down. \n'Just as I though. You are not fit enough to fight Ted. Sorry, but it isn't meant to be.'")
                                        game_over()
                        elif choice4 == "Back":
                            break
                        else:
                            print("Ginna's in trouble! You have to save her now!")
                            continue
                else:
                    print("Ginna is in Ted's castle! You have to take this seriously!")
                    continue
            else:
                print("Ginna is in trouble! You got to help her, not fool around!")
                continue
    else:
        print("Ginna is suffereing as of now! Take this more seriously, will you?")
        continue




                
