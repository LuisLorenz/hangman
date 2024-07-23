word = 'Regenbogen'
word_set = set(word.upper())
word_list =list(word_set)
word_list.sort() 
print(word_list)
# {'b', 'n', 'R', 'g', 'o', 'e'}
# {'R', 'G', 'N', 'E', 'O', 'B'}

# ['B', 'E', 'G', 'N', 'O', 'R']

word = 'Schlange'
word_set = set(word.upper())
word_list = sorted(word_set) # creating a list and sort it in the some step 
print(word_list)
word_set = set(word_list)
print(word_list)