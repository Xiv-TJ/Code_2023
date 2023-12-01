import random
print("In this math test, no calculators are allowed. \nOnly 10 questions shall be asked. \nYou must get at least an overall of 60% to pass. \nIf you fail, you must restart the test again.")
name = input("Please write down your name on the paper. ")
while True:    
    print("The test is about to begin.")
    questions = {
    "If I have 25 apples, and you had 6/5 as much as me, how many apples do you have?": "30",
    "What is the area of a triangle with height 50 and length 5?": "125",
    "If the area of a square is 121, what is the length of one of it's sides?": "11",
    "What is the value of pi, in 3 digits?": "3.14",
    "How many digits are there in 1000000?": "7",
    "Write down five million, eighty-seven thousand, six hundred and thirty-four in numerals.": "5870634",
    "What comes 13 digits after 673?": "686",
    "If the length of a rectangle is 10cm, and the width of the rectangle is 7/5ths as much, what is the area of the rectangle?": "140",
    "The area of a triangle is 700cm, and the height of said triangle was 100cm. What is it's length?": "14",
    "What kind of fraction does 0.69 form?": "69/100",
    "What is 80% in fractions?": "4/5",
    "Billy has 66 marbles, while Abby has 24 marbles and Carl has 75 marbles. What is their average?": "55",
    "What is 4+4?": "8",
    "The area of a circle, using 3.14 as pi, is 200.96. \nWhat is the diameter of the circle?": "16",
    "What is 896/1792 in percentage?": "50%",
    "Joseph has earn $1782. \nHowever, due to costs, he is only able to save 1/3 of the money. \n7/12 of the money spent is on grocerries. How much did he spend on grocerries?": "$693",
    "Valentino and Christopher have $66 on average. \nChristopher has about 5/6 of the money mentioned. \nHow much does Christopher need to give Valentino so they can have the same amount of money?": "$44",
    "Does 66+44 equal to 100?": "No",
    "The height and length of a triangle are 26cm and 13cm respectively. \nThe area of a square is the same as the triangle mentioned. \nWhat is the length of one side of the square?": "13",
    "Give me a number between 1 and 50. \nIt must not divisible by 2 or 5. \nIt must be a whole number. \nIt must be a multiple of 7. \nIt must have at least two digits.": "21" or "49",
    "Qistina wants to buy 20 chocolates. \nStore A sells 4 chocolates for $3.50. \nStore B sells 5 chocolates for $3.80. \n Whihc store should Qistina buy from?": "Store B",
    "What is 7x9?": "63",
    "Savannah has 50 strawberries, while Zoey has 80. What is their average?": "65",
    "Write down 4368 in words.": "Four thousand three hundred and sixty-eight",
    "What is the lowest common factor 3 and 4?": "12"
}

    chosen_questions = random.sample(list(questions.items()), k=10)
    score = 0
    for (questions, solution) in chosen_questions:
        print(questions)
        answer = input("What is your answer?: ")
        if answer == solution:
            print("You got it right!")
            score += 1
        else:
            print("Sorry. You got it wrong. The correct answer is " + str(solution) + ".")
    percentage = (score / 10) * 100
    if int(percentage) >= 60:
        print("You have passed the test, with a score of " + str(int(percentage)) + "!\nCongratulations, " + str(name) + "!")
        break
    else:
        print("Sorry. You have failed, with a score of " + str(int(percentage)) + ".\nTry again.")
        continue