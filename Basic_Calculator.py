name = input("Before you continue, please write your name down here. ")
print("Welcome, " + str(name) + ". This is the Basic Calculator.")
while True:
    try:
        equations = input("Which equation would you like to find? \nA: Addition \nB: Subtraction \nC: Multiplication \nD: Division ")
        def add(num1, num2):
            return num1 + num2
        def subtract(num1, num2):
            return num1 - num2
        def multiply(num1, num2):
            return num1 * num2
        def divide(num1, num2):
            return num1 / num2
        if equations == "A":
            num1 = float(input("What is Number 1?: "))
            num2 = float(input("What is Number 2?: "))
            print("The overall value of the two numbers is " + str(int(add(num1, num2))) + "!")
            break
        elif equations == "B":
            num1 = float(input("What is Number 1?: "))
            num2 = float(input("What is Number 2?: "))
            print("The overall value of the two numbers is " + str(int(subtract(num1, num2))) + "!")
            break
        elif equations == "C":
            num1 = float(input("What is Number 1?: "))
            num2 = float(input("What is Number 2?: "))
            print("The overall value of the two numbers is " + str(int(multiply(num1, num2))) + "!")
            break
        elif equations == "D":
            num1 = float(input("What is Number 1?: "))
            num2 = float(input("What is Number 2?: "))
            print("The overall value of the two numbers is " + str(int(divide(num1, num2))) + "!")
            break
        else:
            print("Please pick a number.")
            continue
    except ValueError:
        print("Please type down a number.")
