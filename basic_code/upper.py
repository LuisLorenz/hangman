# creating a list of char of a word

word = 'Regenbogen'

char_list = [char.upper() for char in word]

print(char_list)

# ['R', 'e', 'g', 'e', 'n', 'b', 'o', 'g', 'e', 'n']

# ['R', 'E', 'G', 'E', 'N', 'B', 'O', 'G', 'E', 'N']

guess = 'r'

guess_upper = guess.upper()
print(guess_upper)
# R

if guess_upper in char_list: 
    print('Your guess was correct')
else:
    print('Your guess was wrong.')