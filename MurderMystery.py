print("A murder has taken place in Frollo's Mansion!")
print("Suspects include: \nBen \nMegan \nJoseph \nKendra \nOllie \nWelsey \nSally \nHarper")
print("Help us to identify the murder!")
choice = input("Is the killer wearing a white shirt?: ")
if choice == "Yes":
    choice = input("Is the killer a man?: ")
    if choice == "Yes":
        choice = input("Is the killer wearing a hat?: ")
        if choice == "Yes":
            print("The killer is Ollie!")
        elif choice == "No":
            print("The killer is Ben!")
        else:
            print("You are fired.")
    elif choice == "No":
        choice = input("Is the killer famous?: ")
        if choice == "Yes":
            print("The killer is Kendra!")
        elif choice == "No":
            print("The killer is Sally!")
        else:
            print("You are fired.")
    else:
        print("You are fired.")
elif choice == "No":
    choice = input("Is the killer old?: ")
    if choice == "Yes":
        choice = input("Is the murder weapon a knife?: ")
        if choice == "Yes":
            print("The kiler is Megan!")
        elif choice == "No":
            print("The killer is Joseph!")
        else:
            print("You are fired.")
    elif choice == "No":
        choice = input("Is the killer stylish?")
        if choice == "Yes":
            print("The killer is Harper!")
        elif choice == "No":
            print("The killer is Wesley!")
        else:
            print("You are fired.")
    else:
        print("You are fired.")    
else:
    print("You are fired.")
print("Congratulations, detective!")