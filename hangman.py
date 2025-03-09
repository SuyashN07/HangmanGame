import random

def pick_word():
    words = [
        "apple", "banana", "orange", "grape", "mango", "water", "coffee", "tea",
        "bottle", "glass", "plate", "spoon", "fork", "knife", "chair", "table",
        "laptop", "mobile", "charger", "headphones", "keyboard", "mouse", "screen",
        "pencil", "pen", "eraser", "paper", "notebook", "book", "school", "college",
        "teacher", "student", "classroom", "board", "marker", "lesson", "homework",
        "bus", "train", "car", "bike", "road", "street", "traffic", "signal",
        "market", "shop", "mall", "money", "wallet", "bag", "clothes", "shoes",
        "television", "remote", "fan", "light", "door", "window", "curtain", "floor",
        "kitchen", "bedroom", "bathroom", "hall", "sofa", "bed", "pillow", "blanket",
        "morning", "afternoon", "evening", "night", "breakfast", "lunch", "dinner",
        "family", "friend", "neighbor", "office", "meeting", "email", "message",
        "holiday", "weekend", "vacation", "birthday", "festival", "celebration"
    ]
    return random.choice(words)

def show_word(word, guesses):
    displayed = ""
    for letter in word:
        if letter in guesses:
            displayed += letter + " "
        else:
            displayed += "_ "
    return displayed.strip()

def success_msg():
    return random.choice([
        "Great job!", "Nice one!", "Correct!", 
        "Well done!", "You got it!", "Perfect!"
    ])

def fail_msg():
    return random.choice([
        "Oops! Wrong guess.", "Not this time.", "Try again!", 
        "Nope!", "Missed it!", "Keep trying!"
    ])

def hangman():
    word = pick_word()
    guesses = set()
    tries = 6

    print("\n--- Welcome to Hangman! Guess the word. ---\n")

    while tries > 0:
        print(show_word(word, guesses))
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Try one letter.")
            continue

        if guess in guesses:
            print("Already guessed. Try another.")
            continue

        guesses.add(guess)

        if guess in word:
            print(success_msg())
        else:
            tries -= 1
            print(fail_msg())
            print(f"{tries} tries left!")

        if all(letter in guesses for letter in word):
            print(f"\nYou won! The word was: {word}")
            return

    print(f"\nGame over! The word was: {word}")

ch = 1
while ch:
    hangman()
    try:
        while 1:
            c = input("Do you want to play again?(Y/N) ")
            if c.lower() == 'y':
                continue
            elif c.lower() == 'n':
                print("Thanks for playing!!!")
                ch = 0
                break
            else:
                "Enter a valid alphabet"
    except:
        print("Some Error Occurred. Try again later.")