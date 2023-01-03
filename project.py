# importing all the libraries

from string import ascii_lowercase
from sys import exit
from random import choice
from tabulate import tabulate
from english_words import english_words_set
from simple_colors import green,red,yellow
from hangman_image import hangman_func


def main ():
    '''
    This is my main function which calls the my game function
    '''
    game()

def menu():
    """
    This funtion displays the menu for the game.
    Parameters: This function doesnt take any parameters
    Returns : Doesnt return anything
    """
    print("Welcome to the Game Menu:")
    print("1. Wordle")
    print("2. Hangman")
    successful = False
    while not successful:
        game_choice = input("Enter '1' to play Wordle or '2' to play Hangman or '3' to quit: ")
        if validate_menu_input(game_choice):
            game_choice = int(game_choice)
            if game_choice == 1:
                wordle()
            elif game_choice == 2:
                hangman()
            elif game_choice == 3:
                print("Thank you for your time!!\nHave a nice day")
                exit()
        else:
            print("Invalid Input")
            continue

def wordle():
    '''
    This function runs the entire game of Wordle
    Parameters : None
    Returns : Doesn't return anything
    '''

    print("welcome to the game of wordle".upper())
    print("x-----------------x\nRules :\n1) You need to guess a five letter word chosen at random from a list of words.\n2) You can input 'only' one word at a time.\n3)You only have 6 attempts to guess the word.\n4)When the program outputs 'Invalid Word' that means the word you input doesnt exist in the pool of the words used in this game.\n5)When the program outputs 'Invalid Input!' that means the input that you gave to the program is not a 5 letter word or it contain characters other than alphabets.\n6)For input do not use any white space in your input.\n7) The characters in your result indicate different meaning with their color.\n8) \033[31mRED\033[0m indicates the alphabet doesnt exist in the correct word.\n9) \033[33mYELLOW\033[0m indicates the alphabet exists in the word but it is not in the right position.\n10) \033[32mGREEN\033[0m indicates the alphabet exists in the word but it is in the right position.")
    input("Press any key to play")
    found_word = False
    index = 0
    correct_word = random_word()
    while index < 6:
        guess_word = input("Enter the word: ")
        guess_word = guess_word.lower()
        if validate_input_wordle(guess_word):
            if check_match(guess_word,correct_word):
                print("Correct Guess!!")
                found_word = True
                break
            else:
                colored_word = color_word(guess_word, correct_word)
                index += 1
                print(colored_word+f" Number of attempts remaining: {(6-index)}")
                continue
        else:
            if guess_word.isalpha():
                print("Invalid Word!")
            else:
                print("Invalid Input!!")
            continue
    if not found_word:
        print(f"Nice Try! \nCorrect word is {correct_word}")

def hangman():
    '''
    This function runs the entire game of Hangman
    Parameters : None
    Returns : Doesn't return anything
    '''
    print("welcome to the game of hangman".upper())
    print("x-----------------x\nRules :\n1) You need to guess the alphabets in a five letter word chosen at random from a list of words.\n2) You can input 'only' one alphabet at a time.\n3) You only have 6 attempts to guess the word.\n4) If a right letter is given the letter appears in the row.\n5) If an incorrect letter is given than hangman starts appearing in the output screen.\n6) The remaining alphabets will be shown below of your attempt.")
    input("Press any key to play")
    alphabet_list = list(ascii_lowercase)
    correct_word = random_word()
    list_correct = []
    list_output = ["_","_","_","_","_"]
    index = 0
    for char in correct_word:
        list_correct.append((char,index))
        index +=1

    print(hangman_func(0))
    index = 0
    word_found = False
    while index <6:
        alphabet = input("Enter the alphabet: ")
        if validate_input_hangman(alphabet):
            if alphabet not in alphabet_list:
                print("Alphabet has already been entered before")
                print(hangman_func(index+1))
                print(tabulate([list_output],tablefmt = "grid") +"\n"+ str(alphabet_list))
                continue
            if alphabet in correct_word:
                for index_list in list_correct:
                    if index_list[0] == alphabet:
                       list_output[index_list[1]] = alphabet.upper()
                print(hangman_func(index))
                alphabet_list.remove(alphabet)
                print(tabulate([list_output],tablefmt = "grid") +"\n"+ str(alphabet_list))
                if list_output == [char for char in correct_word]:
                    print("Correct guess\nThank you for playing")
                    word_found = True
                    break
            else:
                alphabet_list.remove(alphabet)
                print(hangman_func(index+1))
                print(tabulate([list_output],tablefmt = "grid") +"\n"+ str(alphabet_list))
                index+=1
        else:
            print(hangman_func(index))
            print("Not an alphabet!\nTry Again\n" + str(alphabet_list))
            continue
    if not word_found:
        print(f"Nice try!\nCorrect word is {correct_word}")



def validate_input_hangman(alphabet):
    '''
    This function validates the input passed in the hangman function. It checks if the input is alphabet or not.
    :param alphabet: String: String character
    :return: Boolean: True if input is a character, False otherwise
    '''
    valid = False
    if alphabet.isalpha():
        if len(alphabet) == 1:
            valid = True
    return valid


def validate_input_wordle(guess_word):
    '''
    This function validates the input passed in the wordle function. It checks if the input is a valid word from the list of words obtained from english-words library.
    Parameters : 1
    Parmeter type : String
    Returns : True if the input is alphabet | False if the input is not an alphabet
    Return type: Boolean
    '''
    valid_word = False
    if guess_word.isalpha():
        if len(guess_word) == 5:
            if guess_word in five_letter_word_list:
                valid_word = True
    return valid_word


def check_match(guess_word,correct_word):
    '''
    This function checks whether the input passed in the function are an exact match or not
    Parameters : 2
    Parmeter type : String and String
    Returns : True if the input is alphabet | False if the input is not an alphabet
    Return type: Boolean
    '''
    if guess_word == correct_word:
        return True
    else:
        return False


def random_word():
    '''
    This function returns a random five letter word from the english dictionary
    '''
    global five_letter_word_list
    five_letter_word_list = []
    for word in english_words_set:
        if len(word) == 5:
            five_letter_word_list.append(word.lower())
    random_word = choice(five_letter_word_list)
    return random_word

def color_word(guess_word, correct_word):
    '''
     this function colors the guess_word as per the definition of the game
     if the alphabet is in the word and in the correct position the alphabet is colored red
     if the alphabet is in the word and in the wrong position the alphabet is colored yellow
     if the alphabet is not in the word then the alphabet is red
    '''
    word_colored = ""
    index = 0
    for char in guess_word:
        if char in correct_word:
            if char == correct_word[index]:
                word_colored+=green(char.upper()) +" "
            else:
                word_colored+=yellow(char.upper()) +" "
        else:
            word_colored+=red(char.upper()) +" "
        index += 1
    return word_colored

def validate_menu_input(input):
    '''
    This function validates the input passed in the menu function. It checks if the input either (1,2,3)
    :param alphabet: String: String character
    :return: Boolean: True if input is a character, False otherwise
    '''
    valid = False
    try:
        if int(input) in (1,2,3):
            valid = True
            return valid
    except:
        return valid
    return valid

def game():
    menu()



if __name__ == "__main__":
    main()
