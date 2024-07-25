# # Das Wort, das erraten werden soll
# word = "HAUS"

# # Erstellen einer Liste für den aktuellen Stand des gerateten Wortes
# display = ["_"] * len(word) # "_", "_", "_", "_" 

# # Funktion, um das aktuelle Display-Format zu zeigen
# def show_display():
#     print(" ".join(display)) # _ _ _ _ 

# # Funktion, um den Buchstaben zu raten
# def guess_letter(letter):
#     correct_guess = False
#     for i in range(len(word)): # indexing each char in word 
#         if word[i] == letter: # showing 
#             display[i] = letter # '_' gets exchanged by the correct letter for the specific index 
#             correct_guess = True # answer gets returned 
#     return correct_guess

# # Spiel-Loop
# while "_" in display:
#     show_display()
#     guess = input("Raten Sie einen Buchstaben: ").upper()
#     if len(guess) == 1 and guess.isalpha():
#         if not guess_letter(guess):
#             print(f"Der Buchstabe '{guess}' ist nicht im Wort.")
#     else:
#         print("Bitte geben Sie einen einzelnen Buchstaben ein.")
        
# show_display()
# print("Herzlichen Glückwunsch! Sie haben das Wort erraten.")


word = "SEESCHLANGE"
display = ["_"] * len(word)

def show_display():
    print(" ".join(display))

def guess_letter(letter): # letter is simply an arg, this can be exchange -> guess 
    correct_guess = False
    for i in range(len(word)): 
        if word[i] == letter: 
            display[i] = letter 
            correct_guess = True 
    return correct_guess

while "_" in display:
    show_display()
    guess = input("Raten Sie einen Buchstaben: ").upper()
    if len(guess) == 1 and guess.isalpha():
        if not guess_letter(guess):
            print(f"Der Buchstabe '{guess}' ist nicht im Wort.")
    else:
        print("Bitte geben Sie einen einzelnen Buchstaben ein.")
        
show_display()
print("Herzlichen Glückwunsch! Sie haben das Wort erraten.")