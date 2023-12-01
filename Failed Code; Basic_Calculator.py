name = input("Before you continue, please write your name down. ")
print("Welcome, " + str(name) + ", to the Basic Calculator.")
while True:
    equation = input("What equation would you like to find out? \nA: Addition \nB:Subtraction \nC:Multiplication \nD: Division")
    if equation == "A":
        def add (num1, num2):
            num1 = float(input("What is the value of Number 1?: "))
            num2 = float(input("What is the value of Number 2?: "))
            print("The value is, ")
            return num1 + num2
    elif equation == "B":
        def subtract (num1, num2):
            num1 = float(input("What is the value of Number 1?: "))
            num2 = float(input("What is the value of Number 2?: "))
            print("The value is, ")
            return num1 - num2
    elif equation == "C":
        def multiply (num1, num2):
            num1 = float(input("What is the value of Number 1?: "))
            num2 = float(input("What is the value of Number 2?: "))
            print("The value is, ")
            return num1 * num2
    elif equation == "D":
        def divide (num1, num2):
            num1 = float(input("What is the value of Number 1?: "))
            num2 = float(input("What is the value of Number 2?: "))
            print("The value is, ")
            return num1 / num2
    else:
        print("Please pick the above options mentioned.")
        continue
    
    