# ~~~~~~~~~~~~~~~~~~
# 'HANGMAN GAME
# Try to guess word
# ~~~~~~~~~~~~~~~~~~

import random
tries = 8  # number of lives

print('H A N G M A N')
# the game menu
while True:
    play_exit = input('Type "play" to play the game, "exit" to quit: ')
    if play_exit == 'exit':
        exit()
    elif play_exit == 'play':
        break

# list of words and random choice
hangman_list = ['python', 'java', 'kotlin', 'javascript']
hangman_word = random.choice(hangman_list)
# hangman_word = 'java'
# print("choice:", hangman_word)
hangman_word_secret = "-" * (len(hangman_word))
user_letter_list = []  # RIGHT user letters from guessed word
user_input_list = []  # ALL user letters

while True:  # guessed iterations
    print('')
    print(hangman_word_secret)

    # checking if the whole word have been already guessed
    if '-' not in hangman_word_secret:
        print('You guessed the word {}!' .format(hangman_word_secret))
        print('You survived!')
        break

    # receiving the letter for guessing
    user_letter = input("Input a letter: ")

    # checking if the letter have been already guessed
    if ((user_letter in user_letter_list) or (user_letter in user_input_list)) and (len(user_letter) == 1):
        print("You've already guessed this letter")
        continue
    user_input_list.append(user_letter)

    # checking if the letter haven't been single
    if len(user_letter) != 1:
        print("You should input a single letter")
        continue

    # checking if the letter have been lowercase English letter
    if user_letter == user_letter.upper():
        print("Please enter a lowercase English letter")
        continue

    # if the letter have been guessed
    if user_letter in hangman_word:
        hangman_word_secret = ""
        user_letter_list.append(user_letter)
        for i in hangman_word:
            if i in user_letter_list:
                hangman_word_secret = hangman_word_secret + i
            else:
                hangman_word_secret = hangman_word_secret + "-"
    else:  # if the letter haven't been guessed
        tries -= 1
        print("That letter doesn't appear in the word")
        if tries <= 0:  # if the last try used then game over
            print("You lost!")
            break
