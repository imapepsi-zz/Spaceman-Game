"""
Mia Seppi
8/9/2019 - Friday
Invent with Python Book Chapter 7 & 8 - Spaceman Game
"""

from Properties import *
import random


def playGame():
    #Secret Word, correctList, missedList
    secretWord = random.choice(wordList)
    correctList = ""
    missedList = ""
    pastGuesses = ""
    gameStatus = "Playing"

    print("S P A C E M A N")
    print("")
    while gameStatus == "Playing":
        #Show the drawing
        displayBoard(correctList, missedList, secretWord)

        #Ask for a letter (If letter was already chosen ask again)
        currentGuess = getGuess(pastGuesses)
        pastGuesses += currentGuess

        #Letter is in word or Not
        correctList, missedList = checkGuess(currentGuess, correctList, missedList, secretWord)

        #Check game status
        gameStatus = checkWin(correctList, missedList, secretWord)
    
    if gameStatus == "Win":
        print("Congratulations! You Won!")
        print("Secret Word: {}".format(secretWord))

    elif gameStatus == "Lost":
        print("Sorry, you lost.")
        print("Secret Word: {}".format(secretWord))

    print("")

#Play
while True:
    playGame()

    again = playAgain()

    while again != "yes" and again != "no":
        print("Please enter a valid response.")
        again = playAgain()

    if again == "yes":
        continue
    elif again == "no":
        break



print("")
input("Press any key to continue...")