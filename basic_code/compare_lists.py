word1 = 'Seeschlange'
word1_set = set(word1.upper())
word1_list = sorted(word1_set)

word2 = 'Sechlang'
word2_set = set(word2.upper())
word2_list = sorted(word2_set)

if word1_list == word2_list:
    print('True')
else: 
    print('False') 

if word1_set == word2_set:
    print('True')
else: 
    print('False') 

# for sets there are not order
# as a result it is not a criteria 
# same elements of sets -> identicial sets!

print(word1_set)