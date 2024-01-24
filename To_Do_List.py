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
        print(to_do())
    elif choice.lower() == "add":
        while True:
            task = input("What task would you like to add? ")
            list.add(task)
            print("Task successfully added!")
            time.sleep(2)
            break
    elif choice.lower() == "remove":
        while True:
            for tasks in list:
                print(f"{tasks}")
            time.sleep(2)
            remove = input("Which task would you like to remove? ")
            if remove in list:
                list.remove(remove)
                print("Task successfully removed!")
                time.sleep(2)
                break
            else:
                print("Invalid Choice.")
    elif choice.lower() == "exit":
        print("See you soon!")
        break
    else:
        print("Please input a valid answer.")
        continue
    