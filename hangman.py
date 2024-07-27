import time
import random
import sys
from word_list import word_list

class flow_writing:
    def __init__(self, text):
        for char in text:
            sys.stdout.write(char) # printing w/ adding a new row
            sys.stdout.flush() # Stellt sicher, dass die Ausgabe sofort erfolgt
            time.sleep(0.05)

            if char in ".":
                time.sleep(0.5) 

# transform word 
    # e.g.: word 
    # WORD 
    # W O R D 
    # _ _ _ _ 

def game():
    # introduction 
    introduction_text = '''
Welcome to Hangman ... 
You think you can guess my word? ...
I don't think so ...
But we will see ... 
One small hint ... 
It's all about animal names ... 
\n'''
    flow_introduction_text = flow_writing(introduction_text)

# illustration
    # red underline 
    # big font 
    # flow_introduction_text = flow_writing(introduction_text)

    # computer chooses random word from word_list 
    searched_word = random.choice(word_list).upper()
    # set_searched_word = set(searched_word.upper())
    
    # lifes 
    lifes = 10 

    # display word 
    display = len(searched_word) * ['_']

    guessed_char = []
    guessed_char.sort()

    def show_display(): 
        print(' '.join(display))

    def guess_letter(letter):
        correct_guess = False
        for i in range(len(searched_word)): # i times amount of char in searched word, this for loop serves for going through each index of the searched word
            if searched_word[i] == letter: 
                display[i] = letter # exchange '_' with letter
                correct_guess = True 
        return correct_guess

    while "_" in display and lifes > 0:

        # check if the char was already being guessed 
            # list 
            # if guess in list 
                # try again
            # else:
                # add guess to list 
            # needs to be in the alphabet 
            # should be sorted -> list 

            # print list

        show_display()
        print(f'Amount of lives: {lifes}')
        print(f'Guessed letters: {guessed_char}')
        guess = input("What character do you guess?: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_char: 
                print('You already guessed that letter. Please try again!')
            
            else: 
                guessed_char.append(guess)

            if not guess_letter(guess): # if False 
                print(f"The character '{guess}' is not part of the searched word.")
                lifes -= 1 
        else:
            print("Your input was invalid! Please try again.")
            
    if lifes == 0: 
        print(f'Sorry, you lost this game! The searched word was {searched_word}.')
    
    else: 
        print(f'Congrates, you won the game! The searched word was {searched_word}.')



game()