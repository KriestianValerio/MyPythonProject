EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5
turns = 0

# Function to check user's guess and compare
def check_answer(guess,answer,turns):
    """Checks answer against guessed number, Returns the number of turns remaining."""
    if guess > answer:
        print("That is too High!")
        return turns - 1
    elif guess < answer:
        print("That is too low!")
        return turns - 1
    else:
        print(f"You guessed {guess}, and that is correct!")

# Make function to set difficulty
def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

# Choosing a random number 1-100
import random
def gamecode():
    print("Welcome to The Number Guessing Game!")
    print("Hey, I'm Rio, I'm currently thinking of a number between 1 and 100.")
    answer = random.randint(1,100)
    # print(f"Psst, the answer is {answer}")
    turns = set_difficulty()
    guess = 0 # cuma buat pajangan
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        # Let user guess a number
        guess = int(input("Make a guess:"))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You ran out of attempts, you lose!")
            return
        elif guess != answer:
            print("Guess Again.")

gamecode()



# Track number of turns and reduce by 1 if wrong

# Repeat guessing if wrong 




