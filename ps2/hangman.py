# Problem Set 2, hangman.py
# Name:
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------


# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


# checks if a letter is in the guessed letters
def check_list(letter, letters_guessed):  # CUSTOM FUNCTION
    for item in letters_guessed:
        if item == letter:
            return True
    return False


def word_contains_letter(guess, secret_word):  # CUSTOM FUNCTION
    for letter in secret_word:
        if(guess == letter):
            return True
    return False


def guess_is_valid(guess):  # CUSTOM FUNCTION
    all_letters = 'abcdefghijklmnopqrstuvwxyz'

    valid_guess = False
    for letter in all_letters:
        if letter == guess:
            valid_guess = True

    return valid_guess


def is_word_guessed(secret_word, letters_guessed):  # DONE
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''

    # FILL IN YOUR CODE HERE AND DELETE "pass"
    word_is_guessed = False
    count = 0
    secret_word_length = len(secret_word)

    # count each letter that has been successfully found
    for letter in secret_word:
        if check_list(letter, letters_guessed):
            count += 1

    # if the count is equal to the length of the word then the player has found all letters
    if(secret_word_length == count):
        word_is_guessed = True

    return word_is_guessed


def get_guessed_word(secret_word, letters_guessed):  # DONE
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    return_string = ''

    for letter in secret_word:
        if check_list(letter, letters_guessed):
            return_string += letter + ' '
        else:
            return_string += '_' + ' '

    return_string = return_string[:-1]

    return return_string


def get_available_letters(letters_guessed):  # DONE
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    all_letters = 'abcdefghijklmnopqrstuvwxyz'

    for letter in letters_guessed:
        all_letters = all_letters.replace(letter, '')

    return all_letters


def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    game_won = False
    guesses_remaining = 6
    warnings_remaining = 3
    letters_guessed = ''
    total_score = 0

    print('Welcome to the game Hangman!')
    print('I am thinking of a word that is ' +
          str(len(secret_word))+' letters long.')
    print('You have ', warnings_remaining, ' warnings remaining.')
    print('-----------------------------------------------')

    while not(game_won) and guesses_remaining > 0:
        print('You have ', guesses_remaining, ' guesses remaining.')
        print('Available letters: ', get_available_letters(letters_guessed))
        new_letter = input('guess a letter: ').lower()

        # check user input and process warning/penalty as necessary
        if len(new_letter) > 1:
            if warnings_remaining > 0:
                warnings_remaining -= 1
                print('Oops! You must only guess a single letter. You have ' + str(warnings_remaining) +
                      ' warnings remaining: ' + get_guessed_word(secret_word, letters_guessed))
                print('-----------------------------------------------')
                continue
            else:
                guesses_remaining -= 1
                print('Oops! You must only guess a single letter. You have ' + str(guesses_remaining) +
                      ' guesses remaining: ' + get_guessed_word(secret_word, letters_guessed))
                print('-----------------------------------------------')
                continue

        if not(guess_is_valid(new_letter)):
            if warnings_remaining > 0:
                warnings_remaining -= 1
                print('Oops! That is not a valid letter. You have ' + str(warnings_remaining) +
                      ' warnings remaining: ' + get_guessed_word(secret_word, letters_guessed))
                print('-----------------------------------------------')
                continue
            else:
                guesses_remaining -= 1
                print('Oops! That is not a valid letter. You have ' + str(guesses_remaining) +
                      ' guesses remaining: ' + get_guessed_word(secret_word, letters_guessed))
                print('-----------------------------------------------')
                continue

        if check_list(new_letter, letters_guessed):
            if warnings_remaining > 0:
                warnings_remaining -= 1
                print('Oops! You have already guessed that letter. You have ' + str(warnings_remaining) +
                      ' warnings remaining: ' + get_guessed_word(secret_word, letters_guessed))
                print('-----------------------------------------------')
                continue
            else:
                guesses_remaining -= 1
                print('Oops! You have already guessed that letter. You have ' + str(guesses_remaining) +
                      ' guesses remaining: ' + get_guessed_word(secret_word, letters_guessed))
                print('-----------------------------------------------')
                continue

        letters_guessed = letters_guessed + new_letter

        # check if letter is in secret word
        if word_contains_letter(new_letter, secret_word):
            print('Good Guess: ' + get_guessed_word(secret_word, letters_guessed))
            print('-----------------------------------------------')

        # let user know they've guessed wrong
        else:
            vowels = 'aeiou'
            vowel_guessed = False
            for letter in vowels:
                if letter == new_letter:
                    vowel_guessed = True

            if vowel_guessed:
                guesses_remaining -= 2
            else:
                guesses_remaining -= 1

            print('Oops! That letter is not in my word: ' +
                  get_guessed_word(secret_word, letters_guessed))
            print('-----------------------------------------------')

        if is_word_guessed(secret_word, letters_guessed):
            game_won = True
            total_score = len(letters_guessed) * guesses_remaining

    if game_won:
        print('Congratulations, you won!')
        print('Your total score for this game was: ' + str(total_score))
    else:
        print('Sorry, you ran out of guesses. The word was ' + secret_word + '.')

# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
# (hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------


def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    my_word = my_word.replace(" ", "")

    if len(my_word) != len(other_word):
        return False

    for i in range(0, len(my_word)):
        if my_word[i] == '_':
            continue
        if my_word[i] != other_word[i]:
            return False

    return True


def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    matching_words = []

    for word in wordlist:
        if match_with_gaps(my_word, word):
            matching_words.append(word)

    final_string = ''
    for word in matching_words:
        final_string = final_string + " " + word

    print('Possible word matches are:')
    print(final_string)
    print('-----------------------------------------------')
    return


def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.

    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    game_won = False
    guesses_remaining = 6
    warnings_remaining = 3
    letters_guessed = ''
    total_score = 0

    print('Welcome to the game Hangman!')
    print('I am thinking of a word that is ' +
          str(len(secret_word))+' letters long.')
    print('You have ', warnings_remaining, ' warnings remaining.')
    print('-----------------------------------------------')

    while not(game_won) and guesses_remaining > 0:
        print('You have ', guesses_remaining, ' guesses remaining.')
        print('Available letters: ', get_available_letters(letters_guessed))
        new_letter = input('guess a letter: ').lower()

        # check user input and process warning/penalty as necessary
        if len(new_letter) > 1:
            if warnings_remaining > 0:
                warnings_remaining -= 1
                print('Oops! You must only guess a single letter. You have ' + str(warnings_remaining) +
                      ' warnings remaining: ' + get_guessed_word(secret_word, letters_guessed))
                print('-----------------------------------------------')
                continue
            else:
                guesses_remaining -= 1
                print('Oops! You must only guess a single letter. You have ' + str(guesses_remaining) +
                      ' guesses remaining: ' + get_guessed_word(secret_word, letters_guessed))
                print('-----------------------------------------------')
                continue

        if new_letter == "*":
            show_possible_matches(get_guessed_word(
                secret_word, letters_guessed))
            continue

        if not(guess_is_valid(new_letter)):
            if warnings_remaining > 0:
                warnings_remaining -= 1
                print('Oops! That is not a valid letter. You have ' + str(warnings_remaining) +
                      ' warnings remaining: ' + get_guessed_word(secret_word, letters_guessed))
                print('-----------------------------------------------')
                continue
            else:
                guesses_remaining -= 1
                print('Oops! That is not a valid letter. You have ' + str(guesses_remaining) +
                      ' guesses remaining: ' + get_guessed_word(secret_word, letters_guessed))
                print('-----------------------------------------------')
                continue

        if check_list(new_letter, letters_guessed):
            if warnings_remaining > 0:
                warnings_remaining -= 1
                print('Oops! You have already guessed that letter. You have ' + str(warnings_remaining) +
                      ' warnings remaining: ' + get_guessed_word(secret_word, letters_guessed))
                print('-----------------------------------------------')
                continue
            else:
                guesses_remaining -= 1
                print('Oops! You have already guessed that letter. You have ' + str(guesses_remaining) +
                      ' guesses remaining: ' + get_guessed_word(secret_word, letters_guessed))
                print('-----------------------------------------------')
                continue

        letters_guessed = letters_guessed + new_letter

        # check if letter is in secret word
        if word_contains_letter(new_letter, secret_word):
            print('Good Guess: ' + get_guessed_word(secret_word, letters_guessed))
            print('-----------------------------------------------')

        # let user know they've guessed wrong
        else:
            vowels = 'aeiou'
            vowel_guessed = False
            for letter in vowels:
                if letter == new_letter:
                    vowel_guessed = True

            if vowel_guessed:
                guesses_remaining -= 2
            else:
                guesses_remaining -= 1

            print('Oops! That letter is not in my word: ' +
                  get_guessed_word(secret_word, letters_guessed))
            print('-----------------------------------------------')

        if is_word_guessed(secret_word, letters_guessed):
            game_won = True
            total_score = len(letters_guessed) * guesses_remaining

    if game_won:
        print('Congratulations, you won!')
        print('Your total score for this game was: ' + str(total_score))
    else:
        print('Sorry, you ran out of guesses. The word was ' + secret_word + '.')


# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.

if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.

    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)

###############

    # To test part 3 re-comment out the above lines and
    # uncomment the following two lines.

    # secret_word = choose_word(wordlist)
    # hangman_with_hints(secret_word)
