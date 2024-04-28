from art import logo,vs
from game_data import data
# from art import vs
import random

# Format the account data into printable format
def formating(account):
    account_name = account['name']
    account_desc = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_desc}, from {account_country}"

# Check if user is correct
def check_answer(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == "a" #kalo a dia return true karena itu ==
        # if guess == "a":
        #     return True
        # else:
        #     return False
    else:
        return guess == "b"


# display
print(logo)
score=0
game_should_continue = True

account_b = random.choice(data)

# Generate random account
# Make game repeatable
while game_should_continue == True:
# Making account at position B become position A
    account_a = account_b
    account_b = random.choice(data)

    while account_a == account_b:
        account_b = random.choice(data)

    print (f"Compare A: {formating(account_a)}")

    print(vs)

    print (f"Compare B: {formating(account_b)}") 
    
    # Ask user for a guess
    guess = input("Who has more followers? Type 'A' or 'B':").lower()

    is_correct = check_answer(guess,account_a["follower_count"],account_b["follower_count"])
    print(is_correct)

    # Give user feedback after guess
    # Score keeping

    if is_correct == True:
        score += 1
        print(f"You are right! Current Score : {score}.")
    else:
        print(f"Sorry, that is wrong. Your total score is {score}.")
        game_should_continue = False




# Clear the screen after answers
