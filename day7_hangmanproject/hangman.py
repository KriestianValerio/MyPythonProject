#THE HANGMAN PROJECT
import random
# import word_list 


from word_list import hangman_word
chosen_word = random.choice(hangman_word) 

from logo import title
print(title)

lives = 6

print(f"psst the word is unpredictable")

display = []
for char in range(0,len(chosen_word)): #bisa juga langsung for char in chosen_word
    display += "_"

end_of_game = True #kalo originalnya pake end_of_game = false 
while end_of_game: #tapi ini pake while not end_of_game
    guess = input("guess a letter:").lower()

    if guess in display:
        print(f"You have already guessed {guess},try again")

    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that is not in the word. You lose a life.")
        if lives == 0:
            end_of_game = False
            print("You Lose, Try Again.") 
            

    print(f"{' '.join(display)}") # fungsinya : dia menjoin list display dengan space (' ')



    if "_" not in display:
        end_of_game = False # Stopping condition
        print("You WIN!")

    from hangmanimage import stages
    print(stages[lives])

   



    



