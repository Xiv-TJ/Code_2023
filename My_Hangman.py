import time
import random
def hangman(words):
    chosen_word = random.choice(list(words.keys()))
    attempts = 5
    countdown = 60
    guess_word = ["_"] * len((chosen_word))
    while attempts and countdown > 0:
        print(guess_word)
        guess = input("What is your guess? \n")
        if len(guess) != 1 or not guess.isalpha():
            print("That is not an appropriate guess. Please try again.")
            continue
        else:
            answer = guess
        if answer in chosen_word:
            for i in range(len(chosen_word)):
                if chosen_word[i] == answer:
                    guess_word[i] = answer
                    print(" ".join(guess_word))
        else:
            attempts -= 1
            print("You were wrong! Try again!")
        if "_" not in guess_word:
            print("You won!")
            break
        time.sleep(1)
        countdown -= 1
    if "_" in guess_word:
        print(f"Sorry, you lost. The word is {chosen_word}. Try again!")
print("Let's play Hangman!")
words = {"mall": "mall", "plaza": "plaza", "club": "club", "school": "school", "house": "house", "hotel": "hotel", "restaurant": "restaurant", "shop": "shop", "park": "park", "office": "office"}
hangman(words)
        