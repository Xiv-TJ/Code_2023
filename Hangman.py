import random
print("Welcome to Hangman; Fruit Edition! Soon, a random fruit will be chosen, and you will have seven guesses to find the fruit by staing cartain words.")
def fruit():
    fruits = ["apple", 'banana', "cherry", "orange", "pineapple", "strawberry", "lemon", "watermelon", "mango", "grape", "coconut"]
    chosen = random.choice(fruits)
    return chosen
def display(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display
while True:
    word = fruit()
    guessed_letters = []
    attempts = 7
    print("A fruit has been chosen! Start guessing!")
    while attempts > 0:
        print(f"Word: {display(word, guessed_letters)}.")
        print(f"Attempts left: {attempts}.")
        guess = input("What is your word?: ")
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue
        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue
        guessed_letters.append(guess)
        if guess in word:
            if all(letter in guessed_letters for letter in word):
                print(f"You won the game! The letter was {word}!")
                break
            else:
                print("Good guessing!")
        else:
            print("Sorry! Incorrect!")
            attempts -= 1
    if attempts == 0:
        print(f"Sorry! You ran out of attempts! The word is {word}!")
        break
    
        

