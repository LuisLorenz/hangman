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

            if char in ".!?":
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
Small hint ... 
It's all about animal names ... 
'''
# illustration
    # red underline 
    # big font 
    # flow_introduction_text = flow_writing(introduction_text)

    # computer chooses random word from word_list 
    searched_word = random.choice(word_list)
    print(searched_word)

    # lifes 
    lifes = 10 

    correct_word_guess = False 

    # while loop
    while lifes < 10 and correct_word_guess == False: 
        # amount of char is shown to the user
        print(f'Amount of lifes: {lifes}')
    

        # user guesses 

    # result
        # lifes run out
        # word was guessed correctly 

game()