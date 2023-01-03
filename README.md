# A GAME STATION USING PYTHON
#### Video Demo:  <https://youtu.be/OKdYVOwTz1M>
#### Description:
This program has two mini games nested in 1 program(as pf today). When a user runs the program the user is greeted with greetings and a menu is displayed. The menu has three options namely.
1 Play recreated version of Wordle
2 Play recreated version of Hangman
3 Quit the program

Once entered the proper choice between 1 and 2. Rules for the respective game is displayed
##### For the game: Wordle
The rules for the game are simple.
The user has to guess a five letter word which generated randomly(using random library) from the module "english-words". The user can input only a five letter word, if the input is incorrect or is not a word an incorrect message is printed and the user is prompted to enter the word again. The user only has 6 attempts to guess the words. Invalid inputs doesn't get counted towards the attempt. After every attempt the user is shown the result of their guess and the number of attempts remaining. The result of their is displayed in upto three different colors (Red,Yellow,Green).
1) Red    : This color indicates that the text is RED because the alphabet doesnt exist in the correct word.
2) Yellow : This color indicates that the text is YELLOW because the alphabet does exist in the word but not in its correct position.
3) Green  : This color indicates that the text is GREEN because the alphabet does exit in the correct word and it also in its correct position.

If the user fails to guess the word in 6 tries than user is appreciated and the correct word for the game is displayed. If the User guess the answer, than user is congratulated on guesssing the correct answer. In either case the user is returned to the menu again for input to whether continue playing the same or different game or to quit the program.
##### For the game: Hangman
The rules for this game are quite simple
In this game as well the user needs to guess a five letter word which is generated randomly from the english-words module.The user has to guess the word in only 6 tries. The user has to input a single alphabet. Any input other than a alphabet will be rejected by the program and will reprompt the user for the input. Once the user has given the program a valid input than the user can see their current progress by the ascii design of the hangman appearing on incorrect inputs. The user is than shown a row in which "_" is used for the alphabets not yet guessed and proper alphabets in upper case if they have been guessed. On the next line the user is shown all the remaining alphabets which are not yet guessed by the user and can be used as the input for the next guess. At any given moment the user can see the hangman and the remaining alphabets so that the user will know the current status of the progress in the game. Once the user has used all of their lives the user is than appreciated and the correct word is displayed.

After either of the game is played by the user. The user is than returned back to the menu and prompted again whether to continue playing or end the program. If the user decides to end the program, they are thanked for their time and the program ends.

##### Libraries used in the Program:
1)sys:
    This library is used to end the program
2)string:
    This library is used to get all the alphabets in the character set
3)tabulate:
    This library is used to print rows in the game of Hangman
4)english-words:
    This library is used to get all the english words in the dictionary
5)random:
    This library is used to generate a random word using choice function from the list of words acquired from "english-words" library
6)simple-colors:
    This library is used to color the characters of the word

ADDITIONAL FILES USED IN THE PROGRAM
1) hangman_image.py:
    This file is used for importing the image of the hangman in the form of a function that can be called in any program and can be accessed as an interger passed to the function as a variable
