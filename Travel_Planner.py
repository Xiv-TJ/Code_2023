import time
while True:
    countries = {"Singapore": "Although quite the small island, Singapore houses some pleasant views, luxerious hotels, and theme parks that can make one squeal! \n",
             "France": "France is home to amazing landscapes, although that's not the reason most people visit. Rather, it's for it's exotic food, being the romantic hotspot, and the Effiel Tower! \n",
             "Japan": "This place practically has everything, from amazing landscapes, silent places, technological innovation, and for famous videogame mascots being mainstream here. You could never go wrong with Japan! \n",
             "Canada": "Sometimes, cities are not for everyone. That's perfectly understandable! That's why Canada should be a must for those kinds of people, mostly being exotic views with some towns scattered about. Cities still lay, but they are clean, safe, friendly and multicultural. No reason not to visit this once! \n",
             "Australia": "Although weather is a big concern, Australia is home to exotic wildlife, intriguing places, soothing beaches and friendly people. It doesn't hurt to give this place a try! \n",
             "Thailand": "Home to multiple tropical islands, Thailand also sports some delicious food, some great nightlife, and exotic culture, Thailand is not a bad place to visit for your holidays! \n",
             "Portugal": "An odd choice, no one really talks about Portugal. However, with it's culture, amazing beaches, luxurious hotels, and friendly people, Portugal is the kind of place most tourists would go for a dream vacation. \n"}
    print("Welcome to the Travel Planner. Having trouble planning on where to go? Well, this travel planner has got you covered!")
    time.sleep(2)
    choice = input("Do you want to plan your travel, or check your current travel plans? You can also exit. ")
    if choice.lower() == "plan":
        for country, reason in countries.items():
            print(f"Country: {country}. {reason}")
            time.sleep(2)
        add = input("Which country would you like to visit? ")
        with open("Textfile1.txt", "a") as file:
           if add.title() in countries:
               file.write(add + "\n")
           else:
               print("Invalid country choice.")
    elif choice.lower() == "check":
        try:
            with open("Textfile1.txt", "r") as file:
                contents = file.read()
                if contents:
                    print("Your current travel plans:")
                    print(contents)
                else:
                    print("You have no current travel plans.")
        except FileNotFoundError:
            print("File 'Textfile1.txt' not found.")
        time.sleep(2)
    elif choice.lower() == "exit":
        print("Thanks for using the Travel Planner!")
        break
    else:
        print("That is an invalid answer.")
        continue

              