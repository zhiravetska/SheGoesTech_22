# 1. Confusion

# The user enters a name.

# You print user name in reverse (should begin with capital letter)
#  then extra text: ",a thorough mess is it not ", then the first name of the user name then "?"

# Example:

# Enter: Valdis -> Output: Sidlav, a thorough mess is it not V?

# import string
# name = input("Enter your name")

# print(name)
# backward_name = name[::-1]  # reverse not for using in names of variables
# print(f"{backward_name}, a thorough mess is it not {name} ?")


# 2. Almost Hangman (complete a full game)

# Write a program to recognize a text symbol

# The user (first player) enters the text.

# Only asterisks instead of letters are output.

# Assume that there are no numbers, but there may be spaces.

# The user (i.e. the other player) enters the symbol.

# If the letter is found, then the letter is displayed in ALL the appropriate places, all other letters remain asterisks.

# Example:

# First input: Kartupeļu lauks -> ********* *****

# Second input: a -> *a****** *a***


# In principle, this is a good start to the game of hangman.

# https://en.wikipedia.org/wiki/Hangman_(game)

# MY CODE
# TODO to finish this game/////
text = input("Īnput a text: ")
textInAst = ""
# print("*"*len(text))
for c in text:
    if c == ' ':
        textInAst += " "
    else:
        textInAst += "*"
print(textInAst)
letter = input("Enter a letter: ")
textInLet = ""
for c in text:
    if c == letter:
        textInLet += c
    elif c == ' ':
        textInLet += " "
    else:
        textInLet += "*"
print(textInLet)
letter2 = input("Enter another letter: ")
textInLet2 = textInLet
for a in textInLet2:
    if a == letter2:
        textInLet2 += a
    elif a == letter:
        textInLet2 += c
    elif a == ' ':
        textInLet2 += " "
    else:
        textInLet2 += "*"
print(textInLet2)


# END OF MY CODE


# 3. Text conversion

# Write a program for text conversion

# Save user input

# Print the entered text without changes

# Exception: if the words in the input are not .... bad,
# then the output is not ...  bad section must be changed to is good

# text = input("Input a text: ")
# print(text)
# newText = text.replace('bad', 'good')
# print(newText)

# Examples:

# The weather is not bad -> The weather is good

# The car is not new -> The car is not new

# This cottage cheese is not so bad -> This cottage cheese is good

# Hints:

# Find (or index, or even rfind) will probably come in handy, as may an operator. Also slice syntax will be useful.

# Extra: How would you do this task in Latvian language (nav slikts/a -> ir labs/a)?
