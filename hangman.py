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

    # variables
    char_guess = None 
    guessed_char = set(' ')
        # simply add only the character that are not already in the list 
        # this way I can sort immediately 
    char_searched_word = set()


    
    # computer chooses random word from word_list 
    searched_word = random.choice(word_list).upper()
    # set_searched_word = set(searched_word.upper())
    

    # lifes 
    lifes = 10 

    # correct_word_guess = False 
    # correct_char = set()

    # alt while loop 

    # display word 
    display = len(searched_word) * ['_']

    def show_display(): 
        print(' '.join(display))

    def guess_letter(letter):
        correct_guess = False
        for i in range(len(searched_word)): 
            if searched_word[i] == letter: 
                display[i] = letter 
                correct_guess = True 
        return correct_guess

    while "_" in display and lifes > 0:
        show_display()
        guess = input("What character do you guess?: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if not guess_letter(guess):
                print(f"The character '{guess}' is not part of the searched word.")
                lifes -= 1 
        else:
            print("Your input was invalid! Please try again.")
            
    if lifes == 0: 
        print(f'Sorry, you lost this game! The searched word was {searched_word}.')
    
    else: 
        print(f'Congrates, you won the game! The searched word was {searched_word}.')


    # while loop
#     while lifes > 0 and correct_word_guess == False: 
#         # amount of char is shown to the user
#         print(f'Amount of lifes: {lifes}')

#         formated_searched_word = ' '.join([ '_' for char in searched_word])

#         print(f'Your guesse {guessed_char}')

# # improve formating...

#         # user guesses
#         char_guess = input('Guess a new character').upper()

#         if char_guess not in guessed_char:
#             guessed_char.append(char_guess)

#             if char_guess in set_searched_word:
#                 print('You guess was correct!')
#                 correct_char.append(char_guess)

#                 if set_searched_word == correct_char:
#                     correct_word_guess = True 

#             else: 
#                 print(f'Your guess was false.')
#                 lifes -= 1 

#         elif char_guess in guessed_char:
#             print('You already guessed this character.')
#         else:
#             print('Your input was invalid. Please try again!')

#     if correct_word_guess == True:
#         print(f'Congrates, you won the game! The searched word was {searched_word}.')
    
#     else:
#         print(f'Sorry, you lost this game! The searched word was {searched_word}.')

        # checking if both lists - guessed_char and char_searched_word are identically e.g. 

    # result
        # lifes run out
        # word was guessed correctly 

game()