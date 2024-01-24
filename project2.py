# Project of MADLIBS GENERATOR
# Story that has the replaced words, which user has to provide for each case.

# open FILE
path = 'C://Users//Alex-Internet//Dropbox//PROJECTS//Python//project1//madlib_story.txt'
with open(path, "r") as f:
    story = f.read()

# define a set() to use unique word and declare some variables
words = set()
start_of_word = -1
target_start = '<'
target_end = '>'

# get every words and add them to set of words
for i, char in enumerate(story):
    if char == target_start:
        start_of_word = i
    if char == target_end and start_of_word != -1:
        word = story[start_of_word : i + 1]
        words.add(word)
        start_of_word = -1

# Get answers from user and map to each word as value of key
answers = {}
for word in words:
    answer = input('Enter a word for ' + '"' + word + '"' + ': ' )
    answers[word] = answer

# Get each answer and replace it into the story
for word in words:
    story = story.replace(word, answers[word])

print('\n', story, '\n')
