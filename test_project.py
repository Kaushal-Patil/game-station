# tests for the main project
from project import *

five_letter_word_list = []
def test_validate_menu_input():
    #check the input for valid and invalid cases for game menu
    assert validate_menu_input("1") == True
    assert validate_menu_input("f") == False

def test_validate_input_hangman():
    #check the input for valid and invalid cases for hangman input
    assert validate_input_hangman("d") == True
    assert validate_input_hangman("1") == False

def test_check_match():
    #check the input for valid and invalid cases for checks in wordle game
    assert check_match("doubt","doubt") == True
    assert check_match("doubt","treat") == False

def test_color_word():
    #checks the color change in color_word function
    assert color_word("blank","treat") == "\033[31mB\033[0m \033[31mL\033[0m \033[33mA\033[0m \033[31mN\033[0m \033[31mK\033[0m "
    assert color_word("dread","treat") == "\033[31mD\033[0m \033[32mR\033[0m \033[32mE\033[0m \033[32mA\033[0m \033[31mD\033[0m "