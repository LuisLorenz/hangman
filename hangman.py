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

def game():
    # introduction 
    introduction_text = '''
Welcome to Hangman ... 
You think you can guess my word? ...
I don't think so ...
But we will see ... 
'''
# illustration
    # red underline 
    # big font 
    # flow_introduction_text = flow_writing(introduction_text)

    # computer chooses random word from word_list 
    searched_word = random.choice(word_list)
    print(searched_word)

    # while loop
        # amount of char is shown to the user
        # user guesses 

    # result
        # lifes run out
        # word was guessed correctly 

game()