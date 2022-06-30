#Step 5
import os
import random
import hangman_art
import hangman_words

clear = lambda: os.system('cls')
logo = hangman_art.logo
print(logo)

stages = hangman_art.stages


end_of_game = False
word_list = hangman_words.word_list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)


print(f'Pssst, the solution is {chosen_word}.')

display = []
for _ in range(word_length):
    display += "_"

n = 0
guesses = []
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    
    clear()
    if guess in guesses:
        print(f"You have already guessed {guess}")
        
    else:

        for position in range(word_length):
            letter = chosen_word[position]

            if letter == guess:
                display[position] = letter

                    
        print(f"{' '.join(display)}")

        if guess not in chosen_word:
            print(f"The letter {guess} is not in the word, try another guess")
            n += 1
            print(stages[-1 -n])
            if n == len(stages) - 1:
                end_of_game = True
                print(f"You lost, the word was {chosen_word} try again")
                
        if "_" not in display:
            end_of_game = True
            print("You win.")

    guesses.append(guess)

        