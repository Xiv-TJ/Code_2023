print("Hello, adventuerer! Today, we will explore the depths of the Basement together!")
choice1 = input("What shall you bring to the Basement? A flashlight, or a bag?")
if choice1 == "Bag":
    print("You accidentally fall down the stairs because you could not see the floor! Sorry! Try again!")
elif choice1 == "Flashlight":
    print("As you venture into the depths of the Basements, you find that there is a rat inside! Two objects are within reach; a swatter and a jar!")
    choice2 = input("Do you grab the swatter, or the jar?")
    if choice2 == "Jar":
        print("The rat escaped the jar, and you ran out of the basement in fear. Sorry! Try again!")
    elif choice2 == "Swatter":
        print("Successfully killing the rat, you ventured into the cave further. However, there is a fork in the road!")
        choice3 = input("Do you go left, or right?")
        if choice3 == "Left":
            print("You turn to the left, where a cardboard box is found inside.")
            choice4 = input("Do you open the cardboard box?")
            if choice4 == "Yes":
                print("As you open the cardboard box, a creature inside growls. You run off in fear. Sorry! Try again!")
            elif choice4 == "No":
                print("You refrain from opening the box, venturing even further inside. You find a pair of eyes staring back to you.")
                choice5 = input("Do you venture further?")
                if choice5 == "No":
                    print("You leave the basement. Ending 1: Denial")
                elif choice5 == "Yes":
                    print("You ventue further, and find your dad packing up. He looks at you, and says, 'Son, this is for the best.' You nod, before hugging. Ending 2: Hurt")
                else:
                    print("Leave.")
        elif choice3 == "Right":
            print("Lights became plentiful, as you look in front. You see Mother folding some clothes.")
            choice4 = input("Do you venture further?")
            if choice4 == "Yes":
                print("As you tap Mother's shoulder, she looks behind. She gets very upset, forcing you back to your room. Ending 4: Anger")
            elif choice4 == "No":
                print("You begin to walk back, when Mother looks behind and notices you. She blinks, before sighing. 'Sorry, Son. Maybe there will be a better life over there.' You shed some tears, before hugging Mother. Ending 3: Understand")
            else:
                print("Leave.")
            