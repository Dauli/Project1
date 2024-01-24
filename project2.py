# Project of MADLIBS GENERATOR
# Story that has the replaced words, which user has to provide for each case.

path = 'C://Users//Alex-Internet//Dropbox//PROJECTS//Python//project1//madlib_story.txt'
with open(path, "r") as f:
    story = f.read()

words = set()
start_of_word = -1

target_start = '<'
target_end = '>'

for i, char in enumerate(story):
    if char == target_start:
        start_of_word = i
    if char == target_end and start_of_word != -1:
        word = story[start_of_word : i + 1]
        words.add(word)
        start_of_word = -1

print(words)
