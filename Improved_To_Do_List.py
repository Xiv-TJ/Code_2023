import time
def to_do():
    for tasks in list:
        print(f"{tasks}")
list = {"Take a Shower",
        "Eat Breakfast"}
while True:
    print("Here is your To-Do list. Tasks which you need finished will show up here.")
    time.sleep(3)
    choice = input("You can either read, add or remove tasks from the To-Do list. Additionally, you can leave, too. What would you like to do? ")
    if choice.lower() == "read":
        with open("Textfile2.txt", "r") as file:
            contents = file.read()
            print(contents)
    elif choice.lower() == "add":
        with open("Textfile2.txt", "a") as file:
            new_chore = input("What new chore would you like to add? ")
            file.write(new_chore + "\n")
            print("Chore added successfully!")
    elif choice.lower() == "remove":
        with open("Textfile2.txt", "r") as file:
            chores = file.readlines()
        print("Current list of Chores: ")
        for index, chore in enumerate(chores,  start=1):
            print(f"{index}. {chore.strip()}")
        remove = int(input("Which chore would you like to remove? Press the number beside it to do so. ")) - 1
        if 0 <= remove < len(chores):
            removed_chore = chores.pop(remove)
            print(f"You have removed {removed_chore.strip()}!")
            with open("Textfile2.txt", "w") as file:
                for chore in chores:
                    file.write(chore)
        else:
            print("This number is invalid.")
    elif choice.lower() == "exit":
        print("See you soon!")
        break
    else:
        print("Please input a valid answer.")
        continue
    

