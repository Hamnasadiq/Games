# HANGMAN GAME .....
print("<---------Welcome to Hangman Game!-------->")
print("\nGuess the word! Each incorrect guess will cost you a life.")

# Import random words
import random
words=['Thunder','Husky','Zombie','Diamond','Mystery','Castle','Vampire']
words = [word.lower() for word in words]
selected_word=random.choice(words)
print(f"Hint: The word starts with '{selected_word[0].lower()}'")
blank_space="_"*len(selected_word) 
lives=3
#game loop
while '_'in blank_space and lives>0:
    print(f"Lives: {lives}") 
    print(blank_space)
    user_guess = input("Guess a letter: ").lower()
    if user_guess in selected_word:
        print("Good guess!\n")
        display=""
        for i in range(len(selected_word)) :
            if selected_word[i]==user_guess:
                display+=user_guess
            else:
                display+=blank_space[i]
        blank_space=display
    else:
        lives-=1
        print("\nIncorrect guess, try again!")
if lives > 0:
    print(f"\nCongrats! You've guessed the word correctly:{selected_word}")
else:
    print(f"\nOops! you lost, The word was: {selected_word}")
