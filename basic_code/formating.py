word = "python"
# at this point there is just one word and no list

formatted_word = ' '.join([char.upper() for char in word])
    # each character gets separated 
    # list is created for each separated char which gets into upper chase 
print(formatted_word)

# creating format: word -> _ _ _ _ 
formatted_word_v2 = ' '.join([ '_' for char in word])
print(formatted_word_v2)
# _ _ _ _ _ _

# changing every char to the right char that was guessed correctly ... 