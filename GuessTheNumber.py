import random
print("Ginna and You are out in the park, when she gives off a big smile. \n'Let's play Guess the Number!' Ginna said. \nYou smile, ready for the challenge.")
while True:
    try:
        def ginna_num():
            return random.randint(1, 20)
        num = input("What is your guess? ")
        if 1 <= int(num) <= 20:
            print("Your number is " + str(int(num)) + "!")
            ginna_number = ginna_num()
            print("Ginna's number is... " + str(int(ginna_number)) + "!")
        else:
            print("Please pick a number between 1 and 20.")
            continue
        if int(num) == int(ginna_number):
            print("You won the game!")
            break
        elif int(num) > int(ginna_number):
            print("Your guess is too high. Try again.")
            continue
        else:
            print("Your guess to too low. Try again.")
            continue
    except ValueError:
        print("Please type down a number.")
