import random
def game_over():
    print("You lost.")
def winner():
    print("You won the game!")
options = []
inventory = []
print("You shout angrily, as a man, named Hank, runs aways with all of your pocket money. \n'Come back here!' you shout. \n'Or else what, Walker?' \nAnd with that, he ran. But no. You aren't giving up so easily. A fight it shall be.")
while True:
    print(f"Inventory: {inventory}")
    choice = input("Do you, \nA:chase Hank... or, \nB:go to a nearby store first? \nOf course, if you done both already, you can go back home.")
    if choice == "A":
        if "A" in options:
            print("You fought with Hank already. Please go back.")
        else:
            options.append("A")
            print("You walk up to Hank, fists ready. \nHank laughs. \n'You think you got a chance with me?' \nYou nod, signalling Hank to come. \nHank snorts.")
            print("Hank wants to fight!")
            your_hp = 10
            hank_hp = 12
            your_attack = 3
            hank_punch = 2
            hank_spin = 3
            while your_hp and hank_hp >= 0:
                print(f"Your HP: {your_hp} \nHank's HP: {hank_hp}")
                move = input("You have two moves; \nA: Punch, or \nB: Back away. \nYou can also skip with C, or check your inventory with D. \nWhich do you choose?")
                if move == "A":
                    hank_hp -= your_attack
                    print(f"You have dealt {your_attack}HP to Hank!")
                elif move == "B":
                    your_hp += 2
                    print("You have healed yourself by 2HP!")
                elif move == "C":
                    print("You skipped your move.")
                elif move == "D":
                    if "Cupcake" in inventory:
                        use = input("There is a cupcake in your inventory. Do you take it?")
                        if use == "Yes":
                            your_hp += 5
                            inventory.remove("Cupcake")
                            print("You have gained 5HP!")
                        elif use == "No":
                            print("You put the cupcake away.")
                        else:
                            print("You are losing it!")
                            continue
                    else:
                        print("Nothing is in your inventory.")
                else:
                    print("Get your head in the game!")
                    continue
                print("Hank has two moves; Punch and Spin. He could also skip his turn.")
                hank_move = random.choice(["Punch", "Spin", "Skip"])
                if hank_move == "Punch":
                    your_hp -= hank_punch
                    print(f"Hank dealt {hank_punch}HP to you!")
                elif hank_move == "Skip":
                    print("Hank skipped his turn.")
                else:
                   your_hp -= hank_spin
                   print(f"Hank dealt {hank_spin}HP to you!")
                if your_hp <= 0:
                    print("You tumble to the ground, defeated. Hank smiles menacingly at you. \nGAME OVER.")
                    game_over()
                    break
                elif hank_hp <= 0:
                    print("Hank falls to the floor, groaning in pain. You grab your stolen money, and walk away. \nYOU WON!")
                    winner()
                    break
    elif choice == "B":
        if "B" in options:
            print("You already went to the store. You must go back.")
        else:
            options.append("B")
            print("You walk into the store, where a man laid. \n'Hey, Luthor. You got something for me?' \nLuthor smiled. 'You want to fight Hank? Well, I got the thing just for you!' \nHank then blinked, before he panicked. \n'...as son as I find it.'")
            attempts = 3
            while attempts > 0:
                look = input("Luthor's item is somewhere, but where? There are 5 places; \nA:A cabinet \nB:The counter \nC:The table \nD:The toliet \nE:The fridge \nWhere do you look?")
                if look == "A":
                    print("Nothing there. Try again!")
                    attempts -= 1
                elif look == "B":
                    print("Nothing there. Try again!")
                    attempts -= 1
                elif look == "D":
                    print("Nothing there. Try again!")
                    attempts -= 1
                elif look == "E":
                    print("Nothing there. Try again!")
                    attempts -= 1
                elif look == "C":
                    print("You find a cupcake. Grabbing it, you hand it to Luthor. \n'Is this the item, Luthor?' \nLuthor smiled. \n'Yes, it's for you! To help in your battle with Hank! It can increase your health!' You smile, before thanking him. You then left the store.")
                    inventory.append("Cupcake")
                    break
                if attempts == 0:
                    print("Hank laughs are getting more echoey. Luthor sighs. \n'I'm sorry, Walker, but I can't give you the item.' \nWalker sighs, before he walked away.")
                    break
    elif choice == "C":
        print("You returnback home and sleep soundly.")
        break
    else:
        print("You want your money back or not?")
        continue