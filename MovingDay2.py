import random
print("Welcome to your new home... not as good as last tie, but at least you will have fun!... hopefully. For now, it's time to explore!")
name = input("First, we have to set up a new name! What will it be? ")
choice1 = input("There is a house nearby your new one. Do you want to visit it? ")
if choice1 == "Yes":
    print("You ring on the doorbell, and you a girl, about age 12, like yourself. \n'Hello! You must be the new neighbour! My name is Ginna!' \nYou would nod, before stating your own name, " + str(name) + ".")
    choice2 = input("As you enter, you find a plushie. Do you grab it?")
    if choice2 == "Yes":
        print("You and Ginna sit down on the couch, where Ginna devises a game. \n'Alright, let's play a certain game, called The Number Game!'")
        choice3 = input("Do you play the number game? ")
        if choice3 == "Yes":
            while True:
                print("After a long explanation, you are ready to play!")
                try:
                    number = input("Pick a number between 1 to 7! ")
                    if 1 <= int(number) <= 7:
                        print("Your number is " + str(number) + "!")
                        ginna_number = random.randint(1, 10)
                        print("Your number is " + str(number) + ", while Ginna's number is... ") 
                        print(str(ginna_number) + ".")                
                        if int(number) <= int(ginna_number):
                            print("'Whoops! Let's try that again!' Ginna said.")
                            continue
                        else:
                            print("'You won!' Ginna said.")
                            break
                    else:
                        print("A number between 1 and 7, please.")
                except ValueError:
                    print("Please... put a number.")
            print("As you and Ginna smile together, you look outisde the window. Jeeps! It's getting late! \nYou start to leave the house, when Ginna noticed something. \n'Is that my plushie?' Ginna asked.")
            choice4 = input("Do you tell the truth? ")
            if choice4 == "Yes":
                print("With much reluctance, you nod your head. \nGinna blinked, before sighing. " + "'" + str(name) + "... I know you like the plushie... You can't just take it from me, though.' \nGinna would sigh, before smiling. \n'But... telling the truth? That's a hard thing to do. \nGinna shook hands with you, hoping that she can see you some other time. \nENDING 2: FRIENDSHIP")
            elif choice4 == "No":
                print("Ginna looked at your hands. That ws he plushie. \nShe would blink. \n'I thought that...' \nShe would leave, taking the plushie away. \nENDING 1: HEARTBROKEN")
            else:
                print("Please pick something.")
        elif choice3 == "No":
            print("Ginna thought you were boring and asked you to go home. Sorry! Try again!")
        else:
            print("Please pick something next time.")
    elif choice2 == "No":
        print("You and Ginna sit down on the couch, where Ginna devises a game. \n'Alright, let's play a certain game, called The Math Game!'")
        choice3 = input("Do you play the math game? ")
        if choice3 == "Yes":
            while True:
                print("After a long explanation, you are ready to play!")
                try:
                    pro1 = input("What is the area of a triangle of height 10 and width 5?")
                    if pro1 == "25":
                        pro2 = input("If an apple is $2, and an orange is twice as much, how much is a lemon, which is 3/4ths as much as the orange?")
                        if pro2 == "3":
                            pro3 = input("The area of a sqaure is 64. What is the length of one side?")
                            if pro3 == "8":
                                print("Congratulations! You won!")
                                break
                            else:
                                print("Sorry! Try again!")
                                continue
                        else:
                            print("Sorry! Try again!")
                            continue
                    else:
                        print("Sorry! Try again!")
                        continue
                except ValueError:
                    print("Please type down a value.")
                    continue
            print("As you finish the math game, you and Ginna have a laugh. You are about to leave, when Ginna stops you. \n'Are we going to go out sometime?'")
            choice4 = input("Will you? ")
            if choice4 == "No":
                print("Ginna blinked, before sighing. \n'I never had friends, and I though you could be my very first... well, I suppose not.' \nGinna left the room, and you left the house \nENDING 1: HEARTBROKEN")
            elif choice4 == "Yes":
                print("Ginna smile, before hugging you. \n'Finaly! A true friend! Thank you!' \nYou blush, patting her on the back. \nENDING 2: FRIENDSHIP")
            else:
                print("Please pick something.")
        elif choice3 == "No":
            print("Ginna thought you were boring, and asked you to leave. Sorry! Try again!")
        else:
            print("Please pick something.")
elif choice1 == "No":
    print("You decide to stay at home, where Mom is setting up her items. You walk over to her.")
    choice2 = input("Do you get Mom's attention?")
    if choice2 == "Yes":
        print("You tap Mom's shoulder, as she looks behind. \n'Oh! Hi, sweetie!' You smile, as you decide to help her out.")
        choice3 = input("Searching the items, you find a fragile plate. Do you grab it?")
        if choice3 == "No":
            print("You decide to let Mother grab the fragile plate instead. \nAfter cleaning up, you both decide to rest at the couch.")
            choice4 = input("You feel the urge to watch you favourite channel on TV. Do you turn the TV on?")
            if choice4 == "No":
                print("You decide to let Mother watch her show instead. \nAs you watch, you look at Mother. You don't feel at home in this new place.")
                choice5 = input("Do you ask for comfort?")
                if choice5 == "Yes":
                    print("You tell Mother about how you feel in this new place. \nMom sighs, before stating... \n'You just try to hang on, and this this place another chance. Maybe you can form new friends.' \nYou nod, before hugging her. \nENDING 4: HOPE")
                elif choice5 == "No":
                    print("You remain in silence, not knowing what to do in this strange new world. \nENDING 3: CONFUSION")
            elif choice4 == "Yes":
                print("Your favourite TV show just happned to say a bad word, and Mother forced you into your new room. Sorry! Try again!")
        elif choice3 == "Yes":
            print("You drop the plate, and Mom forces you into your new room. Sorry! Try again!")
    elif choice2 == "No":
        print("You walk into the living room, where you see Dad rubbing his head. You walk towards him.")
        choice3 = input("Do you ask what is wrong?")
        if choice3 == "Yes":
            print("As walk up to him, and say, 'Dad, I am bored.' Dad looked at you, before he gave a thought. \nHow about Rock, Paper, Scissors?")
            choice4 = input("Do you play Rock, Paper, Scissors with Dad?")
            if choice4 == "Yes":
                while True:
                    rps = input("Choose either Rock, Paper or Scissors. ")
                    moves = ["Rock", "Paper", "Scissors"]
                    dad_rps = random.choice(moves)
                    print("You chose " + str(rps) + ", and Dad chose... ") 
                    print(str(dad_rps) + ".")
                    if rps == dad_rps:
                        print("It's a tie! Try again!")
                        continue
                    elif rps == "Rock":
                        if dad_rps == "Scissors":
                            print("You win!")
                            break
                        else:
                            print("You lost.")
                            continue
                    elif rps == "Paper":
                        if dad_rps == "Rock":
                            print("You won!")
                            break
                        else:
                            print("You lost.")
                            continue
                    elif rps == "Scissors":
                        if dad_rps == "Paper":
                            print("You won!")
                            break
                        else:
                            print("You lost.")
                            continue
                    else:
                        print("Rock, Paper or Scissors.")
                        continue
                print("Winning Rock, paper, Scissors, you find that Dad is not as upset.")
                choice5 = input("Do you ask why?")
                if choice5 == "Yes":
                    print("You ask Father about his mood. \nHe sighs. \n'I miss home. Really, all the fun times we had aid there. But now that I did have one here... maybe it won't be so bad.' \nYou blinked, before hugging him. tears visible. He patted you on the back. \nENDING 4: HOPE")
                elif choice5 == "No":
                    print("You just shrug it off, but it does intrigue you. What about his behaviour? \nENDING 3: CONFUSION")
                else:
                    print("Please pick something.")
            if choice4 == "No":
                print("You shake your head, and Dad sighs. \nHe asks you to sit back down.")
                choice5 = input("You feel like turning on the TV and watching something. Do you do so?")
                if choice5 == "Yes":
                    print("As you watch your favourite show, you notice how Dad smile along too, even if this kind of content does not entertain him.")
                    choice6 = input("Do you ask why?")
                    if choice6 == "Yes":
                        print("You ask abut this conundrum. He smiles. \n'All the good times I had with you back home, it makes me smile If I see you smile... well. \nYou blink, before smiling. \nENDING 4: HOPE")
                    elif choice6 == "No":
                        print("You remain silent, but this does intrigue you Maybe one day, but who knows. \nENDING 3: CONFUSION")
                    else:
                        print("Please pick something.")
                elif choice5 == "Yes":
                    print("You get bored out of your mind watching football, and it looks like Dad has too, sleeping. You can't get remote from his hands. Sorry! Try again!")
                else:
                    print("Please pick something.")
            else:
                print("Please pick something.")
        elif choice3 == "No":
            print("You both just sit on the couch, as you just sit side by side together Boy, it sure is boring. \nSECRET ENDING: SHEER BOREDOM")
        else:
            print("Please pick something.")
    else:
        print("Please pick something.")
else:
    print("Please pick something.")
                    
                    