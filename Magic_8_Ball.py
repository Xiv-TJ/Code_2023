import time
import random
answer = ["Yes", "No", "I just can't decide", "Possibly", "Possibly Not", "Of course!", "Defenitely not."]
while True:
    print("The Magic 8 Ball can perfectly predict your future, and answer any question you have on your mind, as long as it's yes, no!")
    time.sleep(5)
    choice = input("What is the question you so desperately need answers for? Answer Question for that. Or for your 8 Ball history, type History! ")
    if choice.lower() == "history":
        with open("History.txt", "r") as file:
            print(file.read())
            break
    elif choice.lower() == "question":
        print("Tell me your sacred question. ")
        question = input("")
        response = random.choice(answer)
        print(f"The answer is {response}.")
        with open("History.txt", "a") as file:
            file.write(f"Question: {question}, Answer: {response}.\n")
            break
    else:
        print("Invalid.")
              

